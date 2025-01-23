from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

model = tf.keras.models.load_model('./final_cnn_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['image']
        img = load_img(file, target_size=(150, 150))  # Adjust to your model input size
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        result = model.predict(img_array)
        prediction = 'dog' if result[0][0] > 0.5 else 'cat'
        
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
