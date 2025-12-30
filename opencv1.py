#check the file path and import library in python 
import cv2  #check the opencv library 


image = cv2.imread("New folder23/picture1.jpeg")

if image is not None:
    print('Error:Image not found.')
else:
    print('image loaded sucessfully')
