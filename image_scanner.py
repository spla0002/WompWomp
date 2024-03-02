import numpy as np
import cv2 
import math

import pytesseract
import PIL.Image as pImage
from pytesseract import Output
import re 


#Resize image
def resizeImage(image):
    height,width,_ = image.shape
    aspect_ratio = height/width
    new_width = 600
    new_height = math.ceil((aspect_ratio)*new_width)
    image = cv2.resize(image,(new_width,new_height),interpolation=cv2.INTER_CUBIC)

    return image


#Resize image
def resizeImageHalf(image):
    height,width,_ = image.shape
    aspect_ratio = height/width
    new_width = 2000
    new_height = math.ceil((aspect_ratio)*new_width)
    image = cv2.resize(image,(new_width,new_height),interpolation=cv2.INTER_CUBIC)

    return image



def remove_shadows(img):
    rgb_planes = cv2.split(img)

    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((3,3), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 45)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=1.6, beta=200, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        _,thresh_img = cv2.threshold(norm_img,0,255,cv2.THRESH_BINARY)

        result_planes.append(diff_img)
        result_norm_planes.append(thresh_img)

    

    image= cv2.merge(result_planes)

    return image

def image_to_text(image_path):
    myconfig = r"--psm 11 --oem 1"

    img = cv2.imread(image_path)
    img = resizeImageHalf(img)
    img = remove_shadows(img)

    data = pytesseract.image_to_data(img,config=myconfig,output_type=Output.DICT)
    amount_boxes = len(data['text'])

    #Draw boxes around each peice of text
    for i in range(amount_boxes):
        if float(data['conf'][i])>50:
            (x,y,w,h) = (data['left'][i],data['top'][i],data['width'][i],data['height'][i])
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            img = cv2.putText(img,data['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2,cv2.LINE_AA)

    text = data['text']

    #Filter text to remove floats, ints, and symbols
    def filter_products(x:list):
        data = []
        symbol_pattern = r'[^a-zA-Z0-9\s]'
        for item in x:
            stripped_text = re.sub(symbol_pattern,'',item)
            if item != '' and len(item)>=4 and len(item)<15:
                try:
                    int_value = int(stripped_text)
                    float_vlaue = float(stripped_text)
                    pass
                except ValueError:
                    data.append(stripped_text)
            else:
                pass
        return data

    text = filter_products(text)
    print(text)
            
    cv2.imshow('img',img)
    cv2.waitKey(0)
    return text


