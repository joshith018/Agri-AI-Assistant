import numpy as np
import tensorflow as tf
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, precision_score, accuracy_score, f1_score, recall_score

def create_model(input_shape):
    """Creates a simple Keras sequential model."""
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def main():
    print("--- GENERATING DUMMY DATA ---")
    # 1. Generate synthetic classification data
    X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 2. Train two separate models (Simulating different weights)
    print("--- TRAINING MODEL A ---")
    model_a = create_model(X_train.shape[1])
    model_a.fit(X_train, y_train, epochs=5, verbose=0)
    
    print("--- TRAINING MODEL B ---")
    model_b = create_model(X_train.shape[1])
    model_b.fit(X_train, y_train, epochs=5, verbose=0)

    # 3. COMBINE WEIGHTS (Averaging Strategy)
    print("--- COMBINING WEIGHTS ---")
    weights_a = model_a.get_weights()
    weights_b = model_b.get_weights()

    # Calculate the average of the weights layer by layer
    averaged_weights = []
    for w_a, w_b in zip(weights_a, weights_b):
        averaged_weights.append((w_a + w_b) / 2)

    # 4. Create a new model and inject the combined weights
    combined_model = create_model(X_train.shape[1])
    combined_model.set_weights(averaged_weights)

    # 5. Make Predictions with the combined model
    print("--- EVALUATING COMBINED MODEL ---")
    y_pred_probs = combined_model.predict(X_test, verbose=0)
    y_pred = (y_pred_probs > 0.5).astype("int32").flatten()

    # 6. Calculate Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # 7. Output Results to Terminal
    print("\n" + "="*30)
    print("   COMBINED MODEL METRICS")
    print("="*30)
    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")
    print("="*30)
    
    # Detailed report
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()