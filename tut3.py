import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    
    width = int(cap.get(3))     # get (3) is width in the 17 properties
    height = int(cap.get(4))    # get (4) is height in the 17 properties
    
    image = np.zeros(frame.shape,np.uint8)     #makes blank frame
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180) 
    image[height//2:,:width//2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180) 
    image[:height//2,width//2:] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180) 
    image[height//2:,width//2:] = smaller_frame 
    
    
    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()