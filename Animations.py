from tkinter import *
from GameLogic import *
import random
from playAnimation import *
from startAnimation import *
from jugglingAnimation import * #were pretty much gucci here
from headingAnimation import *
from subsAnimation import *
from boostsAnimation import *
import cv2
import time

def init(data):
    data.mode = "start" #start, play, substitutions
    startInit(data)
    playInit(data)
    #headInit(data)

def mousePressed(event, data):
    if (data.mode == "start"): startMousePressed(event, data) #start takes pic of yourself (you can only take once!)
    elif (data.mode == "play"):   playMousePressed(event, data)
    elif data.mode == "mainMenu": mainMenuMousePressed(event, data) 
    elif (data.mode == "head"): headMousePressed(event, data) #heading minigame
    elif (data.mode == "juggling"): jugglingMousePressed(event, data) #juggling minigame
    elif data.mode == "subs": subsMousePressed(event, data)
    elif data.mode == "boosts": boostsMousePressed(event, data)
    #have boost mode where it tells whose players stats of been enhanced

def keyPressed(event, data):
    if (data.mode == "start"): startKeyPressed(event, data)
    elif (data.mode == "play"):   playKeyPressed(event, data)
    elif (data.mode == "mainMenu"):   mainMenuKeyPressed(event, data)
    elif (data.mode == "head"):   headKeyPressed(event, data)
    elif data.mode == "juggling": jugglingKeyPressed(event, data)
    elif data.mode == "subs": subsKeyPressed(event, data)
    elif data.mode == "boosts": boostsKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "start"): startTimerFired(data)
    elif (data.mode == "play"):   playTimerFired(data)
    elif (data.mode == "mainMenu"):   mainMenuTimerFired(data)
    elif (data.mode == "head"):   headTimerFired(data)
    elif data.mode == "juggling": jugglingTimerFired(data)
    elif data.mode == "subs": subsTimerFired(data)
    elif data.mode == "boosts": boostsTimerFired(data)
        

def redrawAll(canvas, data):
    if (data.mode == "start"): startRedrawAll(canvas, data)
    elif (data.mode == "play"):   playRedrawAll(canvas, data)
    elif (data.mode == "mainMenu"):   mainMenuRedrawAll(canvas, data)
    elif (data.mode == "head"):   headRedrawAll(canvas, data)
    elif data.mode == "juggling": jugglingRedrawAll(canvas, data)
    elif data.mode == "subs": subsRedrawAll(canvas, data)
    elif data.mode == "boosts": boostsRedrawAll(canvas, data)
        
    
#################################################################
# use the run function as-is
#################################################################


def run(width=300, height=300):
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.camera_index = 0

    data.timer_delay = 30 # ms
    data.redraw_delay = 30 # ms
    
    # Initialize the webcams
    camera = cv2.VideoCapture(data.camera_index)
    #data.camera = camera

    # Make tkinter window and canvas
    root = Tk() #maybe change data.root to root?
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # Basic bindings. Note that only timer events will redraw.
    root.bind("<Button-1>", lambda event: mousePressed(event, data))
    root.bind("<Key>", lambda event: keyPressed(event, data))

    # Timer fired needs a wrapper. This is for periodic events.
    def timerFiredWrapper(data):
        # Ensuring that the code runs at roughly the right periodicity
        start = time.time()
        timerFired(data)
        end = time.time()
        diff_ms = (end - start) * 1000
        delay = int(max(data.timer_delay - diff_ms, 0))
        root.after(delay, lambda: timerFiredWrapper(data))

    # Wait a timer delay before beginning, to allow everything else to
    # initialize first.
    root.after(data.timer_delay, 
        lambda: timerFiredWrapper(data))

    def redrawAllWrapper(canvas, data):
        start = time.time()
        # Get the camera frame and get it processed.
        try:
            _, data.frame = data.camera.read() #only does this if data.camera is defined (only when minigames are called)
        except:
            #print("can't read frame")
            pass

        # Redrawing code
        canvas.delete(ALL)
        redrawAll(canvas, data)

        # Calculate delay accordingly
        end = time.time()
        diff_ms = (end - start) * 1000

        # Have at least a 5ms delay between redraw. Ideally higher is better.
        delay = int(max(data.redraw_delay - diff_ms, 5))
        
        delay = 30 #this helps for some reason

        root.after(delay, lambda: redrawAllWrapper(canvas, data))

    # Start drawing immediately
    root.after(0, lambda: redrawAllWrapper(canvas, data))

    # Loop tkinter
   
    root.mainloop()

    # Once the loop is done, release the camera.
    print("Releasing camera!")
    try:
        data.camera.release()
    except:
        print("No camera!")
run(1244, 700) #originally 1244 x 700

