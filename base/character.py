import os
import pygame
import time
from vector import Vector
from constants import Constants


class Character:
    """
    This class is used to build the main
    character of the game. 

    variables:
        game - The game context
        position - The player's vector
        span - Four points that describe 
            the area the player covers
        static_images - The player's 
            movement cycle when
            stationary.
        walk_images - The player's
            movement cycle when 
            walking
    
    functions:
        makeChar - Function to spawn 
            the character's standing
            motion.
        walk - Function to invoke the
            character's walk cycle
    """

    def __init__(self, game, x, y):
        self.game = game
        self.position = Vector(x,y)
        # Static images needed
        self.static_images = [os.path.join('..','assets','char.png')]
        self.static_images_loaded = Constants.makeImage(self.static_images)
        # Walk cycle needed
        self.walk_images = [os.path.join('..','assets','char.png')]
        self.walk_images_loaded = Constants.makeImage(self.walk_images)
        self.span = Constants.getCharacterSpan(self.static_images[0], self.position)
    
    def makeChar(self):
        for image in self.static_images_loaded:
            self.game.game_display.blit(image, self.position.get_p())
            self.game.updateDisplay()

            # A delay would be needed when images are used
            # This is sort of the smoothness index 
            # (Hence the name)
            time.sleep(Constants.SMOOTHNESS_INDEX)

    def walk(self, delta):
        for image in self.walk_images_loaded:
            if (self.position.x + delta.x > 0) : self.position.x = self.position.x + delta.x
            if (self.position.y + delta.y > 0) : self.position.y = self.position.y + delta.y
            self.game.game_display.blit(image, self.position.get_p())
            self.game.updateDisplay()
            self.span = Constants.getCharacterSpan(self.static_images[0], self.position)
            # A delay would be needed when images are used
            # This is sort of the smoothness index 
            # (Hence the name)
            # Also it makes sense to have two variables for this
            time.sleep(Constants.SMOOTHNESS_INDEX)