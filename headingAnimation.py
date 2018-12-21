import time
import sys
from tkinter import *
import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk
#from HeadingMinigame import *
from FaceTracking import *
import random
from boostsAnimation import boostsInit

def headInit(data):
    camera = cv2.VideoCapture(0)
    data.camera = camera
    data.faceDetector = FaceDetector()
    data.faceCoor = (0,0,0,0)
    data.tmpFaceCoor = (0,0,0,0)
    #data.faceTopLeft = (0,0)
    data.helpBoxSize = 50
    
    data.radius = 60
    data.cx = data.width/2
    data.cy = 0
    
    #scoring
    data.headTime = 0
    data.headScore = 0
    data.headCount = 0
    data.headMultiplier = 1
    
    data.target = 10000
    
    #movement
    data.direction = [0, 1]
    data.headSpeed = 10
    data.xSpeed = random.randint(10,30)
    
    data.moveUp = False
    data.gameOver = False
    

def opencvToTk(frame): #DO NOT MODIFY THIS FUNCTION OTHERWISE RENAME FUNCTION B/C THIS EXISTS IN JUGGLING MINIGAME!
    """Convert an opencv image to a tkinter image, to display in canvas."""
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_image) #img is 640 x 480
    
    #pil_img = pil_img.resize((600,600), Image.ANTIALIAS) #resize
    tk_image = ImageTk.PhotoImage(image=pil_img)
    return tk_image
    
def headMousePressed(event, data):
    pass

def headKeyPressed(event, data):
    if event.keysym == "q":
        data.root.destroy()
    pass

def headTimerFired(data):
    if not data.gameOver:
        data.headTime += 1
        ret, frame = data.camera.read()
        if ret:
            data.faceCoor = data.faceDetector.process(frame) #gives topleft and bottom right coordinates of face
            if data.faceCoor != (0,0,0,0): #stores tmoFaceCoor which is displayed
                data.tmpFaceCoor = (data.faceCoor[0]+data.width/2-320, data.faceCoor[1]+data.height/2-240, \
                data.faceCoor[2]+data.width/2-320, data.faceCoor[3]+data.height/2-240)
    
            print(data.faceCoor)
        
        #reactToWallHit(data)
        
        
        #if data.headTim == 0:
        if data.moveUp:
            data.cy -= data.headSpeed
            
        elif isLegalHeadCollisions(data, data.xSpeed*data.direction[0], data.headSpeed*data.direction[1]):
            data.cx += data.xSpeed*data.direction[0]
            
            data.direction[1] *= -1
            data.cy += data.headSpeed*data.direction[1]
            data.moveUp = True
            
        else:
            #data.direction[1] = 1
            data.cy += data.headSpeed*data.direction[1]
        
        if data.cy >= data.height:
            data.gameOver = True
            
        reactToWallHit(data)
    else:
        boostsInit(data)
        data.mode = "boosts"
          
def isLegalHeadCollisions(data, dx, dy):
    if data.tmpFaceCoor[0] <= data.cx+dx<= data.tmpFaceCoor[2] \
    and data.cy+dy+data.radius >= data.tmpFaceCoor[1]:
        return True
    
    
    return False

    
def reactToWallHit(data): 
    # if not (data.radius < data.cx) or not (data.cx < data.width - data.radius):
    #     data.direction[0] *= -1
    if data.cy < 0:
        data.direction[1] = 1
        data.cy += data.headSpeed*data.direction[1]
        data.moveUp = False
    
    


def drawCamera(canvas, data):
    data.tk_image = opencvToTk(data.frame)
    
    canvas.create_image(data.width/2, data.height/2, image=data.tk_image)


def headRedrawAll(canvas, data):
    drawCamera(canvas, data)
    
    #canvas.create_text(800,50, text = "hello?")
    
    canvas.create_rectangle(data.tmpFaceCoor, outline = "red")
    
    canvas.create_rectangle(data.width/10, data.height/10, data.width/10+data.helpBoxSize, data.height/10+data.helpBoxSize, outline = "green")
    
    canvas.create_text(data.width/10, data.height/10, text = "Score %d points!" %data.target)
    canvas.create_text(data.width*9/10, data.height*9/10, text = "Current score: %d" %data.headScore)
    
    canvas.create_oval(data.cx-data.radius, data.cy-data.radius, data.cx+data.radius, data.cy+data.radius, fill = "red")