
from tkinter import *
import tkinter as tk
import numpy as np
import cv2
import random
from startAnimation import *
import copy

def boostsInit(data):
    data.tmpBoostList = []
    for player in data.Liverpool.playerList:
        if not isinstance(player, GoalKeeper):
            data.tmpBoostList.append(player)
            
    data.playerBoost = random.choice(data.tmpBoostList) #chooses player to boost
    
    att = random.randint(0,5)
    data.attributeName = data.playerBoost.boostStats[att]
    data.attribute = data.playerBoost.stats[att]

    
def boostsMousePressed(event, data):
    pass

def boostsKeyPressed(event, data):
    if event.keysym == "q":
        data.root.destroy()
    elif event.keysym == "s":
        data.mode = "start"

def boostsTimerFired(data):
    pass



def boostsRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2, text = "%s %s has increased!" % (data.playerBoost.name, data.attributeName), font = "Arial 60")
    canvas.create_text(data.width/2, data.height/4, text = "Press s to continue!", font = "Arial 24")