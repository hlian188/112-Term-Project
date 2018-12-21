# track starting position (bottom tip will be coordinates), then ball up and down movement, if 
# coordinates fall below certain threshold, then game ends

# might mess up if ball is different color or patterned


# list of times and update every certain number of time
# import the necessary packages

# Heavily inspired by https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

###

#press a key to confirm that it's calibrated, then we start the game

#yay

from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

class BallDetector(object):
    
    def __init__(self):
        self.score = 0
        self.streak = 0
        
    # construct the argument parse and parse the arguments
        self.ap = argparse.ArgumentParser()
        self.ap.add_argument("-v", "--video", help="path to the (optional) video file")
        self.ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
        self.args = vars(self.ap.parse_args())
            
        # define the lower and upper boundaries of the "green"
        # ball in the HSV color space, then initialize the
        # list of tracked points
        self.greenLower = (29, 86, 6)
        self.greenUpper = (64, 255, 255)
        
        self.pts = deque(maxlen=self.args["buffer"])

    def getBallCenter(self, frame):
        
        x = 0
        y= 0
        radius = 0
        
        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, self.greenLower, self.greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        center = None
    
    # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
        # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                    (0, 255, 255), 2)
                #print("test:", int(x), int(y), int(radius))
                
                x = int(x)
                y = int(y)
                radius = int(radius)
                #cv2.circle(frame, center, 5, (0, 0, 255), -1)
    
    # update the points queue
        self.pts.appendleft(center)

        return x, y, radius
    
    # close all windows
    



def main():
    cam = cv2.VideoCapture(0)
    ball = BallDetector()
    
    # allow the camera or video file to warm up
    time.sleep(2.0)

    # keep looping
    x = 0
    y = 0
    radius = 0
    while True:
        ret, frame = cam.read()
        frame = frame[1] if ball.args.get("video", False) else frame
        
        if frame is None:
            break
        
        cv2.imshow("Frame", frame)
        x1, y1, radius1 = ball.getBallCenter(frame)
        
        # show the frame to our screen
        
        key = cv2.waitKey(1) & 0xFF
        
        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break 
    cam.release()
    cv2.destroyAllWindows()
    
#main()