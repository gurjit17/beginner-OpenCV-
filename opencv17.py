import cv2             

image = cv2.imread('New folder23/picture1.jpeg') 

blurred = cv2.medianBlur(image, 11)

cv2.imshow('original', image)
cv2.imshow('blurred image',  blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

