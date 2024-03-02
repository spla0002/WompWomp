from flask import Flask, request, send_file
import os
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Potato\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    image = request.files['image']
    image.save(os.path.join(app.root_path, 'uploaded_image.png'))

    # Use pytesseract to read the text from the image
    text = pytesseract.image_to_string(Image.open('uploaded_image.png'))

    return text

if __name__ == '__main__':
    app.run()