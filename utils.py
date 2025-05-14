import pandas as pd
import os
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model as tf_load_model
from PIL import Image
import io
import base64
import hashlib
from pymongo import MongoClient
from datetime import datetime
import json  # <-- For reading class names from a JSON file

# Set your MongoDB connection string here
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["medplant_app"]
users_col = db["users"]
history_col = db["history"]

# --------------------- AUTH ---------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password):
    user = users_col.find_one({"email": email, "password": hash_password(password)})
    return bool(user)

def signup(email, password):
    if users_col.find_one({"email": email}):
        return False
    users_col.insert_one({"email": email, "password": hash_password(password)})
    return True

# --------------------- MODEL ---------------------
@st.cache_resource
def load_model(model_path="best_mobilenet_model.h5", class_names_path="class_names.json"):
    model = tf_load_model(model_path)

    class_names = None
    if hasattr(model, "class_names"):
        class_names = list(model.class_names)
    elif os.path.exists(class_names_path):
        with open(class_names_path, "r") as f:
            class_names = json.load(f)
    else:
        st.error("Class names not found. Please provide 'class_names.json' file.")
        st.stop()

    return model, class_names

def preprocess_image(image):
    image = image.resize((224, 224))
    img_array = tf.keras.utils.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0) / 255.0
    return img_array

def predict_image(image, model, class_names):
    img = preprocess_image(image)
    pred = model.predict(img)[0]
    idx = np.argmax(pred)
    return class_names[idx], pred[idx]

# --------------------- CSV ---------------------
@st.cache_data
def get_plant_details(csv_path):
    return pd.read_csv(csv_path)

# --------------------- HISTORY ---------------------
def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def decode_image(encoded_str):
    return Image.open(io.BytesIO(base64.b64decode(encoded_str)))

def save_history(user, prediction, image):
    encoded = encode_image(image)
    record = {
        "user": user,
        "prediction": prediction,
        "image": encoded,
        "timestamp": datetime.now()
    }
    history_col.insert_one(record)

def get_history(user):
    return list(history_col.find({"user": user}))

def delete_history(record_id):
    history_col.delete_one({"_id": record_id})



# import tensorflow as tf
# import numpy as np
# import pandas as pd
# from PIL import Image
# from io import BytesIO
# import base64
# from pymongo import MongoClient
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow logs

# IMG_SIZE = (224, 224)

# # MongoDB setup
# MONGO_URI = "mongodb://localhost:27017/"
# client = MongoClient(MONGO_URI)
# db = client["medplant_app"]
# users_col = db["users"]
# history_col = db["history"]

# def load_model(model_path):
#     model = tf.keras.models.load_model(model_path)
#     class_names = model.class_names if hasattr(model, 'class_names') else sorted(os.listdir("your_train_dir"))
#     return model, class_names

# def predict_image(img_file, model, class_names):
#     image = Image.open(img_file).convert("RGB")
#     image = image.resize(IMG_SIZE)
#     img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
#     predictions = model.predict(img_array)
#     predicted_class = class_names[np.argmax(predictions)]
#     confidence = float(np.max(predictions))
#     return predicted_class, confidence

# def get_plant_details(csv_path):
#     return pd.read_csv(csv_path)

# # User Auth
# def signup(email, password):
#     if users_col.find_one({"email": email}):
#         return False
#     users_col.insert_one({"email": email, "password": password})
#     return True

# def login(email, password):
#     user = users_col.find_one({"email": email})
#     return user and user['password'] == password

# # Save history
# def encode_image(img):
#     buf = BytesIO()
#     img.save(buf, format='PNG')
#     return base64.b64encode(buf.getvalue()).decode()

# def decode_image(img_str):
#     return Image.open(BytesIO(base64.b64decode(img_str)))

# def save_history(email, prediction, image):
#     img_str = encode_image(image)
#     history_col.insert_one({
#         "email": email,
#         "prediction": prediction,
#         "image": img_str
#     })

# def get_history(email):
#     return list(history_col.find({"email": email}))

# def delete_history(item_id):
#     history_col.delete_one({"_id": item_id})
