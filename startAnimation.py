from tkinter import *
from jugglingAnimation import *
from playAnimation import *
from headingAnimation import *
### start animation logic
def startInit(data):
    data.boxSize = 125
def startMousePressed(event, data):
    # use event.x and event.y
    if data.width/2-data.boxSize <= event.x <= data.width/2+data.boxSize and \
    data.height/2-data.boxSize <= event.y <= data.height/2+data.boxSize:
        playInit(data)
        data.mode = "play"
        
    
    elif data.width/4-data.boxSize <= event.x <= data.width/4+data.boxSize and \
    data.height/4-data.boxSize <= event.y <= data.height/4+data.boxSize:
        data.mode = "juggling"
        jugglingInit(data)
    
    elif data.width*3/4 - data.boxSize <= event.x <= data.width*3/4+data.boxSize and \
    data.height*3/4 - data.boxSize <= event.y <= data.height*3/4+data.boxSize:
        data.mode = "head"
        headInit(data)
def startKeyPressed(event, data):
    # use event.char and event.keysym
    pass

def startTimerFired(data):
    pass

def startRedrawAll(canvas, data):
    # draw in canvas
    
    canvas.create_rectangle(data.width/2-data.boxSize, data.height/2-data.boxSize, data.width/2+data.boxSize, data.height/2+data.boxSize, width = 4)
    canvas.create_text(data.width/2, data.height/2, text = "Play Match!", font = "Arial 36")
    
    canvas.create_rectangle(data.width/4-data.boxSize, data.height/4-data.boxSize, data.width/4+data.boxSize, data.height/4+data.boxSize, width = 4)
    canvas.create_text(data.width/4, data.height/4, text = "Juggle!", font = "Arial 36")
    
    
    canvas.create_rectangle(3*data.width/4-data.boxSize, data.height*3/4-data.boxSize, data.width*3/4+data.boxSize, data.height*3/4+data.boxSize, width = 4)
    canvas.create_text(data.width*3/4, data.height*3/4, text = "Head!", font = "Arial 36")