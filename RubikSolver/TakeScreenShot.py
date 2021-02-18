import numpy as np
import cv2
import pyscreenshot as ImageGrab
import FilterPicture
import keyboard

#########################################
###########Video capture setting#########
#########################################
cap = cv2.VideoCapture (0)
if not cap.isOpened ():
    print ("Cannot open camera")
    exit ()

def take_picture(count_picture):
    picture = str(count_picture) + ".png"
    im = ImageGrab.grab (bbox=(72, 40, 680, 525))  # X1,Y1,X2,Y2
    im.save("Images/" + picture)

def Get_capture():
    count_picture = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is Trueq
        if not ret:
            print("Can't receive frame (stream enqqd?). Exiting ...")
            break
        cv2.namedWindow ('Original', 0)
        cv2.resizeWindow (winname='Original', width=680, height=480)
        cv2.imshow('Original', frame)
        if cv2.waitKey(1) == ord('q'):
            take_picture(count_picture)
            count_picture += 1

def Give_filter(count_analyse):
    FilterPicture.yellow_filter("Images/0.png")
    count_analyse += 1

if __name__ == "__main__":
    Get_capture()
    Give_filter(0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()