import cv2
import random

img= cv2.imread('assets\\sandy.png',-1)

# for i in range(0,100):
#     for j in range(img.shape[1]):
#         img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        

tag =img[50:70,60:90]
img[10:30,65:95]=tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()