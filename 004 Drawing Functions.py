import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), np.uint8) # black background image as template 

# cv.line ( < image > , < starting point > , < ending point > , < colour > , < thickness > ) 
cv.line(img,(0,0),(511,511),(255,0,0),5) 

# cv.rectangle ( < image > , < starting point > , < ending point > , < colour > , < thickness > )
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# cv.circle ( < image > , < center coordinates > , < radius > , < colour > , < fill / no fill > )
cv.circle(img,(447,63), 63, (0,0,255), 1) # 1 is empty , -1 is solid 

# cv.ellipse ( < image > , < center x location > , < center y location > , < major axis length > , < minor axis length > , < start angle > , < end angle > , < fill / no fill > )
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

# displaying the image
cv.imshow ('Template' , img )
k = cv.waitKey(0)
if k == ord('s') : # "S" to save drawing
    cv.imwrite ('999 Drawing.jpg' , img)
