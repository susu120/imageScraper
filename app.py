import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

def imageScraper():
    #config of pytesseract
    myconfig = r'--psm 6 --oem 3' 
    
    #converting the image to string, saving it in result.txt
    text = pytesseract.image_to_string(PIL.Image.open('test.png'), config=myconfig)
    filename = open('result.txt', 'w+')
    print(text)
    print(text, file=filename)
    
    #reading image with cv2 and converting image to data
    img = cv2.imread('test.png')
    data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)
    
    amount_boxes = len(data['text'])
    
    #looping through the words to draw boxes around the words
    for i in range(amount_boxes):
        if float(data['conf'][i]) > 80:
            (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            img = cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)
    
    #displaying the image
    cv2.imshow('img', img)
    cv2.waitKey(0)
    
def pdfScraper():
    print('hello')


imageScraper()