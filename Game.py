# -*-coding:Latin-1 -*
import os
from player import *
from roulette import *


def play():
    os.system('cls')
    print("-----PLAY------\n")
    global amountP
    rouletteNumber = getRouletteNumber()
    rouletteColor = getRouletteColor(rouletteNumber)

    print("----THE ROULETTE ALREADY CHOOSED HIS NUMBER----\n")
    playerNumber = enterNumber()
    playerColor = getPlayerColor(playerNumber)
    playerAmount = enterAmount()
    setCurrentAmount(-playerAmount)

    print("----PRESS ANY KEY TO SEE THE RESULT----\n")
    os.system("pause")
    os.system('cls')

    if rouletteNumber == playerNumber:
        playerAmount *= 3
        print("Congratulations!!! you guessed the correct Number\n: you won ", playerAmount, " Dollars\n")
    elif rouletteColor == playerColor:
        playerAmount /= 2
        print("You could not guess the correct number but you picked up the right color.\n")
        print("We will give you ", playerAmount, " dollars from the Amount you put for the Game\n")
    else:
        playerAmount = 0
        print("You couldn't guess the number and the winning color is wrong\n")

    setCurrentAmount(playerAmount)
    amountP = getCurrentAmount()
    print("Roulette Number was: ", rouletteNumber, "\n")
    print("Player Number was: ", playerNumber, "\n")
    print("Amount Available : ", amountP, "\n")


while True:
    play()
    inputUser = input("Enter \"exit\" to exit and any key to continue: ")
    if inputUser == "exit" or getCurrentAmount() <= 0:
        break

print("----GAME OVER-----\n")
os.system("pause")
