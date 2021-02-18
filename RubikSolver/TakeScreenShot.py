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
    im = ImageGrab.grab (bbox=(72, 40, 680, 525))  # x1,y1,x2,y2
    im.save("Images/" + picture)

def Get_capture():
    count_picture = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
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
    FilterPicture.yellow_filter("Images/" + str(count_analyse) + ".png")
    FilterPicture.green_filter("Images/" + str(count_analyse) + ".png")
    FilterPicture.orange_filter("Images/" + str(count_analyse) + ".png")
    FilterPicture.red_filter("Images/" + str(count_analyse) + ".png")
    FilterPicture.blue_filter("Images/" + str(count_analyse) + ".png")

    count_analyse += 1
    if count_analyse == 6:
        return

def ApplyFilter(count_analyse):
    while True:
        Give_filter(count_analyse)


if __name__ == "__main__":
    Get_capture()
    if cv2.waitKey(1) == ord('a'):
        ApplyFilter(0)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()