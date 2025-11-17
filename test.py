import requests
import base64

API_URL = "http://127.0.0.1:5000/predict"

# --- CONFIGURE YOUR TEST HERE ---
IMAGE_PATH = "C:/Users/malia/OneDrive/Pictures/Screenshots/Screenshot 2025-09-27 214241.png" # <-- CHANGE THIS
MODEL_TYPE = "disease"  # <-- CHANGE to "disease", "rice", or "banana"
# --- ------------------------ ---

with open(IMAGE_PATH, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

payload = {"model_type": MODEL_TYPE, "image": encoded_string}

try:
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    print("✅ Server Response:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"❌ An error occurred: {e}")