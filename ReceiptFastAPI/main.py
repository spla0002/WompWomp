import logging
import cv2
import numpy as np

from scanner import image_to_text
from recipe_finder import ingredient_extractor,recipe_maker
from emailer import email_sender

from fastapi import FastAPI, File, UploadFile,Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Create a logger
logger = logging.getLogger(__name__)

# Configure logging level
logging.basicConfig(level=logging.DEBUG)


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return JSONResponse(content={"big":"bossman"})


@app.post("/upload")
async def upload_image(image:UploadFile=File(...)):
    try:
        
        #Get contents of upload
        contents = await image.read()
        
        #Get numpy array of image
        image_array = cv2.imdecode(np.frombuffer(contents,np.uint8),cv2.IMREAD_COLOR) 

        #If image exists process it and get data 
        if image_array is not None:
            ocr_result = image_to_text(image_array)
            print(ocr_result)
        
        #OPENAI ingredient
        ingred_list = ingredient_extractor(ocr_result)
        
        #OPENAI recipe
        recipe_list = recipe_maker(ingred_list)
        
        response = {
            'status':'successful',
            'recipes':f'{recipe_list}'
        }
        
            
        return JSONResponse(content=response)
        
        
    except Exception as e:    
        return JSONResponse(content={"error":str(e)})

@app.post("/email_recipe")
async def email_recipe(email:str=Form(...),recipes:str=Form(...)):
    try:
        
        receiver = email
        subject = "Recipes"
        
        if recipes == []:
            body = "No Recipes found"
        else:
            body = recipes
        
        
        
        email_sender(receiver,subject,body)
        return {'message':'Email sent successfully'}
    except Exception as e:
        return {'error':str(e)}
        
        