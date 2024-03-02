import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Potato\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Path to the image
image_path = 'C:\\Users\\Potato\\Desktop\\Yes.png'

# Open the image
img = Image.open(image_path)

# Use pytesseract to read the text
text = pytesseract.image_to_string(img)

# Print the text
print(text)