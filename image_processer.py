from flask import Flask, request, send_file
import os
import pytesseract
from PIL import Image
from image_scanner import image_to_text
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Potato\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    image = request.files['image']
    image.save(os.path.join(app.root_path, 'uploaded_image.png'))
    text = image_to_text(image_path="Add image path here")

    return text

if __name__ == '__main__':
    app.run()