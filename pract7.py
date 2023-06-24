from graphics import *
import time


def helloWhile():
    i = 0
    while i < 10:
        print("i is now", i)
        i = i + 1


def countDown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


def mysteryLoop():
    i = 1
    while i < 1000:
        print(i)
        i = i * 2

# Be careful! This loop will run forever!


def infiniteLoop():
    i = 0
    while i < 10:
        print(i)


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
