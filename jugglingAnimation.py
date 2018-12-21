#from Animations import *
import time
import sys
from tkinter import *
import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk
from JugglingMinigame import *
from FaceTracking import *

def jugglingInit(data):
    # Initialize the webcams
    camera = cv2.VideoCapture(0)
    data.camera = camera
    data.ballDetector = BallDetector()
    data.center = (0,0,0)
    
    
    data.jugglingScore = 0
    
    data.initialCenter = (0,0,0)
    data.jugglingTimer = 0
    
def opencvToTk(frame):
    """Convert an opencv image to a tkinter image, to display in canvas."""
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_image) #img is 640 x 480
    
    #pil_img = pil_img.resize((600,600), Image.ANTIALIAS) #resize
    tk_image = ImageTk.PhotoImage(image=pil_img)
    return tk_image


def jugglingMousePressed(event, data):
    pass


def jugglingKeyPressed(event, data):
    if event.keysym == "q":
        data.root.destroy()
    pass


def jugglingTimerFired(data):
    data.jugglingTimer += 1
    ret, frame = data.camera.read()
    if ret:
        center = data.ballDetector.getBallCenter(frame)
        data.center = center
        
        print(data.center)
    
        if data.jugglingTimer <= 100: #wait 3 seconds
            if data.center != (0,0,0):
                data.initialCenter = data.center
    
            
        

def drawCamera(canvas, data):
    data.tk_image = opencvToTk(data.frame)
    print("here")
    canvas.create_image(data.width/2, data.height/2, image=data.tk_image)


def jugglingRedrawAll(canvas, data):
    drawCamera(canvas, data)
    
    #canvas.create_text(800,50, text = "hello?")
    radius = data.center[2]
    canvas.create_oval(data.center[0]-radius+data.width/2-320, data.center[1]-radius+data.height/2-240, data.center[0]+radius+data.width/2-320, data.center[1]+radius+data.height/2-240, outline = "red", width = 10)
    
    radius = data.initialCenter[2]
    canvas.create_line(0, data.initialCenter[1]+data.height/2-240, data.width, data.initialCenter[1]+data.height/2-240) #bottom threshold
    
    canvas.create_line(0, data.initialCenter[1]+data.height/2-200, data.width, data.initialCenter[1]+data.height/2-200)
