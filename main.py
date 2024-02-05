import cv2
import numpy as np

#reads img file in full color
video = cv2.VideoCapture('circle.MOV')

#processes video by converting to grayscale and blurs 3x3
def image_processing(video):
    ret, frame = video.read()
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurring_img = cv2.blur(grayscale_img, (3, 3))

    #detects what is considered a circle
    found_circle = cv2.HoughCircles(blurring_img, cv2.HOUGH_GRADIENT, dp = 1, minDist = 9999, param1 = 60, param2 = 30, minRadius = 40, maxRadius = 500)

    #if circle found, rounds midpoint x and y coords and radius
    rounding = np.around(found_circle)
    found_circle = np.uint16(rounding)

    #for every row(circle) the circle detector finds, it assigns the 1st element as x coord, 2nd element as y coord, and 3rd element as radius
    for single_circle in found_circle[0, :]:
        x_center = single_circle[0]
        y_center = single_circle[1]
        radius = single_circle[2]

        #draws the circle and midpoint on the image
        cv2.circle(frame, center = (x_center, y_center), radius = 3, color = (240, 207, 137), thickness = 5)
        cv2.circle(frame, center = (x_center, y_center), radius = radius, color = (193, 182, 255), thickness = 6)

    cv2.imshow('Circle', frame)
    cv2.waitKey(15)

while True:
    image_processing(video)

video.release()
cv2.destroyAllWindows()
