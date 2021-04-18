import cv2

img= cv2.imread('assets\\sandy.png',1)

# 0 is greyscale
# -1 color image
# 1 color image including alpha channel

img= cv2.resize(img,(400,400))
# img= cv2.resize(img,(0,0),fx=1,fy=30)

img = cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) 
cv2.imwrite('assets/modifiedsandy.png',img)


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()