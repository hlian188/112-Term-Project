from tkinter import *
import tkinter #difference between this and first line?
import cv2
import PIL.Image, PIL.ImageTk
import math
import random
from FaceTracking import *

#TODO
# Look into doing collisions and logic purely in openCV
#write plans I want to try

#tell use to wear a mask

#code partially copied from 
#https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
class App(object):
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)
        self.faceCoordinates = (0,0,0,0)
        
        
    def run(self, width = 600, height = 600):
        
        def init(data, self):
            
            data.diameter = 100
            data.moveDown = True #down is always up or down
            data.moveRight = random.randint(-1,1) #either moving left, right or not horizontally at all
            #face coordinates
            data.x = data.width/2-data.diameter #top left ball
            data.y = 0
            
            data.speed = 5
            
            data.fx = self.faceCoordinates[0] #top left
            data.fy = self.faceCoordinates[1]
            data.fx1 = self.faceCoordinates[2] #bottom right of face rectangle
            data.fy1 = self.faceCoordinates[3]
            
            #scoring
            data.score = 0
            data.streak = 0
            data.ScoreMultiplier = 1
            
            data.camera = self.vid.vid
            #cv2.VideoCapture(0)
            data.detector = FaceDetector()
        
        def keyPressed(event, data):
            # use event.char and event.keysym
            pass
        
        def timerFired(data):
            ret, frame = data.camera.read()
            if ret:
                #cv2.imshow('Video', frame)

                coordinates = data.detector.process(frame) # Process
                self.faceCoordinates = coordinates #sometimes this can be None
                print("coordinates:", coordinates)
                
                data.fx = self.faceCoordinates[0] #top left
                data.fy = self.faceCoordinates[1]
                data.fx1 = self.faceCoordinates[2] #bottom right of face rectangle
                data.fy1 = self.faceCoordinates[3]
            # Standard display code, showing the resultant frame in a window titled
            # "Video". Close the window with 'q'.
                # cv2.imshow('Video', frame)
            else:
                coordinates = (0,0,0,0)
                print('shit')
            

            if data.moveDown:
                if data.moveRight == -1:
                    if isLegalCollisions(data.x-data.speed, data.y+data.speed): #not physically correct
                        data.x -= data.speed
                        data.y += data.speed
                
                elif data.moveRight == 0:
                    if isLegalCollisions(data.x, data.y+data.speed):
                        data.y += data.speed
                
                elif data.moveRight == 1:
                    if isLegalCollisions(data.x+data.speed, data.y+data.speed):
                        data.x += data.speed
                        data.y += data.speed
            else:
                if data.moveRight == -1:
                    if isLegalCollisions(data.x-data.speed, data.y-data.speed): #not physically correct
                        data.x -= data.speed
                        data.y -= data.speed
                elif data.moveRight == 0:
                    if isLegalCollisions(data.x, data.y-data.speed):
                        data.y -= data.speed
                elif data.moveRight == 1:
                    if isLegalCollisions(data.x+data.speed, data.y-data.speed):
                        data.x += data.speed
                        data.y -= data.speed
            
            hitBall(data)
            #this is speed
            #should we be doing this in timerFired?
            #handle logic for face detection?
        
        def isLegalCollisions(x,y):
            if not (x or y) > 0: #remember this is top left
                return False
            elif x + data.diameter > data.width:
                return False
            elif y + data.diameter > data.height:
                return False
            return True
        
        def hitBall(data):
            if data.x == data.fx1 and data.fy <= data.y <= data.fy1:
                data.x += data.speed
                data.y = 0 # for testing purposes
            elif data.fx <= data.x + data.diameter <=data.fx1 and data.y + data.diameter == data.fy:
                data.y -= data.speed
            elif data.x + data.diameter == data.fx and data.fy <= data.y + data.diameter <= data.fy1:
                data.x -= data.speed
                data.y = 0 #for testing purposes
                
            
                    
        def redrawAll(canvas, data):
            # draw in canvas
            ret, frame = self.vid.get_frame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)    
            canvas.create_oval(data.x,data.y,data.x+data.diameter,data.y+data.diameter, fill = "red")
            canvas.create_rectangle(data.fx, data.fy, data.fx1, data.fy1, outline = "green", width = "10")

        def redrawAllWrapper(canvas, data):
            canvas.delete(ALL)
            """canvas.create_rectangle(0, 0, data.width, data.height,
                                    fill='white', width=0)"""
            redrawAll(canvas, data)
            canvas.update()    
    
        def keyPressedWrapper(event, canvas, data):
            keyPressed(event, data)
            redrawAllWrapper(canvas, data)
    
        def timerFiredWrapper(canvas, data):
            timerFired(data)
            redrawAllWrapper(canvas, data)
    
            self.window.after(data.timerDelay, timerFiredWrapper, canvas,data)
        
        class Struct(object): pass
        data = Struct()
        data.width = self.vid.width
        data.height = self.vid.height
        data.timerDelay = 40
        self.delay = data.timerDelay # milliseconds
        init(data, self)
        # create the root and the canvas
        canvas = Canvas(self.window, width=self.vid.width, height=self.vid.height)
        canvas.configure(bd=0, highlightthickness=0)
        canvas.pack()

        timerFiredWrapper(canvas, data) 
        # and launch the app
        self.window.mainloop() # blocks until window is closed
        
        print("bye!")

class MyVideoCapture(object):
    def __init__(self, video_source=0):
      # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
    
            # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
        self.detector = FaceDetector()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                #Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application objec App(tkinter.Tk(), "Tkinter and OpenCV")
"""
def main():
   
    # Open a camera, allowing us to read frames. Note that the frames are BGR,
    # not RGB, since that's how OpenCV stores them. The index 0 is usually the
    # integrated webcam on your laptop. If this fails, try different indices, or
    # get a webcam.
    camera = cv2.VideoCapture(0)
    detector = FaceDetector()
    app = App(tkinter.Tk(), "Tkinter and OpenCV")
    # In every loop, we read from the camera, process the frame, and then
    # display the processed frame. The process function is where all of the
    # interesting logic happens.
    while True:
        ret, frame = camera.read()
        print(ret)
        
        coordinates = detector.process(frame) # Process
        app.faceCoordinates = coordinates
        print(coordinates)
        # Standard display code, showing the resultant frame in a window titled
        # "Video". Close the window with 'q'.
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #app.run()

    # Clean up after ourselves.
    camera.release()
    cv2.destroyAllWindows()
 """   

#main()

app = App(tkinter.Tk(), "Tkinter and OpenCV")
app.run()


            

 #TODO
    #get both windows to run concurrently # or not lol????????????/
    #pass in output of processFace to data to handle collisions
    #write collisions
    
#### testing
"""import cv2
cam = cv2.VideoCapture(0)
#detector = FaceDetector()
i = 0
while True:
    ret, frame = cam.read()
    #coordinates = detector.process(frame)
    if ret:
        cv2.imshow('Video', frame)"""
    

    
    
    

