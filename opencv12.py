import cv2              
image = cv2.imread('New folder23/picture1.jpeg') 
if image is None:
    print('image is loaded failed')
else: 
    print(' image is loaded successfully') 
    cv2.circle(image, (450,450) , 500, (0,255,0), -1)
    cv2.imshow('circle drawing', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
