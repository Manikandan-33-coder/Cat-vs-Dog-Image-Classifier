import os
import zipfile
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# ✅ (Optional) Extract ZIP Dataset — uncomment if needed
# zip_path = 'C:/Users/smgop/Desktop/Task/Gog vs cat/Dataset/archive (17).zip'
# with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#     zip_ref.extractall('C:/Users/smgop/Desktop/Task/Gog vs cat/')

# ✅ Resize Cat and Dog Images
target_size = (150, 150)
cat_dir = 'C:/Users/smgop/Desktop/Task/Gog vs cat/archive (17)/animals/cat'
dog_dir = 'C:/Users/smgop/Desktop/Task/Gog vs cat/archive (17)/animals/dog'

# Resize Cat images
for img_name in os.listdir(cat_dir):
    img_path = os.path.join(cat_dir, img_name)
    try:
        img = Image.open(img_path)
        img = img.resize(target_size)
        img.save(img_path)
    except:
        print(f"Couldn't process {img_path}")

# Resize Dog images
for img_name in os.listdir(dog_dir):
    img_path = os.path.join(dog_dir, img_name)
    try:
        img = Image.open(img_path)
        img = img.resize(target_size)
        img.save(img_path)
    except:
        print(f"Couldn't process {img_path}")

# ✅ Data Preparation using ImageDataGenerator
Datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

# Training Data Generator
train_generator = Datagen.flow_from_directory(
    'C:/Users/smgop/Desktop/Task/Gog vs cat/archive (17)/animals',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='training'
)
print(train_generator.class_indices)

# Validation Data Generator
validation_generator = Datagen.flow_from_directory(
    'C:/Users/smgop/Desktop/Task/Gog vs cat/archive (17)/animals',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)
print(validation_generator.class_indices)

# ✅ Build CNN Model
model = Sequential()

model.add(Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(32, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(128, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid'))

# Compile the Model
model.compile(
    optimizer=Adam(),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Show Model Summary
model.summary()

# ✅ Train the Model
history = model.fit(
    train_generator,
    epochs=40,
    validation_data=validation_generator
)

# ✅ Save Trained Model
model.save("C:/Users/smgop/Desktop/Task/Gog vs cat/cat_dog_cnn_model.h5")
print("✅ Model saved successfully.")
