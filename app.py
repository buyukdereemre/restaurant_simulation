# app.py (backend)

from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('yemek_model_augmented.h5')
class_names = ['baklava', 'iskender', 'kellepacacorbasi', 'mercimekcorbasi', 'sutlac', 'tazefasulye']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            img_path = os.path.join('uploads', file.filename)
            file.save(img_path)

            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            preds = model.predict(img_array)
            predicted_index = np.argmax(preds)
            prediction = class_names[predicted_index]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    import os
    os.makedirs('uploads', exist_ok=True)
    print("Flask uygulaması başlıyor...")
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Hata çıktı: {e}")
