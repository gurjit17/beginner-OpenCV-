import cv2
image = cv2.imread('New folder23/picture1.jpeg')

if image is None: 
    print('image is not found')
else: 
    (h, w)  = image.shape[:2]
    centre = (w//2, h//2)
    M = cv2.getRotationMatrix2D(centre, 90, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h))
    cv2.imshow('original image', image)
    cv2.imshow('rotated image', rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


















