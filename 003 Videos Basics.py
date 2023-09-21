import cv2 as cv
import sys

def readfromfile() :
    video = cv.VideoCapture('999 yume nikki.mp4') # video capture object 

    if not video.isOpened():
        sys.exit('Error : Could not read video')

    cv.namedWindow('Video', cv.WINDOW_NORMAL) # Create the Video Window  

    while True:
        frame_read , frame = video.read() # read frame -> frame_read is boolean value which checks if each frame detected

        if not frame_read:
            print("Error: Could not read frame.")
            break

        cv.imshow('Video', frame) # display the frame 

        if cv.waitKey(1) & 0xFF == ord('q'): # q to quit loop
            break

    video.release() # Video Camera
    cv.destroyAllWindows()

def readfromcamera() :
    camera = cv.VideoCapture(0) # video capture object , 0 is default camera .

    if not camera.isOpened():
        sys.exit('Error : Could not open camera')

    cv.namedWindow('Camera Feed', cv.WINDOW_NORMAL) # Create the Camera Window  

    while True:
        frame_read , frame = camera.read() # read frame -> frame_read is boolean value which checks if each frame detected

        if not frame_read:
            print("Error: Could not read frame or any further frames.")
            break

        cv.imshow('Camera Feed', frame) # display the frame 

        if cv.waitKey(1) & 0xFF == ord('q'): # q to quit loop
            break

    camera.release() # Release Camera
    cv.destroyAllWindows()

typeofvideo = int (input('1 for Camera and 2 For Video from File : '))
if typeofvideo ==  1 :
    readfromcamera() 
elif typeofvideo == 2 :
    readfromfile()
else :
    sys.exit('Invalid Input')





