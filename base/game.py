import pygame
import time
import os
from constants import Constants
from vector import Vector
from character import Character
from oppenent import Cars
from interaction import Crash

pygame.init()
    
class Game:
    """
    The main game class.

    variables:
        height - The window's height
        width - The window's width
        game_display - The game's window
        clock - The game's clock
    
    functions:
        updateDisplay - Update the window
        main - The game's loop
    """
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.game_display = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.crashed = False
        # self.game_display.fill(Constants.WHITE)
        pygame.display.set_caption('Test Game')
    
    def updateDisplay(self):
        pygame.display.update()
    
    def main(self):
        testChar = Character(self, (self.width*0.3), (self.height*0.65))
        testCar = Cars(self, 0, 0)
        exited = False
        interaction = Crash(self, [testCar], testChar)

        while not exited:

            self.game_display.fill(Constants.WHITE)
            testCar.makeChar()
            # Get all the keys that are pressed
            keys = pygame.key.get_pressed()
            player_movement = Vector(0,0)
            car_movement = Vector(0,0)

            if 1 in keys:
                if keys[pygame.K_LEFT]:
                    player_movement.x += -5
                elif keys[pygame.K_RIGHT]:
                    player_movement.x += 5
                if keys[pygame.K_UP]:
                    car_movement.y += 5
                elif keys[pygame.K_DOWN]:
                    car_movement.y += -5

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exited = True

                # Event : keys when down pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Exit the game
                        exited = True
                        break

                    if event.key == pygame.K_LEFT:
                        player_movement.x += -5
                    elif event.key == pygame.K_RIGHT:
                        player_movement.x += 5
                    elif event.key == pygame.K_UP:
                        car_movement.y += 5
                    elif event.key == pygame.K_DOWN:
                        car_movement.y += -5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        pass
                else: # No event, run the static animation
                    pass
            
            if player_movement.__ne__(Vector(0, 0)):
                testChar.walk(player_movement)
            else:
                testChar.makeChar()
            if car_movement.__ne__(Vector(0, 0)):
                testCar.walk(car_movement)
            
            interaction.isCrashed()

            self.clock.tick(60)
            self.updateDisplay()

if __name__ == '__main__':
    game = Game(Constants.WINDOW_HEIGHT, Constants.WINDOW_WIDTH)
    game.main()
