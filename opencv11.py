import cv2               
image = cv2.imread('New folder23/picture1.jpeg')

if image is None:
    print('image is loaded failed')
else:
    print(' image is loaded suceessfully') 
    pt1 = (100, 100)
    pt2 = (500,500)

    color = (0,0,255)
    thickness = 15 
    cv2.rectangle(image, pt1 , pt2 , color, thickness)
    cv2.imshow('rectanle drawing', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
