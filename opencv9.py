import cv2

image = cv2.imread('New folder23/picture1.jpeg')

if image is None:
    print('image loaded failed')
else:
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow('original image', image )
    cv2.imshow('flipped horizontal', flipped_horizontal)
    cv2.imshow('flipped vertical', flipped_vertical)
    cv2.imshow('flipped both' , flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()