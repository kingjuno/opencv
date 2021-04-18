import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    
    width = int(cap.get(3))     # get (3) is width in the 17 properties
    height = int(cap.get(4))    # get (4) is height in the 17 properties
    
    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10)   
    img = cv2.line(frame,(0,height),(width,0),(255,0,255),10)
    img = cv2.rectangle(img,(10,10),(width-10,height-10),(0,0,0),5,-1)
    img = cv2.circle(img,(300,300),60,(0,0,255),-1)
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    img = cv2.putText(img,"Juno is testing",(360,360),font,4,(0,255,0),2,cv2.LINE_AA)
    
    
    
    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()