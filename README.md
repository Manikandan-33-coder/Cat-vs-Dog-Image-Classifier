
# 🐱🐶 Cat vs Dog Image Classifier

A deep learning-based image classification project that identifies whether an image contains a **cat** or a **dog**. This project uses a Convolutional Neural Network (CNN) model built with TensorFlow/Keras and OpenCV, trained on a labeled image dataset.

---

## 📌 Features

- 📦 Classifies images into two categories:
  - **Cat**
  - **Dog**
- 🖼️ Supports image upload for classification.
- 📈 Displays prediction results clearly.
- Simple and user-friendly application.

---

## 🗂️ Project Structure

```
Cat-vs-Dog-Image-Classifier/
├── Dataset/
│   ├── Cat/
│   └── Dog/
├── model/
│   └── cat_dog_classifier.h5
├── app.py
├── requirements.txt
├── README.md
└── images/
    └── test_sample.jpg
```

---

## 🚀 Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/Manikandan-33-coder/Cat-vs-Dog-Image-Classifier.git
cd Cat-vs-Dog-Image-Classifier
```

2️⃣ **Create a virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

### 🖼️ Predict an Image

Run the app using:

```bash
python app.py
```

- Upload an image.
- The model will classify the image as **Cat** or **Dog** and display the result.

---

## 🧠 Model Details

- **Architecture:** Convolutional Neural Network (CNN)
- **Input Image Size:** 150x150 pixels
- **Training Data:** Image dataset containing labeled Cat and Dog images.
- **Optimizer:** Adam
- **Loss Function:** Binary Crossentropy
- **Accuracy Achieved:** ~97% on validation data.

---

## 📦 Requirements

The required Python packages are listed in `requirements.txt`, including:

- TensorFlow
- Keras
- OpenCV
- NumPy
- Matplotlib
- Flask (for web app)

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📊 Sample Result

![Sample Output](images/test_sample.jpg)

---

## 📚 References

- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [Keras Documentation](https://keras.io/)
- [OpenCV Documentation](https://docs.opencv.org/)

---

## 📬 Contact

**Manikandan Murugan**  
[GitHub Profile](https://github.com/Manikandan-33-coder)

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on [GitHub](https://github.com/Manikandan-33-coder/Cat-vs-Dog-Image-Classifier)!
