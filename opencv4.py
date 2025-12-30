import cv2
image = cv2.imread('new folder23/picture1.jpeg')

if image is not None:
    h, w, c = image.shape 
    print(f'image loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}')
else: 
    print('could not load')