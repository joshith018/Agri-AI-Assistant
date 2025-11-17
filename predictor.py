import tensorflow as tf
import numpy as np
from PIL import Image
import io

# A dictionary to cache loaded models to avoid reloading them on every call
loaded_models = {}

def predict_image(model_path, class_list_path, image_bytes):
    """
    Loads a model and its class list, preprocesses an image,
    and returns the top prediction.
    """
    global loaded_models

    # Load model if not already in cache
    if model_path not in loaded_models:
        print(f"Loading model from: {model_path}")
        loaded_models[model_path] = tf.keras.models.load_model(model_path)
    model = loaded_models[model_path]
    
    # Load the class list
    class_names = np.load(class_list_path, allow_pickle=True)

    # Preprocess the image
    img = Image.open(io.BytesIO(image_bytes)).resize((224, 224))
    if img.mode != 'RGB': # Ensure image is in RGB format
        img = img.convert('RGB')
    
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) # Create a batch

    # Make prediction
    predictions = model.predict(img_array)
    
    # Decode prediction
    predicted_index = np.argmax(predictions)
    predicted_class_name = class_names[predicted_index]
    confidence = 100 * np.max(predictions)
    
    return f"{predicted_class_name} ({confidence:.2f}%)"
