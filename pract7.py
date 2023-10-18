from graphics import *


def countDown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


# Note: msg == "" needs to appear twice here
def getString1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def getString2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def addUpNumbers1():
    total = 0
    more = "y"
    while more == "y":  # The loop runs while `more` is "y"
        number = int(input("Enter a number "))
        total = total + number
        more = input("Any more numbers? ")
    print("The total is", total)


def addUpNumbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:  # The loop runs while `number` is not 0
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def addUpNumbers3():
    total = 0
    nStr = input("Number (hit enter to stop): ")
    while nStr != "":  # The loop runs while `nStr` is not empty
        number = int(nStr)  # Assumes that `nStr` contains a number
        total = total + number
        nStr = input("Number (hit enter to stop): ")
    print("The total is", total)


def addUpNumbers4():
    total = 0
    while True:  # The loop runs until we break it
        nStr = input("Number (anything else to stop): ")
        if not nStr.isdigit():
            break  # Break the loop if `nStr` is not a number
        number = int(nStr)
        total = total + number
    print("The total is", total)


# For exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        pass
        # remove the pass and add your code here


# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32
