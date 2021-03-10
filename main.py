import pygame as pyg
import setup


#nastepny cel: dodac player, poruszanie, sprite 

#initialize pygame

pyg.init()

# create screen
screen = pyg.display.set_mode((setup.width, setup.height))
pyg.display.set_caption("2Dgame")
icon = pyg.image.load("IMG/icon.png")
pyg.display.set_icon(icon)

# game loop
gameOn = True
while gameOn:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            gameOn = False
    screen.fill((255, 0, 155))
    pyg.display.update()

