from tkinter import *
from GameLogic import *
import random
import copy
from Players import *
### play animation logic
#mouse doesn't do anything
###how should I handle this logic?
def subsInit(data):
    data.tactics = []
    data.subs = {} #set of substitutes
    data.activePlayers = [] #always draws activePlayers
    pass
def subsMousePressed(event, data):
    pass

def subsKeyPressed(event, data):
    
    pass

#game logic        
def subsTimerFired(data):
    pass
   


def subsRedrawAll(canvas, data):
    canvas.create_image(0,0, anchor = NW, image=data.image)
    
    canvas.create_rectangle(0,data.height*8/10, data.width, data.height, fill = "dark blue")

    for img_coor in data.playerImagesL:
        canvas.create_image(img_coor[1].subLocation, anchor = NW, image = img_coor[0])
        if img_coor[1].hasBall:
            lcoor = img_coor[1].subLocation
            data.ball[0] = (lcoor[0]-20, lcoor[1]+15)
            data.ball[1] = (data.ball[0][0] + 2*data.radius, data.ball[0][1] + 2*data.radius)
            
            canvas.create_oval(data.ball[0], data.ball[1], fill = "red") #
            
    
    canvas.create_text(data.width/2, 20, text = "Barcelona %d: Liverpool %d" %(data.BScore, data.LScore), font = "Arial 24")