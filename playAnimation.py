from tkinter import *
from GameLogic import *
import random
import copy
### play animation logic
#mouse doesn't do anything
def startingGameInit(data): #even after scoring
    #you always play as liverpool 
    
    teams = random.choice([[BarcelonaInitBall(), LiverpoolInitNoBall()], [BarcelonaInitNoBall(), LiverpoolInitBall()]])
    
    data.Barcelona = teams[0] 
    data.Liverpool = teams[1]
    

    
def playInit(data):
    data.path = "Images/SoccerField.gif"
    data.image = PhotoImage(file = data.path)
    
    startingGameInit(data)
    data.LScore = 0
    data.BScore = 0
    
    #ball parameters
    data.radius = 10
    data.x = data.width/2 - data.radius #topleft 
    data.y = data.height/2 - data.radius
    data.x1 = data.x + 2*data.radius
    data.y1 = data.y + 2*data.radius
    data.ball = [(data.x,data.y), (data.x1,data.y1), data.radius]
    
    data.gameTime = 0
    
    #ball movement logic
    data.displacement = None
    data.originalDisplacement = None
    data.passSpeed = 30
    data.ballMoving = False #only true if ball is shot or passed
    
    data.passableBarcelonaList = copy.copy(data.Barcelona.playerList)
    data.passableLiverpoolList = copy.copy(data.Liverpool.playerList)
    
    data.LScored = False
    data.Bscored = False
    
    data.playerImagesB = [] #[PhotoImage, player, type(player)]
    data.playerImagesL = []

    for player in data.Barcelona.playerList:
        path = player.image
        data.playerImagesB.append([PhotoImage(file = path, width = 50, height = 50), player, type(player)])
        
    for player in data.Liverpool.playerList:
        path = player.image
        data.playerImagesL.append([PhotoImage(file = path, width = 50, height = 50), player, type(player)])
    

def playMousePressed(event, data):
    pass

def playKeyPressed(event, data):
    if event.keysym == "s":
        data.mode = "subs"
    



def ballHit(data, player):
    pass


#game logic   
def movePlayers(data):
    for player in data.Barcelona.playerList:
        if not isinstance(player, GoalKeeper): #everyone moves but goalkeeper
            coor = (random.randint(-8, 10), random.randint(-10,10))
            
            if inBounds(data, player, coor) and notHittingAnotherPlayer(data, player, coor):
                player.location = (player.location[0] + coor[0], player.location[1] + coor[1])
    
    for player in data.Liverpool.playerList:
        if not isinstance(player, GoalKeeper):
            coor = (random.randint(-10, 8), random.randint(-10,10))
            if inBounds(data, player, coor) and notHittingAnotherPlayer(data, player, coor):
                player.location = (player.location[0] + coor[0], player.location[1] + coor[1])   
def playTimerFired(data):
    #movement
    data.gameTime += 1
    if data.gameTime % 5 == 0:
        movePlayers(data)
        
        #passing/interceptions/shooting logic
        if data.Barcelona.hasBall():
            for player in data.Barcelona.playerList:
                if player.hasBall:
                    x = random.randint(1,100)
                    print(x)
                    if x<=50: #pass x% of the time
                        teammate = random.choice(data.Barcelona.playerList)
                        if teammate == player: break
 
                        player.passBall(teammate, data) #either passes or makes mistake    
                    else:
                        for opponent in data.Liverpool.playerList:
                            if isinstance(opponent, GoalKeeper):
                                goalkeeper = opponent
                                break
                        isGoal = player.score(goalkeeper)
                        if isGoal:
                            data.BScore += 1
                        #determine dribble in space
                        #determine shoot
                        
                        
        elif data.Liverpool.hasBall():
            for player in data.Liverpool.playerList:
                if player.hasBall:
                    x = random.randint(1,100)
                    if x<=50:
                        teammate = random.choice(data.Liverpool.playerList)
                        if teammate == player: break
                        player.passBall(teammate, data) #either passes or makes mistake
                    else:
                        for opponent in data.Barcelona.playerList:
                            if isinstance(opponent, GoalKeeper):
                                goalkeeper = opponent
                                break
                        isGoal = player.score(goalkeeper)
                        if isGoal:
                            data.LScore += 1
                        #determine dribble in space
                        #determine shoot
          
        
        
        
        
        
        #moves ball
        if data.ballMoving:
            data.ball[0] = (data.ball[0][0]+data.passSpeed*data.displacement[0], data.ball[0][1]+data.passSpeed*data.displacement[1])
            data.ball[1] = (data.ball[1][0]+data.passSpeed*data.displacement[0], data.ball[1][1]+data.passSpeed*data.displacement[1])
            
        
        #receiving ball logic
        for player in data.passableBarcelonaList: 
            if data.ballMoving:
                if player.getPossession(data):
                    data.passableBarcelonaList = data.Barcelona.playerList
                    break

        for player in data.passableLiverpoolList:
            if data.ballMoving:
                if player.getPossession(data):
                    data.passableLiverpoolList = data.Liverpool.playerList
                    break
                
                
            

def canDribble(data): #will determine if player will dribble
    pass

def inBounds(data, player, coor):
    if not 0 <= player.location[0] + coor[0] <= data.width-50:
        return False
    if not 0 <= player.location[1] + coor[1] <= data.height-50:
        return False
    return True


    
def notHittingAnotherPlayer(data, player, coor):
    tempLiverpoolList = copy.copy(data.Liverpool.playerList)
    tempBarcelonaList = copy.copy(data.Barcelona.playerList)
    
    try:
        tempLiverpoolList.remove(player)
    except: pass
    
    try:
        tempBarcelonaList.remove(player)
    except: pass
    
    for other in (tempLiverpoolList+tempBarcelonaList):
        if distance(player.location[0]+25+coor[0], player.location[1]+25+coor[1], other.location[0]+25, other.location[1]+25) <= 40: #orginally 71
            return False
    return True

def notOffside(data, player, coor): #can significantly impact logic, do last
    pass
        

def playRedrawAll(canvas, data):
    canvas.create_image(0,0, anchor = NW, image=data.image)
    if not data.ballMoving:
        for img_coor in data.playerImagesB:
            canvas.create_image(img_coor[1].location, anchor = NW, image = img_coor[0])
            if img_coor[1].hasBall:
                lcoor = img_coor[1].location
                data.ball[0] = (lcoor[0]+50, lcoor[1]+15)
                data.ball[1] = (data.ball[0][0] + 2*data.radius, data.ball[0][1] + 2*data.radius)
                
                canvas.create_oval(data.ball[0], data.ball[1], fill = "red")
                
    
        for img_coor in data.playerImagesL:
            canvas.create_image(img_coor[1].location, anchor = NW, image = img_coor[0])
            if img_coor[1].hasBall:
                lcoor = img_coor[1].location
                data.ball[0] = (lcoor[0]-20, lcoor[1]+15)
                data.ball[1] = (data.ball[0][0] + 2*data.radius, data.ball[0][1] + 2*data.radius)
                
                canvas.create_oval(data.ball[0], data.ball[1], fill = "red") #
    
    if data.ballMoving:
        for img_coor in data.playerImagesB:
            canvas.create_image(img_coor[1].location, anchor = NW, image = img_coor[0])
            
                
    
        for img_coor in data.playerImagesL:
            canvas.create_image(img_coor[1].location, anchor = NW, image = img_coor[0])
            
        canvas.create_oval(data.ball[0], data.ball[1], fill = "red")
        
            
    
    canvas.create_text(data.width/2, 20, text = "Barcelona %d: Liverpool %d" %(data.BScore, data.LScore), font = "Arial 24")