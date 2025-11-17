from flask import Flask, request, jsonify
from predictor import predict_image # Keep your image predictor
import base64
import requests
# REMOVE all transformers imports (AutoTokenizer, pipeline, etc.)

# NEW: Import your knowledge base directly
from knowledge_base import treatment_kb, SAFETY_NOTE 

app = Flask(__name__)

# --- Image Prediction Model Paths (Unchanged) ---
MODEL_PATHS = {
    "disease": {"model": "models/disease_model_final.h5", "classes": "models/disease_classes.npy"},
    "rice": {"model": "models/rice_model_final.h5", "classes": "models/rice_classes.npy"},
    "banana": {"model": "models/banana_model_final.h5", "classes": "models/banana_classes.npy"}
}

# --- Root Endpoint (Unchanged) ---
@app.route("/")
def index():
    return "<h1>Plant Diagnosis API is running!</h1>"

# --- Image Prediction Endpoint (Unchanged) ---
@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'plant_type' not in data or 'image' not in data:
        return jsonify({"error": "Invalid input: 'plant_type' and 'image' are required."}), 400

    plant_type = data['plant_type']
    model_to_use = 'disease' # Default
    if plant_type.lower() == 'rice':
        model_to_use = 'rice'
    elif plant_type.lower() == 'banana':
        model_to_use = 'banana'

    try:
        image_data = base64.b64decode(data['image'])
        paths = MODEL_PATHS[model_to_use]
        prediction_result = predict_image(paths["model"], paths["classes"], image_data)
        detected_plant_name = prediction_result.split('___')[0] if '___' in prediction_result else plant_type

        return jsonify({
            "prediction": prediction_result,
            "plant_type": detected_plant_name
        })
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": f"An error occurred during prediction: {e}"}), 500

# --- Chat Endpoint (Unchanged, still calls Ollama) ---
@app.route("/chat", methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "Invalid input: 'prompt' is required."}), 400

    try:
        ollama_payload = {
            "model": "gemma:2b", # Using the lighter model
            "prompt": data['prompt'],
            "stream": False
        }
        response = requests.post("http://localhost:11434/api/generate", json=ollama_payload)
        response.raise_for_status()
        return jsonify({"response": response.json()['response']})

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama server at http://localhost:11434. Is Ollama running?")
        return jsonify({"error": "Could not connect to Ollama server. Please ensure it is running."}), 500
    except Exception as e:
        print(f"Error during chat: {e}")
        return jsonify({"error": f"An error occurred during chat: {e}"}), 500

# --- REMOVED /translate ENDPOINT ---

# --- NEW: Updated Treatment Advice Endpoint ---
@app.route("/get_treatment", methods=['POST'])
def get_treatment():
    data = request.get_json()
    # Now expecting lang code from the frontend
    if not data or 'disease' not in data or 'soil' not in data or 'season' not in data or 'lang' not in data:
        return jsonify({"error": "Invalid input: 'disease', 'soil', 'season', and 'lang' are required."}), 400

    disease_clean = data['disease'].split(' (')[0]
    soil_key = data['soil'].lower()
    season_key = data['season'].lower()
    lang_code = data['lang'] # Get the language code

    # Get the knowledge base entry for the disease, or the default one
    disease_info = treatment_kb.get(disease_clean, treatment_kb['default'])

    # --- Assemble the custom response in the correct language ---
    
    # Helper function to safely get the translated text
    def get_translated_text(section, key, lang, fallback_lang='en'):
        entry = section.get(key, section.get('general', {}))
        return entry.get(lang, entry.get(fallback_lang, "No information available."))

    # 1. Get soil advice
    soil_advice = get_translated_text(disease_info['soils'], soil_key, lang_code)
    
    # 2. Get season advice
    season_advice = get_translated_text(disease_info['seasons'], season_key, lang_code)
    
    # 3. Get action plan
    action_plan = disease_info.get('action_plan', treatment_kb['default']['action_plan']) # Fallback to default action plan
    cultural_advice = get_translated_text(action_plan, 'cultural', lang_code)
    organic_advice = get_translated_text(action_plan, 'organic', lang_code)
    chemical_advice = get_translated_text(action_plan, 'chemical', lang_code)
    
    # 4. Get safety note
    safety_note = SAFETY_NOTE.get(lang_code, SAFETY_NOTE['en'])

    # 5. Build the final response string
    # We use English labels for consistency, the content will be translated
    assembled_response = (
        f"**Advice for {disease_clean}**\n\n"
        f"**On {soil_key.capitalize()} Soil:**\n{soil_advice}\n\n"
        f"**For the {season_key.capitalize()} Season:**\n{season_advice}\n\n"
        f"--- \n"
        f"**Action Plan:**\n\n"
        f"**Cultural:** {cultural_advice}\n\n"
        f"**Organic:** {organic_advice}\n\n"
        f"**Chemical:** {chemical_advice}\n\n"
        f"--- \n"
        f"{safety_note}"
    )

    # Return the assembled, pre-translated text
    return jsonify({"treatment_text": assembled_response})


if __name__ == "__main__":
    app.run(debug=True)