import cv2  #check the opencv library 


image = cv2.imread("New folder23/picture1.jpeg")

if image is not None:
    cv2.imshow('Image showing', image) #open the window
    cv2.waitKey(0) #wait for a key
    cv2.destroyAllWindows() #close the window 
    print('Error:Image  found.')
else:
    print('image not loaded sucessfully')