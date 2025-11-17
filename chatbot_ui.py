import streamlit as st
import requests
import base64
from PIL import Image
import io

# --- Page Configuration ---
st.set_page_config(page_title="Farmer's AI Assistant", layout="wide")

# --- Translation Dictionaries (Full Version) ---
# This dictionary now *only* translates the UI itself
translations = {
    'en': {
        'title': "🤖 Farmer's AI Assistant",
        'description': "Ask me any farming question, or upload an image to diagnose a plant.",
        'sidebar_header': "🌿 Plant Diagnosis",
        'plant_selector': "1. Choose the plant you are uploading:",
        'soil_selector': "2. Select your Soil Type:",
        'season_selector': "3. Select your Current Season:",
        'uploader_label': "4. Upload an image...",
        'diagnosis_result': "The diagnosis for your uploaded image is:",
        'chat_prompt': "What is your question?",
        'thinking': "Thinking...",
        'error_api': "Error connecting to the model API:",
        'chat_error': "Error connecting to the chat model:",
        'treatment_fetching': "Fetching specific treatment advice...",
        'treatment_error': "Error fetching treatment advice:"
    },
    'kn': {
        'title': "🤖 ರೈತರ AI ಸಹಾಯಕ",
        'description': "ನನಗೆ ಯಾವುದೇ ಕೃಷಷಿ ಪ್ರಶ್ನೆಯನ್ನು ಕೇಳಿ, ಅಥವಾ ಸಸ್ಯವನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.",
        'sidebar_header': "🌿 ಸಸ್ಯ ರೋಗನಿರ್ಣಯ",
        'plant_selector': "1. ನೀವು ಅಪ್‌ಲೋಡ್ ಮಾಡುತ್ತಿರುವ ಸಸ್ಯವನ್ನು ಆರಿಸಿ:",
        'soil_selector': "2. ನಿಮ್ಮ ಮಣ್ಣಿನ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        'season_selector': "3. ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಋತುವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        'uploader_label': "4. ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ...",
        'diagnosis_result': "ನೀವು ಅಪ್‌ಲೋಡ್ ಮಾಡಿದ ಚಿತ್ರದ ರೋಗನಿರ್ಣಯ:",
        'chat_prompt': "ನಿಮ್ಮ ಪ್ರಶ್ನೆ ಏನು?",
        'thinking': "ಯೋಚಿಸುತ್ತಿದೆ...",
        'error_api': "ಮಾದರಿ API ಗೆ ಸಂಪರ್ಕಿಸುವಲ್ಲಿ ದೋಷ:",
        'chat_error': "ಚಾಟ್ ಮಾದರಿಗೆ ಸಂಪರ್ಕಿಸುವಲ್ಲಿ ದೋಷ:",
        'treatment_fetching': "ನಿರ್ದಿಷ್ಟ ಚಿಕಿತ್ಸೆಯ ಸಲಹೆಯನ್ನು ತರಲಾಗುತ್ತಿದೆ...",
        'treatment_error': "ಚಿಕಿತ್ಸೆಯ ಸಲಹೆಯನ್ನು ತರುವಲ್ಲಿ ದೋಷ:"
    },
    'te': {
        'title': "🤖 రైతు AI సహాయకుడు",
        'description': "నన్ను ఏదైనా వ్యవసాయ ప్రశ్న అడగండి, లేదా మొక్కను నిర్ధారించడానికి చిత్రాన్ని అప్‌లోడ్ చేయండి.",
        'sidebar_header': "🌿 మొక్కల నిర్ధారణ",
        'plant_selector': "1. మీరు అప్‌లోడ్ చేస్తున్న మొక్కను ఎంచుకోండి:",
        'soil_selector': "2. మీ నేల రకాన్ని ఎంచుకోండి:",
        'season_selector': "3. మీ ప్రస్తుత సీజన్‌ని ఎంచుకోండి:",
        'uploader_label': "4. చిత్రాన్ని అప్‌లోడ్ చేయండి...",
        'diagnosis_result': "మీరు అప్‌లోడ్ చేసిన చిత్రం యొక్క నిర్ధారణ:",
        'chat_prompt': "మీ ప్రశ్న ఏమిటి?",
        'thinking': "ఆలోచిస్తున్నాను...",
        'error_api': "మోడల్ APIకి కనెక్ట్ చేయడంలో లోపం:",
        'chat_error': "చాట్ మోడల్‌కి కనెక్ట్ చేయడంలో లోపం:",
        'treatment_fetching': "నిర్దిష్ట చికిత్స సలహాను తెస్తున్నాము...",
        'treatment_error': "చికిత్స సలహాను పొందడంలో లోపం:"
    },
    'hi': {
        'title': "🤖 किसान एआई सहायक",
        'description': "मुझसे कोई भी खेती का सवाल पूछें, या किसी पौधे का निदान करने के लिए एक छवि अपलोड करें।",
        'sidebar_header': "🌿 पौधे का निदान",
        'plant_selector': "1. वह पौधा चुनें जिसे आप अपलोड कर रहे हैं:",
        'soil_selector': "2. अपनी मिट्टी का प्रकार चुनें:",
        'season_selector': "3. अपना वर्तमान मौसम चुनें:",
        'uploader_label': "4. एक छवि अपलोड करें...",
        'diagnosis_result': "आपकी अपलोड की गई छवि का निदान है:",
        'chat_prompt': "आपका क्या प्रश्न है?",
        'thinking': "सोच रहा हूँ...",
        'error_api': "मॉडल एपीआई से कनेक्ट करने में त्रुटि:",
        'chat_error': "चैट मॉडल से कनेक्ट करने में त्रुटि:",
        'treatment_fetching': "विशिष्ट उपचार सलाह प्राप्त की जा रही है...",
        'treatment_error': "उपचार सलाह प्राप्त करने में त्रुटि:"
    }
}

# --- API Endpoints ---
FLASK_PREDICT_URL = "http://127.0.0.1:5000/predict"
FLASK_CHAT_URL = "http://127.0.0.1:5000/chat"
# REMOVED: FLASK_TRANSLATE_URL
FLASK_TREATMENT_URL = "http://127.0.0.1:5000/get_treatment" # Updated endpoint

# --- REMOVED translate_text FUNCTION ---

# --- Language Selection ---
language_options = {'English': 'en', 'ಕನ್ನಡ (Kannada)': 'kn', 'తెలుగు (Telugu)': 'te', 'हिन्दी (Hindi)': 'hi'}
selected_language_name = st.selectbox("Select Language / ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ / భాషను ఎంచుకోండి / भाषा चुनें", options=language_options.keys())
lang_code = language_options[selected_language_name]
ui_texts = translations[lang_code]

# --- Main App UI ---
st.title(ui_texts['title'])
st.write(ui_texts['description'])

SUPPORTED_PLANTS = [
    "Apple", "Blueberry", "Cherry", "Corn (Maize)", "Grape", "Orange", "Peach",
    "Bell Pepper", "Potato", "Raspberry", "Soybean", "Squash", "Strawberry",
    "Tomato", "Banana", "Rice"
]

# --- Initialize Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_diagnosis" not in st.session_state:
    st.session_state.last_diagnosis = None
if "soil_type" not in st.session_state:
    st.session_state.soil_type = "Red"
if "season" not in st.session_state:
    st.session_state.season = "Monsoon"


# --- Sidebar ---
with st.sidebar:
    st.header(ui_texts['sidebar_header'])
    selected_plant = st.selectbox(ui_texts['plant_selector'], SUPPORTED_PLANTS)

    # Dropdowns for Soil and Season
    soil_type = st.selectbox(
        ui_texts['soil_selector'],
        ('Red', 'Black', 'Alluvial', 'General'),
        key='soil_type'
    )
    
    season = st.selectbox(
        ui_texts['season_selector'],
        ('Monsoon', 'Summer', 'Winter', 'General'),
        key='season'
    )
    
    uploaded_file = st.file_uploader(ui_texts['uploader_label'], type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption=f'Uploaded Image ({selected_plant}).')
        with st.spinner(ui_texts['thinking']):
            buffered = io.BytesIO()
            image = Image.open(uploaded_file)
            if image.mode != 'RGB': image = image.convert('RGB')
            image.save(buffered, format="JPEG")
            img_bytes = buffered.getvalue()
            encoded_string = base64.b64encode(img_bytes).decode('utf-8')
            
            payload = {"plant_type": selected_plant, "image": encoded_string}
            
            try:
                # --- Call Prediction API ---
                response = requests.post(FLASK_PREDICT_URL, json=payload)
                response.raise_for_status()
                result = response.json()

                # Get the English prediction (e.g., "Apple___Apple_scab (99.1%)")
                english_prediction = result.get("prediction", "No prediction found.")
                # Store the clean disease name (e.g., "Apple___Apple_scab")
                st.session_state.last_diagnosis = english_prediction.split(' (')[0] 

                # Format for display (e.g., "Apple - Apple_scab (99.1%)")
                display_prediction = english_prediction.replace("___", " - ") 
                
                diagnosis_label = ui_texts['diagnosis_result']
                st.session_state.messages.append({"role": "assistant", "content": f"{diagnosis_label} **{display_prediction}**"})

            except requests.exceptions.RequestException as e:
                st.error(f"{ui_texts['error_api']} {e}")

# --- Main Chat Interface ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(ui_texts['chat_prompt']):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Check for treatment query ---
    is_treatment_query = False
    last_diagnosis = st.session_state.get("last_diagnosis")
    treatment_keywords = ["treat", "cure", "manage", "solution", "what now", "fix", "remedy", "advice", "how to"]

    if last_diagnosis and any(keyword in prompt.lower() for keyword in treatment_keywords):
        is_treatment_query = True

    with st.chat_message("assistant"):
        with st.spinner(ui_texts['thinking']):
            if is_treatment_query:
                # --- Get PRE-TRANSLATED Treatment Advice ---
                st.write(ui_texts['treatment_fetching'])
                try:
                    # Send disease, soil, season, AND LANGUAGE
                    payload = {
                        "disease": last_diagnosis,
                        "soil": st.session_state.soil_type,
                        "season": st.session_state.season,
                        "lang": lang_code  # <-- Send the user's language
                    }
                    response = requests.post(FLASK_TREATMENT_URL, json=payload)
                    response.raise_for_status()
                    
                    # Get the pre-translated advice block
                    advice_block = response.json().get("treatment_text", "Advice not found.")
                    
                    st.markdown(advice_block)
                    st.session_state.messages.append({"role": "assistant", "content": advice_block})
                    st.session_state.last_diagnosis = None # Clear diagnosis

                except requests.exceptions.RequestException as e:
                    st.error(f"{ui_texts['treatment_error']} {e}")

            else:
                # --- General Chat Flow (Ollama) ---
                try:
                    # Send the raw prompt to Ollama.
                    # Ollama will try to respond in the language it receives.
                    payload = {"prompt": prompt} 
                    response = requests.post(FLASK_CHAT_URL, json=payload)
                    response.raise_for_status()
                    assistant_response = response.json()['response']
                    
                    st.markdown(assistant_response)
                    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                except Exception as e:
                    st.error(f"{ui_texts['chat_error']} {e}")