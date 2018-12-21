from Players import *
"""import pygame
from bs4 import BeautifulSoup
import requests
import csv"""
#scrape Fifa data first
### starting positions assuming Barca has posession
def BarcelonaInitBall():
    logo = ""
    
    Dembele=Player("Dembele", "Images/Players/Barcelona/Dembele.gif", [89, 87, 75, 76, 55, 36], "f", (550, 75)) #180
    Suarez = Player("Suarez", "Images/Players/Barcelona/Suarez.gif", [80, 87, 90, 79, 85, 52], "f",(600, 325), True) #180
    Messi = Player("Messi", "Images/Players/Barcelona/Messi.gif", [88, 96, 91, 88, 32, 61], "f", (575, 550)) #240
    Coutinho = Player("Coutinho", "Images/Players/Barcelona/Coutinho.gif", [81, 91, 81, 86, 64, 45], "m", (500, 250)) #160
    Busquets = Player("Busquets", "Images/Players/Barcelona/Busquets.gif", [43, 78, 62, 79, 80, 85], "m",(450, 325))
    Rakitic = Player("Rakitic", "Images/Players/Barcelona/Rakitic.gif", [62, 82, 84, 87, 69, 72], "m",(500, 400))
    Alba = Player("Alba", "Images/Players/Barcelona/Alba.gif", [93, 83, 69, 79, 72, 79], "d",(300, 50))
    Umtiti = Player("Umtiti", "Images/Players/Barcelona/Umtiti.gif", [72, 72, 64, 71, 82, 88], "d",(200, 200)) #180
    Pique = Player("Pique", "Images/Players/Barcelona/Pique.gif", [55, 66, 61, 69, 76, 87], "d",(200, 400),)
    Roberto = Player("Roberto", "Images/Players/Barcelona/Roberto8g.gif", [78, 77, 63, 81, 71, 80], "d",(300, 600)) #180
    TerStegen = GoalKeeper("Ter Stegen", "Images/Players/Barcelona/TerStegen.gif", [87, 85, 88, 90, 38, 85], "gk", (0, 325))
    
    players = [Dembele, Suarez, Messi, Coutinho, Busquets, Rakitic, Alba, Umtiti, Pique, Roberto, TerStegen]
    return Club("Barcelona", logo, players)

def BayernInit():
    logo = ""
    players = []
    return Club("Bayern", logo, players)

def LiverpoolInitNoBall():
    logo = ""
    
    Salah = Player("Salah", "Images/Players/Liverpool/Salah.gif", [93, 89, 86, 83, 73, 42],"f", (650, 75)) #160x160
    Mane = Player("Mane", "Images/Players/Liverpool/Mane8g.gif", [94, 87, 80, 76, 73, 42], "f",(650, 575))
    Firmino = Player("Firmino", "Images/Players/Liverpool/Firmino.gif", [81, 90, 87, 83, 85, 56], "f",(800, 325))
    OxladeChamberlain = Player("Oxlade-Chamberlain", "Images/Players/Liverpool/Oxlade-Chamberlain8g.gif", [88, 83, 70, 74, 70, 52], "m",(750, 220))
    Milner = Player("Milner", "Images/Players/Liverpool/Milner8g.gif", [62, 77, 70, 82, 78, 75], "m",(800, 475))
    Henderson = Player("Henderson", "Images/Players/Liverpool/Henderson8g.gif", [66, 75, 70, 83, 78, 77], "m", (900, 325))
    Robertson = Player("Robertson", "Images/Players/Liverpool/Robertson8g.gif", [84, 77, 59, 72, 73, 77], "d", (1000, 600))
    VanDijk = Player("Van Dijk", "Images/Players/Liverpool/VanDijk.gif", [71, 70, 60, 67, 84, 85], "d",(1050, 275))
    Lovren = Player("Lovren", "Images/Players/Liverpool/Lovren.gif", [55, 63, 40, 59, 79, 81], "d",(1050, 400))
    AlexanderArnold = Player("Alexander-Arnold", "Images/Players/Liverpool/AlexanderArnold8g.gif", [80, 73, 60, 75, 69, 73] , "d",(1000, 100)) 
    Alisson = GoalKeeper("Alisson", "Images/Players/Liverpool/Alisson8g.gif", [82, 81, 85, 88, 54, 83], "gk", (1244-50,325)) #180x180
    
    players = [Salah, Mane, Firmino, Alisson, OxladeChamberlain, Milner, Henderson, Robertson, VanDijk, Lovren, AlexanderArnold]
    
    return Club("Liverpool", logo, players, False)




#stats = [pace, dribbling, shooting, passing, physical, defense]
#goalie stats = [diving, handling, kicking, reflxes, speed, positioning]



### starting positions assuming Liverpool has ball



def LiverpoolInitBall():
    logo = ""
    
    Salah = Player("Salah", "Images/Players/Liverpool/Salah.gif", [93, 89, 86, 83, 73, 42],"f", (650, 75)) #160x160
    Mane = Player("Mane", "Images/Players/Liverpool/Mane8g.gif", [94, 87, 80, 76, 73, 42], "f",(650, 575))
    Firmino = Player("Firmino", "Images/Players/Liverpool/Firmino.gif", [81, 90, 87, 83, 85, 56], "f",(800, 325), True)
    OxladeChamberlain = Player("Oxlade-Chamberlain", "Images/Players/Liverpool/Oxlade-Chamberlain8g.gif", [88, 83, 70, 74, 70, 52], "m",(750, 220))
    Milner = Player("Milner", "Images/Players/Liverpool/Milner8g.gif", [62, 77, 70, 82, 78, 75], "m",(800, 475))
    Henderson = Player("Henderson", "Images/Players/Liverpool/Henderson8g.gif", [66, 75, 70, 83, 78, 77], "m", (900, 325))
    Robertson = Player("Robertson", "Images/Players/Liverpool/Robertson8g.gif", [84, 77, 59, 72, 73, 77], "d", (1000, 600))
    VanDijk = Player("Van Dijk", "Images/Players/Liverpool/VanDijk.gif", [71, 70, 60, 67, 84, 85], "d",(1050, 275))
    Lovren = Player("Lovren", "Images/Players/Liverpool/Lovren.gif", [55, 63, 40, 59, 79, 81], "d",(1050, 400))
    AlexanderArnold = Player("Alexander-Arnold", "Images/Players/Liverpool/AlexanderArnold8g.gif", [80, 73, 60, 75, 69, 73] , "d",(1000, 100)) 
    Alisson = GoalKeeper("Alisson", "Images/Players/Liverpool/Alisson8g.gif", [82, 81, 85, 88, 54, 83], "gk", (1244-50,325)) #180x180
    
    players = [Salah, Mane, Firmino, Alisson, OxladeChamberlain, Milner, Henderson, Robertson, VanDijk, Lovren, AlexanderArnold]
    
    return Club("Liverpool", logo, players)


def BarcelonaInitNoBall():
    logo = ""
    
    Dembele=Player("Dembele", "Images/Players/Barcelona/Dembele.gif", [89, 87, 75, 76, 55, 36], "f", (550, 75)) #180
    Suarez = Player("Suarez", "Images/Players/Barcelona/Suarez.gif", [80, 87, 90, 79, 85, 52], "f",(600, 325)) #180
    Messi = Player("Messi", "Images/Players/Barcelona/Messi.gif", [88, 96, 91, 88, 32, 61], "f", (575, 550)) #240
    Coutinho = Player("Coutinho", "Images/Players/Barcelona/Coutinho.gif", [81, 91, 81, 86, 64, 45], "m", (500, 250)) #160
    Busquets = Player("Busquets", "Images/Players/Barcelona/Busquets.gif", [43, 78, 62, 79, 80, 85], "m",(450, 325))
    Rakitic = Player("Rakitic", "Images/Players/Barcelona/Rakitic.gif", [62, 82, 84, 87, 69, 72], "m",(500, 400))
    Alba = Player("Alba", "Images/Players/Barcelona/Alba.gif", [93, 83, 69, 79, 72, 79], "d",(300, 50))
    Umtiti = Player("Umtiti", "Images/Players/Barcelona/Umtiti.gif", [72, 72, 64, 71, 82, 88], "d",(200, 200)) #180
    Pique = Player("Pique", "Images/Players/Barcelona/Pique.gif", [55, 66, 61, 69, 76, 87], "d",(200, 400),)
    Roberto = Player("Roberto", "Images/Players/Barcelona/Roberto8g.gif", [78, 77, 63, 81, 71, 80], "d",(300, 600)) #180
    TerStegen = GoalKeeper("Ter Stegen", "Images/Players/Barcelona/TerStegen.gif", [87, 85, 88, 90, 38, 85], "gk", (0, 325))
    
    players = [Dembele, Suarez, Messi, Coutinho, Busquets, Rakitic, Alba, Umtiti, Pique, Roberto, TerStegen]
    return Club("Barcelona", logo, players, False)



