Cat vs Dog Image Classifier — Flask Web App
===========================================

Description:
------------
This project is a simple image classifier built using Convolutional Neural Networks (CNN) with TensorFlow/Keras to distinguish between cat and dog images. It also includes a Flask web application that allows users to upload an image and receive a prediction.

Folder Structure:
-----------------
Project/
│
├── Main.py               # Python script to preprocess data, build, and train the CNN model
├── app.py                # Flask web application to serve the model for image prediction
├── templates/
│   └── index.html        # Frontend HTML template for uploading images
├── static/
│   └── uploads/          # Folder where uploaded images are temporarily stored
├── Dataset/
│   └── archive (17)/
│       └── animals/
│           ├── cat/      # Cat images
│           └── dog/      # Dog images
└── cat_dog_cnn_model.h5  # Trained CNN model file saved after training

Requirements:
-------------
- Python 3.x
- TensorFlow
- Keras
- Flask
- Pillow (PIL)
- NumPy

Install required libraries using:
I will give the Dataset link give below pls download the dataset after you will run the program
Dataset link : https://www.kaggle.com/datasets/anthonytherrien/dog-vs-cat
