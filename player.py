# -*-coding:Latin-1 -*
import os

numberP = 0
amountP = 1000


def enterNumber():
    while True:

        inputUser = input("Enter a number between 0 and 49 \n")

        try:
            numberP = int(inputUser)
            if numberP >= 50 or numberP < 0:
                print("The number entered is not in the correct intervalle\n")
                continue
            else:
                return numberP

        except ValueError:
            print("Your input is not a correct number\n")


def enterAmount():
    while True:
        print("Available Amount ", amountP, "Dollars\n")
        inputUser = input("Enter the Amount\n")

        try:
            amountUser = int(inputUser)
            if amountUser > amountP:
                print("You don't have enough Money to bet this amount\n")
                continue
            else:
                return amountUser

        except ValueError:
            print("The number you entered is not valid\n")


def getPlayerColor(number):
    if number % 2 == 0:
        colorP = True
    else:
        colorP = False

    return colorP


def getCurrentAmount():
    return amountP


def setCurrentAmount(amount):
    global amountP
    amountP += amount


# test des functions de getPlayerColor
if __name__ == '__main__':
    enterNumber()
    enterAmount()
    # print(getPlayerColor(number))
    print(amountP)
    os.system("pause")
