import pygame as pyg
import setup


#initialize pygame

pyg.init()

# create screen
screen = pyg.display.set_mode((setup.width, setup.height))
pyg.display.set_cap("2Dgame")

# game loop
gameOn = True
while gameOn:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            gameOn = False