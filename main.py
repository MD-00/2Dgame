import pygame as pyg
import setup


<<<<<<< Updated upstream



=======
>>>>>>> Stashed changes
#initialize pygame

pyg.init()

# create screen
<<<<<<< Updated upstream
screen = pyg.display.set_mode((800,600))
while True:
    pass
=======
screen = pyg.display.set_mode((setup.width, setup.height))

gameOn = True
while gameOn:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            gameOn = False


>>>>>>> Stashed changes
