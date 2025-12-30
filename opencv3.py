import cv2
image = cv2.imread('new folder23/picture1.jpeg')
if image is not  None: 
    success = cv2.imwrite('new folder23/saved_image.png', image)
    if success:
        print('image is saved')
    else: 
        print('failed to save')
else: 
     print('error: image is not found')