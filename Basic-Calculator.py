# This is my First Program Learn About Python
# This Program Help you to Calculate Addition & Multiplication
# by Cosmas | © May 2022 | Version 1, 5/5/22

import sys


def welcomeNickname(a):
    print("Yay ! Welcome", a)
    print("So, Now You can Input 2 Number and Select")
    print("Operation You Want it")
    print("Got it ? Let's Start !")


def askForInput(a, b):
    number1 = input("Please Input Any Number : ")
    number2 = input("Please Input Any Number : ")
    return number1, number2


def callingUI():
    # BasicUI
    uI1 = "*************"
    uI2 = "*** Basic Calculator ***"
    uI3 = "*** Program ***"
    uI4 = "by Cosmas"
    print(uI1.center(30))
    print(uI2.center(30))
    print(uI3.center(30))
    print(uI4.center(30))
    print("")

def praOps():
    # BasicUI
    p1 = "Now, Please Choose Operation Your Want"
    p2 = "There are Only 2 Ops, Addition & Multiplication"
    print(p1.center(30))
    print(p2.center(30))
    print("")

def Addition(results):

def Multiplication(results):


# Declaration
yNumberOne = int()
yNumberTwo = int()

# Main Program
yourName = input("Please Input Your Nickname : ")

# No Number Please
while yourName.isdigit():
    print("Your Nickname Can't Contains any Number")
    yourName = input("Please Input Your Real Nickname : ")

callingUI()
welcomeNickname(yourName)
askForInput(yNumberOne, yNumberTwo)
praOps()


chooseOps = input("Please, Choose The Function Your Want : ")
print("1. Addition")
print("2. Multiplication")
print()
print("Okay, This is The Result!")

if chooseOps == 1:
    Addition(results)
elif chooseOps == 2:
    Multiplication(results)
#else:
    #while choose0ps <=2 && >=1:


