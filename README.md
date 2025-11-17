# 🌱 Agri-AI: Hybrid Plant Disease Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Framework](https://img.shields.io/badge/Framework-Flask%20%7C%20Streamlit-green)

## 📜 Abstract
This project is a full-stack AI application designed to assist farmers in diagnosing plant diseases and nutrient deficiencies. It utilizes a **Hybrid Architecture**:
1.  **Deep Learning:** Custom-trained **EfficientNetV2B0** models for visual diagnosis of 38 classes (Disease + Rice/Banana Nutrient Deficiency).
2.  **Expert System:** A deterministic, rule-based engine for providing 100% safe, expert-verified treatment advice in local languages (Kannada, Telugu, Hindi).

## 🚀 Features
* **Multi-Crop Support:** Detects diseases in Tomato, Potato, Corn, etc., plus specific NPK deficiencies in Rice and Banana.
* **High Performance:** Average Accuracy of **~89%** with inference speed <50ms.
* **Safety First:** Uses a static Knowledge Base for treatment advice to prevent AI hallucinations.
* **Multilingual:** Real-time support for English, Kannada, Telugu, and Hindi.

## 🛠️ Tech Stack
* **Model:** EfficientNetV2B0 (Transfer Learning with Fine-Tuning)
* **Training:** TensorFlow/Keras on Google Colab (T4 GPU)
* **Backend:** Flask API
* **Frontend:** Streamlit
* **Tools:** NumPy, Scikit-Learn (for metrics)

## 📊 Model Performance
| Metric | Score |
| :--- | :--- |
| **Accuracy** | 89.00% |
| **Precision** | 88.42% |
| **Recall** | 89.01% |
| **F1-Score** | 88.25% |

**Working model**
![working model](https://github.com/joshith018/Agri-AI-Assistant/blob/main/farmer%20out.jpg)

## 🧠 Architecture
The system uses a **Partial Unfreezing Strategy**:
* **Backbone:** Frozen EfficientNetV2B0 (Retains generic visual features).
* **Top 20 Layers:** Unfrozen (Fine-tuned for Plant Pathology).
* **Head:** GlobalAveragePooling -> Dropout(0.4) -> Softmax.

## 💻 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Agri-AI-Assistant.git](https://github.com/YOUR_USERNAME/Agri-AI-Assistant.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the App:
    ```bash
    streamlit run app.py
    ```

## ⚠️ Limitation
The model is optimized for single-leaf images with simple backgrounds. Performance may vary in complex, cluttered field conditions.
## Team mates:- SV Joshith, Yadhu MR Gowda 
