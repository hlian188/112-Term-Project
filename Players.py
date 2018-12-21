import random

#stats = [pace, dribbling, shooting, passing, physical, defense]
def norm(vector):
    return (vector[0]**2+vector[1]**2)**0.5

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
class Player(object):
    
    def __init__(self, name, image, stats, position, location, hasBall = False):
        self.name = name
        self.image = image
        
        self.stats = stats
        self.pace = self.stats[0]
        self.dribbling = self.stats[1]
        self.shooting = self.stats[2]
        self.passing = self.stats[3]
        self.physical = self.stats[4]
        self.defense = self.stats[5]
        
        self.boostStats = ["pace", "dribbling", "shooting", "passing", "physical", "defense"]
        self.position = position #string, like forward, midfield, defender
        self.hasBall = hasBall
        self.location = location #player location
        #self.ballMoving = False
        
        self.isSub = False
        
        ### this is for substitutions screen
        self.subLocation = location #location is immutable which is nice
    
    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name

    def passBall(self, other, data): #attempt to pass
        passAccuracy = self.passing #code in error
        displacement = (-self.location[0]+other.location[0], -self.location[1]+other.location[1])
        
        data.originalDisplacement = displacement
        
        mag = norm(displacement)
        
        unitDisplacement = (displacement[0]/mag, displacement[1]/mag) #gives unit displacement
        
        data.displacement = unitDisplacement
        
        self.hasBall = False 
        data.ballMoving = True
        
        try:
            data.passableLiverpoolList = copy.copy(data.Liverpool.playerList)
            data.passableLiverpoolList.remove(self)
        except:
            pass
        
        try:
            data.passableBarcelonaList = copy.copy(data.Barcelona.playerList)
            data.passableBarcelonaList.remove(self)
        except:
            pass
        
        #other.hasBall = True
    
    def getPossession(self, data):
        if distance(self.location[0]+25, self.location[1]+25, data.ball[0][0]+10, data.ball[0][1]+10) < 46: #10+25sqrt(2)
            print("%s got possession" % self.name)
            self.hasBall = True
            data.ballMoving = False
            return True

    
        ### if ball is within certain distance of player, then they get possession, if it's same, then based on physical stat
        

        
        #self.ballMoving = True
    def controlBall(self, other):
        pass
    
    def __repr__(self):
        if self.hasBall:
            return "%s has ball!" %self.name
        else:
            return "%s doesn't have ball" %self.name
            
    
        
    def score(self, other): #other is goalie on opposing team
        #whether or not they score is dependent on distance, goalie's stats, and their shooting stat
        def distance(self, other):
            x = self.location[0]
            y = self.location[1]
            x1 = other.location[0]
            y1 = other.location[1]
            return ((x-x1)**2 + (y-y1)**2)**0.5
        shooting = self.stats[2] #probability they score
        reflexes =  other.stats[3]
        error = random.randint(90,110)
        if distance(self, other) <= 200:
            print("%s shot!" %self.name)
            if error/100*shooting > reflexes:
                print("%s scored!" %self.name)
                return True
            else:
                print("%s missed!" %self.name)
        return False
            
    
    def move(self, dx, dy):
        pass
        #their position will determine likelihood they are forward or not
    
class Club(object):
    def __init__(self, name, image, playerList, onRight = True):
        self.name = name
        self.image = image
        self.playerList = playerList
        self.onRight = True

    
    def hasBall(self):
        for player in self.playerList:
            if player.hasBall:
                return True
        return False

class User(Player):
    def __init__(self, name, image, stats, position = "f"):
        super().__init__(self, name, image, stats, position = "f")
        
    
class GoalKeeper(Player):
    def __init__(self, name, image, stats, position, location, hasBall = False):
        super().__init__(name, image, stats, position, location, hasBall = False)
        
        
        self.diving = self.stats[0]
        self.handling = self.stats[1]
        self.kicking = self.stats[2]
        self.reflexes = self.stats[3]
        self.speed = self.stats[4]
        self.positioning = self.stats[5]
        
        self.save = False
    
    def save(self):
        prob = random.randint(100)
        if x > self.stats[3]:
            self.save = True
        else:
            self.save = False
class Ball(object):
    def __init__(self, location):
        self.location = location #top right coordinate 
        self.radius = 10    
