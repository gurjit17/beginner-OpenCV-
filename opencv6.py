import cv2

image = cv2.imread('New folder23/picture1.jpeg')

if image is  None:
    print("image  not found")
else: 
    print("image  found")

    resized = cv2.resize(image, (300, 300))

    cv2.imshow('Original image', image)
    cv2.imshow('Resized image', resized)
    cv2.imwrite('resized_output.jpeg', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

