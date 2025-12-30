import cv2            
image = cv2.imread("New folder23/picture1.jpeg")
if image is None: 
   print('image is not loaded ' ) 
else: 
   print('image loaded successfully') 
   cv2.putText(image, 'Hello Gurjit and rajveer', (50,300), 
   cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,155,255), 2)
   cv2.imshow('text on image' , image) 
   cv2.waitKey(0)
   cv2.destroyAllWindows()