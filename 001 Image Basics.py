import cv2 as cv
import sys

img = cv.imread ('999 Sunflower1.jpg') # Reading 
image = cv.resize (img, (702,777)) # Resizing

if image is None :
    sys.exit ('Image could not be loaded')
else :
    cv.imshow ('Sunflower' , image )
    key_press = cv.waitKey(0) # Displays image until key is pressed
    if key_press == ord('s') :
        cv.imwrite ('Sunflower_Duplicate.jpg', image) # Saving if "S" key pressed
