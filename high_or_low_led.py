#The Following is the same program as the High Or Low game written in Java.
#I rewrote this in Python when playing around with Raspberry Pi LED projects.

#import Libraries
import os
import time
import random
from gpiozero import LED


red = LED(18)
yellow = LED(23)
green = LED(24)

def red_flash(time_in):
    red.on()
    time.sleep(time_in)
    red.off()


def green_flash(time_in):
    green.on()
    time.sleep(time_in)
    green.off()

#LEDs on the Pi light up red or green depending on the guess given :)
def game_start():
    score = 0
    gameover = False
    num = random.randint(1, 12)
    while gameover == False:
        print(num)
        guess = input("Higher or Lower? h/l\n")
        temp = num
        num = random.randint(1, 12)
        print(num)
        if guess == "h" and temp <= num:
            score = score + 1
            green_flash(0.5)
        elif guess == "l" and temp >= num:
            score = score + 1
            green_flash(0.5)
        elif guess == "h" and temp > num:
            print("Incorrect! Game over!")
            red_flash(2)
            print("Score: " + str(score))
            gameover = True
        elif guess == "l" and temp < num:
            print("Incorrect! Game over!")
            red_flash(2)
            print("Score: " + str(score))
            gameover = True
        else:
            print("Input not recognised.")
    play_again = input("Would you like to play again? y/n")
    if play_again == "y":
        game_start()
    else:
        print("Goodbye!")

game_start()


