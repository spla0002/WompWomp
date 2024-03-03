# Recipe Finder  
This project is a web application with a custom built api that allows users to upload an image of their shopping receipt, extract the items purchased from the image using OCR (Optical Character Recognition) and image processing techniques, and then find a recipe that matches those ingredients. The application also allows users to email the recipe to themselves.  

## Features  
Custom API  
Image upload  
Image processing   
OCR for ingredient extraction  
Recipe matching  
Email functionality  

## Technologies Used  
Python
FastAPI
OpenCV
NumPy
Python-dotenv
OpenAI
Pytesseract
Pillow
Requests

## Installation  
Clone the repository
Install the required packages using pip install -r requirements.txt
Set up PATH variables as required
Run the application using uvicorn main:app --reload

## Usage  
Upload an image of a receipt
The application will extract the ingredients and find a recipe matching the items bought
You can then choose to email the recipe to yourself

## Contributors  
Dhruv Israni
Suman Plackal
Jayden Mun Wai Ng
Adrian Dimar
