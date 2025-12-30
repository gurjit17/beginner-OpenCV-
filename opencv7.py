import cv2
image = cv2.imread('New folder23/picture1.jpeg')

if image is not None:
    cropped = image[500:800, 400:800]
    cv2.imshow('original image' , image)
    cv2.imshow('Cropped image' , cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




