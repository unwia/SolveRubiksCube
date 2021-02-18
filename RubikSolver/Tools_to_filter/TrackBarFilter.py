import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('HSV')
cv2.resizeWindow("HSV", 600, 600)
cv2.createTrackbar("HUE min", "HSV", 0,179,nothing)
cv2.createTrackbar("HUE max", "HSV", 179,179,nothing)
cv2.createTrackbar("SAT min", "HSV", 0,255,nothing)
cv2.createTrackbar("SAT max", "HSV", 255,255,nothing)
cv2.createTrackbar("V min", "HSV", 0,255,nothing)
cv2.createTrackbar("V max", "HSV", 255,255,nothing)

while(True):

    ret, img = cap.read()
    if img is None:
        print("Error image is None")
        exit(1)
    else:
        imgHSV = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)

        hmin = cv2.getTrackbarPos("HUE min", "HSV")
        hmax = cv2.getTrackbarPos ("HUE max", "HSV")
        smin = cv2.getTrackbarPos ("SAT min", "HSV")
        smax = cv2.getTrackbarPos ("SAT max", "HSV")
        vmin = cv2.getTrackbarPos ("V min", "HSV")
        vmax = cv2.getTrackbarPos ("V max", "HSV")

        lower = np.array([hmin, smin, vmin])
        upper = np.array([hmax, smax, vmax])
        mask = cv2.inRange(imgHSV,lower,upper)
        result = cv2.bitwise_and(img,img, mask= mask)


        cv2.imshow('Original', img)
        cv2.imshow('resulr', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
