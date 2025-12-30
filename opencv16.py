import cv2      
image = cv2.imread('New folder23/picture1.jpeg')
blurred = cv2.GaussianBlur(image, (15,15), 3)

cv2.imshow('Original Image', image)
cv2.imshow('blurred Image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()