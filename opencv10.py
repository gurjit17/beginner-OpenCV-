import cv2      
image = cv2.imread('New folder23/picture1.jpeg') 
if image is None:
  print('image loaded failed')
else:
  print('image loaded sucessfully')
pt1 = (100,100)
pt2 = (500,400)
color =(255, 0, 0)
thickness = 10
cv2.line(image , pt1, pt2 , color, thickness)
cv2.imshow('line drawing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



















































