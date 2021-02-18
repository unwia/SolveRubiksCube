import numpy as np
import cv2

from random import randint

#########################################
###########Video capture setting#########
#########################################
cap = cv2.VideoCapture(0)


def detection_color(img):
    # Convert HSV color
    imgHSV = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)

    #Filter and color for the Cube

    lower_blue = np.array ([106, 0, 87])
    upper_blue = np.array ([141, 255, 131])
    lower_red = np.array ([150, 165, 151])
    upper_red = np.array ([179, 255, 255])
    lower_green = np.array ([52, 198, 27])
    upper_green= np.array ([87, 255, 255])
    lower_yellow = np.array ([22, 106, 0])
    upper_yellow = np.array ([32, 255, 255])
    lower_orange = np.array ([0, 121, 223])
    upper_orange = np.array ([20, 254, 254])


    mask_blue = cv2.inRange (imgHSV, lower_blue, upper_blue)
    result_blue = cv2.bitwise_and (img, img, mask=mask_blue)
    mask_red = cv2.inRange (imgHSV, lower_red, upper_red)
    result_red = cv2.bitwise_and (img, img, mask=mask_red)
    mask_green = cv2.inRange (imgHSV, lower_green, upper_green)
    result_green = cv2.bitwise_and (img, img, mask=mask_green)
    mask_green = cv2.inRange (imgHSV, lower_green, upper_green)
    result_green = cv2.bitwise_and (img, img, mask=mask_green)
    mask_yellow = cv2.inRange (imgHSV, lower_yellow, upper_yellow)
    result_yellow = cv2.bitwise_and (img, img, mask=mask_yellow)
    mask_orange = cv2.inRange (imgHSV, lower_orange, upper_orange)
    result_orange = cv2.bitwise_and (img, img, mask=mask_orange)

    #Morphological transformation Dilatation
    kernal = np.ones((3,3), "uint8")

    blue = cv2.dilate(mask_blue, kernal)
    red = cv2.dilate(mask_red, kernal)
    yellow = cv2.dilate(mask_yellow, kernal)
    green = cv2.dilate(mask_green, kernal)
    orange = cv2.dilate(mask_orange, kernal)

    #Tracking color red
    (contours_red, _) = cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours_red):
        area = cv2.contourArea(contour)
        if (area > 340):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,255), 2)
            cv2.putText(img, "red", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

    #Tracking color blue
    (contours_blue, _) = cv2.findContours (blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate (contours_blue):
        area = cv2.contourArea (contour)
        if (area > 340):
            x, y, w, h = cv2.boundingRect (contour)
            img = cv2.rectangle (img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText (img, "blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    # Tracking color yellow
    (contours_yel, _) = cv2.findContours (yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate (contours_yel):
        area = cv2.contourArea(contour)
        if (area > 420):
            x, y, w, h = cv2.boundingRect (contour)
            img = cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText (img, "yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    # Tracking color green
    (contours_gre, h_) = cv2.findContours (green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate (contours_gre):
        area = cv2.contourArea (contour)
        if (area > 420):
            x, y, w, h = cv2.boundingRect (contour)
            img = cv2.rectangle (img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText (img, "green", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    # Tracking color orange
    (contours_ora, _) = cv2.findContours(orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate (contours_ora):
        area = cv2.contourArea(contour)
        if (area > 420):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "orange", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    cv2.namedWindow('Original', 0)
    cv2.resizeWindow (winname='Original', width=680, height=480)
    cv2.imshow ('Original', img)

def display_rectangle(img):
    x = 230
    y = 150
    x1 = 230
    y1 = 220
    x2 = 230
    y2 = 290

    for i in range(3):
        cv2.rectangle(img, (x,y), (x + 27, y + 27), (255,255,255), 2)
        x += 62
    for i in range(3):
        cv2.rectangle (img, (x1, y1), (x1 + 27, y1 + 27), (255, 255, 255), 2)
        x1 += 62
    for i in range (3):
        cv2.rectangle (img, (x2, y2), (x2 + 27, y2 + 27), (255, 255, 255), 2)
        x2 += 62

if __name__ == "__main__":
    while(True):
        # Capture frame-by-frame
        ret, img = cap.read()
        if img is None:
            print("Error image is None")
            exit(1)
        else:
            display_rectangle(img)
            detection_color(img)
            key = cv2.waitKey(10) & 0xFF

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
