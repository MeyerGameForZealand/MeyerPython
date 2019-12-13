#region -------------------------------------------------     Imports     ----------------------------------------------
from sense_hat import SenseHat
import time
import random
from time import sleep
s = SenseHat()
sense = SenseHat()
s.low_light = True

#UDP Import
from socket import *
from datetime import datetime
import threading

#endregion

#region-------------------------------------------    Global var    ----------------------------------------------------

#On Off------
playerAmountOn = 1
TurnSwithOn = 0
PlayerRoundOn = 0

# 2 defult
playerAmount = 2

#Dices
UserChoiceTheDice = 0
UserChoiceForDiceC = 0
UserChoiceForDiceD = 0

#Turn
turn=1
LastPlayer = 1

#Intro Count
introCount = 0

#Player HP
player1HP = 0
player2HP = 0
player3HP = 0
player4HP = 0
player5HP = 0
player6HP = 0

#Dices
Dice1 = 0
Dice2 = 0

#WhoWon
WhoWon = 0
#endregion

#region-------------------------------------------------    GUI    ------------------------------------------------------
#-- - - Colors - - -
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)

# - - - - - - - - - - Dices - - - - - - - - - -
# - - - - - Dice A - - - - -
def PixelA1():
    #On
    s.set_pixel(1, 1, blue)
    #Off
    s.set_pixel(0,0, nothing)
    s.set_pixel(0, 1, nothing)
    s.set_pixel(0, 2, nothing)
    s.set_pixel(2, 0, nothing)
    s.set_pixel(2, 1, nothing)
    s.set_pixel(2, 2, nothing)

def PixelA2():
    # On
    s.set_pixel(0, 2, blue)
    s.set_pixel(2, 0, blue)
    #Off
    s.set_pixel(0, 0, nothing)
    s.set_pixel(0, 1, nothing)
    s.set_pixel(1, 1, nothing)
    s.set_pixel(2, 1, nothing)
    s.set_pixel(2, 2, nothing)

def PixelA3():
    # On
    s.set_pixel(0, 2, blue)
    s.set_pixel(2, 0, blue)
    s.set_pixel(1, 1, blue)
    #Off
    s.set_pixel(0, 0, nothing)
    s.set_pixel(0, 1, nothing)
    s.set_pixel(2, 1, nothing)
    s.set_pixel(2, 2, nothing)

def PixelA4():
    # On
    s.set_pixel(0, 0, blue)
    s.set_pixel(0, 2, blue)
    s.set_pixel(2, 0, blue)
    s.set_pixel(2, 2, blue)
    #Off
    s.set_pixel(0, 1, nothing)
    s.set_pixel(1, 1, nothing)
    s.set_pixel(2, 1, nothing)

def PixelA5():
    # On
    s.set_pixel(0, 0, blue)
    s.set_pixel(0, 2, blue)
    s.set_pixel(2, 0, blue)
    s.set_pixel(2, 2, blue)
    s.set_pixel(1, 1, blue)
    #Off
    s.set_pixel(0, 1, nothing)
    s.set_pixel(2, 1, nothing)

def PixelA6():
    # On
    s.set_pixel(0, 0, blue)
    s.set_pixel(0, 1, blue)
    s.set_pixel(0, 2, blue)
    s.set_pixel(2, 0, blue)
    s.set_pixel(2, 1, blue)
    s.set_pixel(2, 2, blue)
    #Off
    s.set_pixel(1, 1, nothing)

# - - - - - Dice B - - - - -
def PixelB1():
    # On
    s.set_pixel(6, 1, blue)
    #Off
    s.set_pixel(5, 0, nothing)
    s.set_pixel(5, 1, nothing)
    s.set_pixel(5, 2, nothing)
    s.set_pixel(7, 0, nothing)
    s.set_pixel(7, 1, nothing)
    s.set_pixel(7, 2, nothing)

def PixelB2():
    # On
    s.set_pixel(5, 2, blue)
    s.set_pixel(7, 0, blue)
    #Off
    s.set_pixel(5, 0, nothing)
    s.set_pixel(5, 1, nothing)
    s.set_pixel(7, 1, nothing)
    s.set_pixel(7, 2, nothing)
    s.set_pixel(6, 1, nothing)

def PixelB3():
    # On
    s.set_pixel(7, 0, blue)
    s.set_pixel(6, 1, blue)
    s.set_pixel(5, 2, blue)
    #Off
    s.set_pixel(5, 0, nothing)
    s.set_pixel(5, 1, nothing)
    s.set_pixel(7, 1, nothing)
    s.set_pixel(7, 2, nothing)

def PixelB4():
    # On
    s.set_pixel(5, 0, blue)
    s.set_pixel(7, 0, blue)
    s.set_pixel(5, 2, blue)
    s.set_pixel(7, 2, blue)
    #Off
    s.set_pixel(5, 1, nothing)
    s.set_pixel(7, 1, nothing)
    s.set_pixel(6, 1, nothing)

def PixelB5():
    # On
    s.set_pixel(5, 0, blue)
    s.set_pixel(7, 0, blue)
    s.set_pixel(6, 1, blue)
    s.set_pixel(5, 2, blue)
    s.set_pixel(7, 2, blue)
    #Off
    s.set_pixel(5, 1, nothing)
    s.set_pixel(7, 1, nothing)

def PixelB6():
    # On
    s.set_pixel(5, 0, blue)
    s.set_pixel(5, 1, blue)
    s.set_pixel(5, 2, blue)
    s.set_pixel(7, 0, blue)
    s.set_pixel(7, 1, blue)
    s.set_pixel(7, 2, blue)
    #Off
    s.set_pixel(6, 1, nothing)

# - - - - - Dice C - - - - -
def PixelC1():
    # On
    s.set_pixel(1, 6, blue)
    #Off
    s.set_pixel(0, 5, nothing)
    s.set_pixel(2, 5, nothing)
    s.set_pixel(0, 7, nothing)
    s.set_pixel(2, 7, nothing)
    s.set_pixel(0, 6, nothing)
    s.set_pixel(2, 6, nothing)

def PixelC2():
    # On
    s.set_pixel(0, 7, blue)
    s.set_pixel(2, 5, blue)
    #Off
    s.set_pixel(0, 5, nothing)
    s.set_pixel(2, 7, nothing)
    s.set_pixel(0, 6, nothing)
    s.set_pixel(2, 6, nothing)
    s.set_pixel(1, 6, nothing)

def PixelC3():
    # On
    s.set_pixel(2, 5, blue)
    s.set_pixel(1, 6, blue)
    s.set_pixel(0, 7, blue)
    #Off
    s.set_pixel(0, 5, nothing)
    s.set_pixel(2, 7, nothing)
    s.set_pixel(0, 6, nothing)
    s.set_pixel(2, 6, nothing)

def PixelC4():
    # On
    s.set_pixel(0, 5, blue)
    s.set_pixel(2, 5, blue)
    s.set_pixel(0, 7, blue)
    s.set_pixel(2, 7, blue)
    #Off
    s.set_pixel(0, 6, nothing)
    s.set_pixel(2, 6, nothing)
    s.set_pixel(1, 6, nothing)

def PixelC5():
    # On
    s.set_pixel(0, 5, blue)
    s.set_pixel(2, 5, blue)
    s.set_pixel(0, 7, blue)
    s.set_pixel(2, 7, blue)
    s.set_pixel(1, 6, blue)
    #Off
    s.set_pixel(0, 6, nothing)
    s.set_pixel(2, 6, nothing)

def PixelC6():
    # On
    s.set_pixel(0, 5, blue)
    s.set_pixel(2, 5, blue)
    s.set_pixel(0, 7, blue)
    s.set_pixel(2, 7, blue)
    s.set_pixel(0, 6, blue)
    s.set_pixel(2, 6, blue)
    #Off
    s.set_pixel(1, 6, nothing)

# - - - - - Dice D - - - - -
def PixelD1():
    # On
    s.set_pixel(6, 6, blue)
    #Off
    s.set_pixel(5, 5, nothing)
    s.set_pixel(7, 5, nothing)
    s.set_pixel(5, 7, nothing)
    s.set_pixel(7, 7, nothing)
    s.set_pixel(5, 6, nothing)
    s.set_pixel(7, 6, nothing)

def PixelD2():
    # On
    s.set_pixel(5, 7, blue)
    s.set_pixel(7, 5, blue)
    #Off
    s.set_pixel(7, 7, nothing)
    s.set_pixel(5, 6, nothing)
    s.set_pixel(7, 6, nothing)
    s.set_pixel(6, 6, nothing)

def PixelD3():
    # On
    s.set_pixel(7, 5, blue)
    s.set_pixel(6, 6, blue)
    s.set_pixel(5, 7, blue)
    #Off
    s.set_pixel(5, 5, nothing)
    s.set_pixel(7, 7, nothing)
    s.set_pixel(5, 6, nothing)
    s.set_pixel(7, 6, nothing)

def PixelD4():
    # On
    s.set_pixel(5, 5, blue)
    s.set_pixel(7, 5, blue)
    s.set_pixel(5, 7, blue)
    s.set_pixel(7, 7, blue)
    #Off
    s.set_pixel(5, 6, nothing)
    s.set_pixel(7, 6, nothing)
    s.set_pixel(6, 6, nothing)

def PixelD5():
    # On
    s.set_pixel(5, 5, blue)
    s.set_pixel(7, 5, blue)
    s.set_pixel(5, 7, blue)
    s.set_pixel(7, 7, blue)
    s.set_pixel(6, 6, blue)
    #Off
    s.set_pixel(5, 6, nothing)
    s.set_pixel(7, 6, nothing)

def PixelD6():
    # On
    s.set_pixel(5, 5, blue)
    s.set_pixel(7, 5, blue)
    s.set_pixel(5, 7, blue)
    s.set_pixel(7, 7, blue)
    s.set_pixel(5, 6, blue)
    s.set_pixel(7, 6, blue)
    #Off
    s.set_pixel(6, 6, nothing)

# - - - - - - - - - - - HP - - - - - - - - - - -
def HP1():
    # On
    s.set_pixel(0, 3, red)
    #Off
    s.set_pixel(1, 4, red)
    s.set_pixel(2, 3, red)
    s.set_pixel(3, 4, red)
    s.set_pixel(4, 3, red)
    s.set_pixel(5, 4, red)

def HP2():
    # On
    s.set_pixel(0, 3, red)
    s.set_pixel(1, 4, red)
    #Off
    s.set_pixel(2, 3, red)
    s.set_pixel(3, 4, red)
    s.set_pixel(4, 3, red)
    s.set_pixel(5, 4, red)

def HP3():
    # On
    s.set_pixel(0, 3, red)
    s.set_pixel(1, 4, red)
    s.set_pixel(2, 3, red)
    #Off
    s.set_pixel(3, 4, red)
    s.set_pixel(4, 3, red)
    s.set_pixel(5, 4, red)

def HP4():
    # On
    s.set_pixel(0, 3, red)
    s.set_pixel(1, 4, red)
    s.set_pixel(2, 3, red)
    s.set_pixel(3, 4, red)
    #Off
    s.set_pixel(4, 3, red)
    s.set_pixel(5, 4, red)

def HP5():
    # On
    s.set_pixel(0, 3, red)
    s.set_pixel(1, 4, red)
    s.set_pixel(2, 3, red)
    s.set_pixel(3, 4, red)
    s.set_pixel(4, 3, red)
    #Off
    s.set_pixel(5, 4, red)

def HP6():
    # On
    s.set_pixel(0, 3, red)
    s.set_pixel(1, 4, red)
    s.set_pixel(2, 3, red)
    s.set_pixel(3, 4, red)
    s.set_pixel(4, 3, red)
    s.set_pixel(5, 4, red)
    #Off

# - - - - - - - - - - Numbers - - - - - - - - - -
def number_1():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def number_2():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, O, O, O,
        O, W, O, O, O, W, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, W, O, O, O, O,
        O, O, W, O, O, O, O, O,
        O, W, W, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def number_3():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, W, O, O, W, O, O,
        O, O, O, O, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, W, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def number_4():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, W, O, O, W, O, O,
        O, O, W, O, O, W, O, O,
        O, O, W, O, O, W, O, O,
        O, O, W, W, W, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def number_5():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, O, O, W, O, O,
        O, O, O, O, O, W, O, O,
        O, O, W, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

def number_6():
    W = white
    O = nothing
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, W, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, O, O, O, O, O,
        O, O, W, W, W, W, O, O,
        O, O, W, O, O, W, O, O,
        O, O, O, W, W, W, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo

# - - - - - - - - - - Letters - - - - - - - - - -
def letter_M():
    W = white
    R = red
    Y = yellow
    B = blue
    O = nothing
    logo = [
        W, W, W, W, W, W, W, W,
        W, B, B, W, W, B, B, W,
        W, B, B, B, B, W, B, W,
        W, B, W, B, B, W, B, W,
        W, B, W, B, B, W, B, W,
        W, B, W, B, B, W, B, W,
        W, B, W, B, B, W, B, W,
        W, W, W, W, W, W, W, W,
    ]
    return logo

def letter_E():
    W = white
    R = red
    Y = yellow
    B = blue
    O = nothing
    logo = [
        W, W, W, W, W, W, W, W,
        W, W, B, B, B, B, W, W,
        W, W, B, W, W, W, W, W,
        W, W, B, W, W, W, W, W,
        W, W, B, B, B, B, W, W,
        W, W, B, W, W, W, W, W,
        W, W, B, B, B, B, W, W,
        W, W, W, W, W, W, W, W,
    ]
    return logo

def letter_Y():
    W = white
    R = red
    Y = yellow
    B = blue
    O = nothing
    logo = [
        W, W, W, W, W, W, W, W,
        W, W, B, W, W, B, W, W,
        W, W, B, W, W, B, W, W,
        W, W, B, W, W, B, W, W,
        W, W, W, B, B, W, W, W,
        W, W, W, B, B, W, W, W,
        W, W, W, B, B, W, W, W,
        W, W, W, W, W, W, W, W,
    ]
    return logo

def letter_R():
    W = white
    R = red
    Y = yellow
    B = blue
    O = nothing
    logo = [
        W, W, W, W, W, W, W, W,
        W, W, B, B, B, W, W, W,
        W, W, B, W, W, B, W, W,
        W, W, B, B, B, W, W, W,
        W, W, B, W, B, W, W, W,
        W, W, B, W, W, B, W, W,
        W, W, B, W, W, B, W, W,
        W, W, W, W, W, W, W, W,
    ]
    return logo

# - - - - - - - - - - UserMenu - - - - - - - - - -
def userMenu():
    s.clear()
    W = white
    R = red
    Y = yellow
    B = blue
    O = nothing
    G = green
    logo = [
        W, W, W, B, W, W, W, W,
        W, W, B, B, B, W, W, W,
        W, W, W, B, W, W, G, W,
        W, R, W, B, G, G, G, G,
        R, R, R, R, Y, W, G, W,
        W, R, W, W, Y, W, W, W,
        W, W, W, Y, Y, Y, W, W,
        W, W, W, W, Y, W, W, W,
    ]
    return logo
#endregion

#region---------------------------------------------    Intro Gui    ------------------------------------------------------
#Set Letters
images = [letter_M, letter_E, letter_Y, letter_E, letter_R]
introCount = 0
userMenu = [userMenu]

#WriteLetters
while introCount < 5:
    s.set_pixels(images[introCount % len(images)]())
    time.sleep(.75)
    introCount += 1
#endregion

#region --------------------------------------    Between players    ---------------------------------------------------

def TurnSwith():
    s = SenseHat()
    # - - GlobalHP - -
    global player1HP
    global player2HP
    global player3HP
    global player4HP
    global player5HP
    global player6HP

    # - - Turn - - -
    global TurnSwithOn
    global PlayerRoundOn
    global turn
    global LastPlayer

    # - - Dices - -
    global UserChoiceForDiceC
    global UserChoiceForDiceD

    # - - Set Last Player - -
    LastPlayer = turn

    # - - UI - -
    s.clear()
    s.set_pixels(userMenu[introCount % len(userMenu)]())

    # SenceHat Activate                 <-- Test
    s = SenseHat()
    sense = SenseHat()


    # - - loop - -
    while TurnSwithOn == 1:
        for event in sense.stick.get_events():
            if event.action == "pressed":

                # + - dice number.
                # if event.direction == "up":
                #    if UserChoiceTheDice==0:
                #        UserChoiceForDiceC+=1
                #    if UserChoiceTheDice==1:
                #        UserChoiceForDiceD+=1
                # elif event.direction == "down":
                #    if UserChoiceTheDice==0:
                #        UserChoiceForDiceC-=1
                #    if UserChoiceTheDice==1:
                #        UserChoiceForDiceD-=1


                # ----------------------------If Next player belive the previus player was lying
                if event.direction == "left":
                    # ----------------------------If The Player Is telling the truth -----------------------------------
                    if Dice1 == UserChoiceForDiceC and Dice2 == UserChoiceForDiceD:
                        if turn == 1:
                            if player2HP > 0:
                                player2HP -= 1
                            elif player3HP > 0:
                                player3HP -= 1
                            elif player4HP > 0:
                                player4HP -= 1
                            elif player5HP > 0:
                                player5HP -= 1
                            elif player6HP > 0:
                                player6HP -= 1
                        if turn == 2:
                            if player3HP > 0:
                                player3HP -= 1
                            elif player4HP > 0:
                                player4HP -= 1
                            elif player5HP > 0:
                                player5HP -= 1
                            elif player6HP > 0:
                                player6HP -= 1
                            elif player1HP > 0:
                                player1HP -= 1
                        if turn == 3:
                            if player4HP > 0:
                                player4HP -= 1
                            elif player5HP > 0:
                                player5HP -= 1
                            elif player6HP > 0:
                                player6HP -= 1
                            elif player1HP > 0:
                                player1HP -= 1
                            elif player2HP > 0:
                                player2HP -= 1
                        if turn == 4:
                            if player5HP > 0:
                                player5HP -= 1
                            elif player6HP > 0:
                                player6HP -= 1
                            elif player1HP > 0:
                                player1HP -= 1
                            elif player2HP > 0:
                                player2HP -= 1
                            elif player3HP > 0:
                                player3HP -= 1
                        if turn == 5:
                            if player6HP > 0:
                                player6HP -= 1
                            elif player1HP > 0:
                                player1HP -= 1
                            elif player2HP > 0:
                                player2HP -= 1
                            elif player3HP > 0:
                                player3HP -= 1
                            elif player4HP > 0:
                                player4HP -= 1
                        if turn == 6:
                            if player1HP > 0:
                                player1HP -= 1
                            elif player2HP > 0:
                                player2HP -= 1
                            elif player3HP > 0:
                                player3HP -= 1
                            elif player4HP > 0:
                                player4HP -= 1
                            elif player5HP > 0:
                                player5HP -= 1
                        #Break The Loop
                        TurnSwithOn = 0
                        PlayerRoundOn = 1

                        # ----------------------------if player is Lying----------------------------
                    elif Dice1 != UserChoiceForDiceC and Dice2 != UserChoiceForDiceD:
                        if LastPlayer == 1:
                            turn = 1
                            player1HP -= 1
                        elif LastPlayer == 2:
                            turn = 2
                            player2HP -= 1
                        elif LastPlayer == 3:
                            turn = 3
                            player1HP -= 1
                        elif LastPlayer == 4:
                            turn = 4
                            player1HP -= 1
                        elif LastPlayer == 5:
                            turn = 5
                            player1HP -= 1
                        elif LastPlayer == 6:
                            turn = 6
                            player6HP -= 1
                    TurnSwithOn = 0
                    PlayerRoundOn = 1

                # --------------------------------------Next Player----------------------------------------
                elif event.direction == "right":
                    TurnSwithOn = 0
                    PlayerRoundOn = 1

    WhoWonDef()
    NextTurn() #Using Turn Secure
#endregion

#region--------------------------------------------- Turn Secure --------------------------------------------------------

def NextTurn():
    # - - GlobalHP - -
    global player1HP
    global player2HP
    global player3HP
    global player4HP
    global player5HP
    global player6HP

    # - - Turn - - -
    global TurnSwithOn
    global PlayerRoundOn
    global turn
    global LastPlayer

    # - - Dices - -
    global UserChoiceForDiceC
    global UserChoiceForDiceD
    # -----     -----     2 player game     -----     -----

    #if playerAmount==2:
    #    turn+=1

    # -----     -----     3 player game     -----     -----
    if playerAmount==3:
        # p1
        if turn==1 and player2HP==0:
            turn+=2
        # p2
        if turn==2 and player3HP==0:
            turn+=2
        # p3
        if turn==3 and player1HP==0:
            turn+=2
        else:
            turn+=1


    # -----     -----     4 player game     -----     -----
    elif playerAmount==4:
        # -----     p1     -----
        if turn==1 and player2HP==0 and player3HP==0:
            turn+=3
        if turn==1 and player2HP==0:
            turn+=2

        # -----     p2     -----
        if turn==2 and player3HP==0 and player1HP==0:
            turn+=3
        if turn==2 and player3HP==0:
            turn+=2
        # -----     p3     -----
        if turn==3 and player4HP==0 and player1HP==0:
            turn+=3
        if turn==3 and player4HP==0:
            turn+=2

        # -----     p4     -----
        if turn==4 and player1HP==0 and player2HP==0:
            turn+=3
        if turn==4 and player1HP==0:
            turn+=2
        else:
            turn += 1

    # -----     -----     5 player game     -----     -----
    elif playerAmount==5:
        # -----     p1     -----
        if turn==1 and player2HP==0 and player3HP==0 and player4HP==0:
            turn+=4
        elif turn==1 and player2HP==0 and player3HP==0:
            turn+=3
        elif turn==1 and player2HP==0:
            turn+=2
        # -----     p2     -----
        if turn==2 and player3HP==0 and player4HP==0 and player5HP==0:
            turn+=4
        elif turn==2 and player3HP==0 and player4HP==0:
            turn+=3
        elif turn==2 and player3HP==0:
            turn+=2
        # -----     p3     -----
        if turn==3 and player4HP==0 and player5HP==0 and player1HP==0:
            turn+=4
        elif turn==3 and player4HP==0 and player5HP==0:
            turn+=3
        elif turn==3 and player4HP==0:
            turn+=2
        # -----     p4     -----
        if turn==4 and player5HP==0 and player1HP==0 and player2HP==0:
            turn+=4
        elif turn==4 and player5HP==0 and player1HP==0:
            turn+=3
        elif turn==4 and player5HP==0:
            turn+=2
        # -----     p5     -----
        if turn==5 and player1HP==0 and player2HP==0 and player3HP==0:
            turn+=4
        elif turn==5 and player1HP==0 and player2HP==0:
            turn+=3
        elif turn==5 and player1HP==0:
            turn+=2
        else:
            turn += 1
         # -----     -----     6 player game     -----     -----
    elif playerAmount==6:
        # -----     p1     -----
        if turn==1 and player2HP==0 and player3HP==0 and player4HP==0 and player5HP==0:
            turn+=5
        elif turn==1 and player2HP==0 and player3HP==0 and player4HP==0:
            turn+=4
        elif turn==1 and player2HP==0 and player3HP==0:
            turn+=3
        elif turn==1 and player2HP==0:
            turn+=2

        # -----     p2     -----
        if turn==2 and player3HP==0 and player4HP==0 and player5HP==0 and player6HP==0:
            turn+=5
        elif turn==2 and player3HP==0 and player4HP==0 and player5HP==0:
            turn+=4
        elif turn==2 and player3HP==0 and player4HP==0:
            turn+=3
        elif turn==2 and player3HP==0:
            turn+=2

        # -----     p3     -----
        if turn==3 and player4HP==0 and player5HP==0 and player6HP==0 and player1HP==0:
            turn+=5
        elif turn==3 and player4HP==0 and player5HP==0 and player6HP==0:
            turn+=4
        elif turn==3 and player4HP==0 and player5HP==0:
            turn+=3
        elif turn==3 and player4HP==0:
            turn+=2

        # -----     p4     -----
        if turn==4 and player5HP==0 and player6HP==0 and player1HP==0 and player2HP==0:
            turn+=5
        elif turn==4 and player5HP==0 and player6HP==0 and player1HP==0:
            turn+=4
        elif turn==4 and player5HP==0 and player6HP==0:
            turn+=3
        elif turn==4 and player5HP==0:
            turn+=2

        # -----     p5     -----
        if turn==5 and player6HP==0 and player1HP==0 and player2HP==0 and player3HP==3:
            turn+=5
        elif turn==5 and player6HP==0 and player1HP==0 and player2HP==0:
            turn+=4
        elif turn==5 and player6HP==0 and player1HP==0:
            turn+=3
        elif turn==5 and player6HP==0:
            turn+=2

        # -----     p6     -----
        if turn==6 and player1HP==0 and player2HP==0 and player3HP==0 and player4HP==0:
            turn+=5
        elif turn==6 and player1HP==0 and player2HP==0 and player3HP==0:
            turn+=4
        elif turn==6 and player1HP==0 and player2HP==0:
            turn+=3
        elif turn==6 and player1HP==0:
            turn+=2
        else:
            turn += 1

    #Add end of round
    else:
        turn+=1
    #If The round is over the amount of turns
    if turn > playerAmount:
        turnFix = turn - playerAmount
        turn =0
        turn+turnFix
        if turn == 0:
            turn=1
#endregion

#region---------------------------------------    Player Round    ------------------------------------------------------

def PlayerRound():
    global PlayerRoundOn
    global TurnSwithOn
    global introCount
    #For HP Drawings
    global turn
    global player1HP
    global player2HP
    global player3HP
    global player4HP
    global player5HP
    global player6HP

    # ShakeTime
    ShakeTimes = 1

    #Test
    s = SenseHat()
    sense = SenseHat()
    s.clear()
    #TestEnd
    while PlayerRoundOn == 1:
        x, y, z = sense.get_accelerometer_raw().values()
        x = abs(x)
        y = abs(y)
        z = abs(z)

        global UserChoiceTheDice
        global UserChoiceForDiceC
        global UserChoiceForDiceD

        global Dice1
        global Dice2

        # - - - - - HP Show - - - - -                            -----------------------FIX----------
        if turn == 1:
            if player1HP == 6:
                HP6()
            elif player1HP == 5:
                HP5()
            elif player1HP == 4:
                HP4()
            elif player1HP == 3:
                HP3()
            elif player1HP == 2:
                HP2()
            elif player1HP == 1:
                HP1()

        if turn == 2:
            if player2HP == 6:
                HP6()
            elif player2HP == 5:
                HP5()
            elif player2HP == 4:
                HP4()
            elif player2HP == 3:
                HP3()
            elif player2HP == 2:
                HP2()
            elif player2HP == 1:
                HP1()

        if turn == 3:
            if player3HP == 6:
                HP6()
            elif player3HP == 5:
                HP5()
            elif player3HP == 4:
                HP4()
            elif player3HP == 3:
                HP3()
            elif player3HP == 2:
                HP2()
            elif player3HP == 1:
                HP1()

        if turn == 4:
            if player4HP == 6:
                HP6()
            elif player4HP == 5:
                HP5()
            elif player4HP == 4:
                HP4()
            elif player4HP == 3:
                HP3()
            elif player4HP == 2:
                HP2()
            elif player4HP == 1:
                HP1()

        if turn == 5:
            if player5HP == 6:
                HP6()
            elif player5HP == 5:
                HP5()
            elif player5HP == 4:
                HP4()
            elif player5HP == 3:
                HP3()
            elif player5HP == 2:
                HP2()
            elif player5HP == 1:
                HP1()

        if turn == 6:
            if player6HP == 6:
                HP6()
            elif player6HP == 5:
                HP5()
            elif player6HP == 4:
                HP4()
            elif player6HP == 3:
                HP3()
            elif player6HP == 2:
                HP2()
            elif player6HP == 1:
                HP1()
            # -----------------------------------------------------------------------


        if x > 5.4 or y > 5.4 or z > 5.4:
            if ShakeTimes==1:
                #ShakeTimes off
                ShakeTimes=0

                Dice1 = random.randint(1, 6)
                if Dice1 == 1:
                    PixelA1()
                elif Dice1 == 2:
                    PixelA2()
                elif Dice1 == 3:
                    PixelA3()
                elif Dice1 == 4:
                    PixelA4()
                elif Dice1 == 5:
                    PixelA5()
                elif Dice1 == 6:
                    PixelA6()

                Dice2 = random.randint(1, 6)
                if Dice2 == 1:
                    PixelB1()
                elif Dice2 == 2:
                    PixelB2()
                elif Dice2 == 3:
                    PixelB3()
                elif Dice2 == 4:
                    PixelB4()
                elif Dice2 == 5:
                    PixelB5()
                elif Dice2 == 6:
                    PixelB6()


        for event in sense.stick.get_events():

            if event.action == "pressed":

                # + - dice number.
                if event.direction == "up":
                    if UserChoiceTheDice==0:
                        UserChoiceForDiceC+=1
                    if UserChoiceTheDice==1:
                        UserChoiceForDiceD+=1
                if event.direction == "down":
                    if UserChoiceTheDice==0:
                        UserChoiceForDiceC-=1
                    if UserChoiceTheDice==1:
                        UserChoiceForDiceD-=1

                # With dice
                elif event.direction == "right":
                    if UserChoiceTheDice == 0:
                        UserChoiceTheDice =1
                elif event.direction == "left":
                    if UserChoiceTheDice == 1:
                        UserChoiceTheDice = 0

                        # Over And Under Safe
                if UserChoiceForDiceC==0:
                    UserChoiceForDiceC=1
                if UserChoiceForDiceC==7:
                    UserChoiceForDiceC=6

                if UserChoiceForDiceD==0:
                    UserChoiceForDiceD=1
                if UserChoiceForDiceD==7:
                    UserChoiceForDiceD=6

                # Dice C & D UI
                if UserChoiceForDiceC == 1:
                    PixelC1()
                if UserChoiceForDiceC == 2:
                    PixelC2()
                if UserChoiceForDiceC == 3:
                    PixelC3()
                if UserChoiceForDiceC == 4:
                    PixelC4()
                if UserChoiceForDiceC == 5:
                    PixelC5()
                if UserChoiceForDiceC == 6:
                    PixelC6()

                if UserChoiceForDiceD == 1:
                    PixelD1()
                if UserChoiceForDiceD == 2:
                    PixelD2()
                if UserChoiceForDiceD == 3:
                    PixelD3()
                if UserChoiceForDiceD == 4:
                    PixelD4()
                if UserChoiceForDiceD == 5:
                    PixelD5()
                if UserChoiceForDiceD == 6:
                    PixelD6()


                if event.direction == "middle":
                    s.clear()
                    PlayerRoundOn=0
                    TurnSwithOn=1                               #Look
#endregion

#region----------------------------    Player amount / Create Players    -----------------------------------------------

def PlayerAmount():
    global playerAmountOn
    global playerAmount
    global introCount
    global TurnSwithOn
    global PlayerRoundOn

    global player1HP
    global player2HP
    global player3HP
    global player4HP
    global player5HP
    global player6HP

    s.clear()
    sense = SenseHat()

    while playerAmountOn == 1:

        for event in sense.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":

                # - - - - - Check which direction - - - - -
                # - - - - - Add Players - - - - -
                if event.direction == "up":
                    playerAmount += 1
                # - - - - - Remove Players - - - -
                elif event.direction == "down":
                    playerAmount -= 1
                # - - - - - Set Image and player amount - - - - -
                if playerAmount <= 2:
                    playerAmount = 2
                    images = [number_1]
                if playerAmount == 2:
                    images = [number_2]
                if playerAmount == 3:
                    images = [number_3]
                if playerAmount == 4:
                    images = [number_4]
                if playerAmount == 5:
                    images = [number_5]
                if playerAmount == 6:
                    images = [number_6]
                s.set_pixels(images[introCount % len(images)]())

                # - - - - - If player is over or lower than 6 - - - - -
                if playerAmount >= 6:
                    playerAmount = 6
                if playerAmount < 2:
                    playerAmount = 2

                # - - - - - Set Player HP - - - - -
                elif event.direction == "middle":
                    playerAmountOn = 0
                    if playerAmount==6:
                        player1HP = 6
                        player2HP = 6
                        player3HP = 6
                        player4HP = 6
                        player5HP = 6
                        player6HP = 6
                    elif playerAmount==5:
                        player1HP = 6
                        player2HP = 6
                        player3HP = 6
                        player4HP = 6
                        player5HP = 6
                    elif playerAmount==4:
                        player1HP = 6
                        player2HP = 6
                        player3HP = 6
                        player4HP = 6
                    elif playerAmount==3:
                        player1HP = 6
                        player2HP = 6
                        player3HP = 6
                    elif playerAmount==2:
                        player1HP = 6
                        player2HP = 6
                    # - - - - - Start Next Loop - - - - -
                    s.clear()
                    playerAmountOn=0
                    TurnSwithOn=0
                    PlayerRoundOn=1
#endregion

#region------------------------------------    UDP       -------------------------------------------------

def UDP():
    #dataToSendt
    global playerAmountOn
    global TurnSwithOn
    global PlayerRoundOn

    # 2 defult
    global playerAmount

    # Dices
    global UserChoiceTheDice
    global UserChoiceForDiceC
    global UserChoiceForDiceD

    # Turn
    global turn
    global LastPlayer

    # Intro Count
    global introCount

    # Player HP
    global player1HP
    global player2HP
    global player3HP
    global player4HP
    global player5HP
    global player6HP

    # Dices
    global Dice1
    global Dice2

    #Socket
    sense = SenseHat()
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    #Port
    BROADCAST_TO_PORT = 7000
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    #Data To Sendt
    data = str(turn)+" "+str(player1HP)+" "+str(player2HP)+" "+str(player3HP)+" "+str(player4HP)+" "+str(player5HP)+" "+str(player6HP)+" "+str(playerAmount)+" "+str(WhoWon) # <-------------------- Missing Who Won

    #Data To Sendt
    dataForPrint = "Turn: "+str(turn)+"    "+"Dice1: "+str(Dice1)+"    "+"Dice2: "+str(Dice2)+"    "+"UserChoiceForDiceC: "+str(UserChoiceForDiceC)+"    "+"UserChoiceForDiceD: "+str(UserChoiceForDiceD)+"    "+"player1HP: "+str(player1HP)+"    "+"player2HP: "+str(player2HP)+"    "+"player3HP: "+str(player3HP)+"    "+"player4HP: "+str(player4HP)+"    "+"player5HP: "+str(player5HP)+"    "+"player6HP: "+str(player6HP)+"    "+"PlayerAmount: "+str(playerAmount)


    #Sending Data
    s.sendto(bytes(data), ('<broadcast>', BROADCAST_TO_PORT))

    #Printing Data
    print(dataForPrint)
    print(data)

#endregion--------------------------------------------------------------------------------------------------------------

#region------------------------------------    WhoWon       -------------------------------------------------
def WhoWonDef():
    global player1HP
    global player2HP
    global player3HP
    global player4HP
    global player5HP
    global player6HP
    global WhoWon

    if   (player2HP==0 and player3HP==0 and player4HP==0 and player5HP==0 and player6HP==0):
        WhoWon=1
    elif (player3HP == 0 and player4HP == 0 and player5HP == 0 and player6HP == 0 and player1HP == 0):
        WhoWon = 2
    elif (player4HP == 0 and player5HP == 0 and player6HP == 0 and player1HP == 0 and player2HP == 0):
        WhoWon = 3
    elif (player5HP == 0 and player6HP == 0 and player1HP == 0 and player2HP == 0 and player3HP == 0):
        WhoWon = 4
    elif (player6HP == 0 and player1HP == 0 and player2HP == 0 and player3HP == 0 and player4HP == 0):
        WhoWon = 5
    elif (player1HP == 0 and player2HP == 0 and player3HP == 0 and player4HP == 0 and player5HP == 0):
         WhoWon = 6
    if WhoWon!=0:
        UDP()
        s.clear()
        exit()


#endregion

#region------------------------------------    The Game Def Router       -------------------------------------------------

def TheGame():
    #x = threading.Thread(target=UDP())
    #x.start()
    gameloob = 1
    while gameloob==1:
        global playerAmountOn
        global TurnSwithOn
        global PlayerRoundOn
        global playerAmountOn

        global firstTimeUdp

        if playerAmountOn==1:
            UDP()
            PlayerAmount()

        if PlayerRoundOn==1:
            UDP()
            PlayerRound()

        if TurnSwithOn==1:
            UDP()
            TurnSwith()

TheGame()
#endregion