#A guessing game
import random
import time
from time import *
from random import *
dif = "1"
def start():
    print "Welcome to UberGuess!"
    sleep(0.2)
    print "In UberGuess, you guess random numbers."
    sleep(1)
    print "To get started, choose a difficulty, or put in T for the tutorial."
    global dif 
    dif = raw_input()
    sleep(0.5)
    if dif.lower() == "t":
        tut()
    print "Your difficulty has been set to",dif
    sleep(1)
    print ""
    print ""
    global rnd, skip, hint
    if dif == "sad":
        rnd = "ARE SAD"
        skip = "ARE SAD"
        hint = "ARE SAD"
    else:
        rnd = 1
        skip = 1
        hint = 3
    game()
def tut():
    print "Welcome to the tutorial!"
    sleep(0.5)
    print "In this tutorial, you will learn the basics of the game."
    sleep(1)
    print "To get started, I will choose a number."
    tunum = randint(1,5)
    sleep(0.5)
    print "To start off with, I will tell you the range of the number."
    sleep(0.5)
    print "The number is between 1 and 5."
    sleep(0.1)
    raw_input("Press enter to continue")
    print "Then you must guess what the number is. Try to find it!"
    sleep(0.5)
    tunumg = int(raw_input())
    sleep(0.3)
    if tunumg == tunum:
        print "You found the number!"
        sleep(0.5)
    else:
        print "That wasn't the number"
        sleep(0.5)
        print "The number was",tunum
        sleep(0.5)
    print "Now, onwards."
    sleep(0.5)
    print "You get 5 tries to guess the number."
    sleep(1)
    print "If you guess correctly, you get a hint."
    sleep(1)
    print "Hints are used to give a smaller range of numbers to guess from."
    sleep(2)
    print "You start with three hints."
    sleep(1)
    raw_input("Press enter to continue.")
    print "Every five times you guess correctly, you get a skip."
    sleep(2)
    print "Skips are used as extra lives, or to just skip a level."
    sleep(1)
    print "If you run out of tries, you can use a skip to go on."
    sleep(2)
    print "You can also type \"skip\" to go on to the next level."
    sleep(1)
    print "You start with one skip."
    sleep(1)
    raw_input("Press enter to continue.")
    print "That's all you need to know about the game!"
    sleep(3)
    print "Now, time to play!"
    start()
def game():
    global chances
    global randnum
    print "ROUND",rnd,"   HINTS",hint,"   SKIPS",skip
    if dif == "sad":
        randnum = "sad"
    else:
        randnum = randint(1,(int(dif) * 5))
    print ""
    print ""
    if dif == "sad":
        print "The number is between 1 and",dif
    else:
        print "The number is between 1 and",int(dif) * 5
    chances = 5
    guessing()
def guessing():
    guess = raw_input()
    if guess.lower() == "hint":
        hintnum1 = randnum - randint(1, (int(dif)*2))
        hintnum2 = randnum + randint(1, (int(dif)*2))
        sleep(0.5)
        print "The number is in between",hintnum1,"and",hintnum2
        hint = hint - 1
        guessing()
    if guess.lower() == "exit":
        print "Do you really want to quit?"
        if raw_input("Y/N").lower() == "y":
            start()
        else:
            guessing()
    elif guess == str(randnum) or guess.lower() == "skip" :
        sleep(0.5)
        print ""
        print "Correct!"
        if not dif == "sad":  
            hint = hint + 1
            if rnd == 5 or rnd == 10 or rnd == 15 or rnd == 20 or rnd == 25 or rnd == 30 or rnd == 35 or rnd == 40 or rnd == 45 or rnd == 50:
                skip = skip + 1
            rnd = rnd + 1
        print ""
        print ""
        raw_input("Press enter to continue")
        print ""
        print ""
        game()
    else:
        sleep(0.5)
        print "That isn't correct. Try again."
        global chances
        chances = chances-1
        if chances == 0:
            sleep(1)
            print "You have run out of chances. Use a skip to go to next round? Y/N"
            if raw_input().lower() == "y" and skip > 0:
                global skip, hint, rnd
                skip = skip - 1
                hint = hint + 1
                rnd = rnd + 1
                print ""
                print ""
                print "The number was",str(randnum)
                print ""
                print ""
                raw_input("Press enter to continue.")
                game()
            else:
                sleep(0.5)
                print "You lose!"
                sleep(3)
                start()
        else:
            guessing()
        
start()
    
