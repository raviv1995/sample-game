import os
import pygame
import time
from vector import Vector
from constants import Constants

class Cars:
    """
    This class is the base class for 
    the cars that are spawned randomly
    This create the road and the cars 
    on them. For now I've using 
    a static image
    """

    def __init__(self, game, x, y):
        self.game = game
        self.position = Vector(x,y)
        # Static images needed
        self.static_images = [os.path.join('..','assets','car.png')]
        self.static_images_loaded = Constants.makeImage(self.static_images)
        # Walk cycle needed
        self.walk_images = [os.path.join('..','assets','car.png')]
        self.walk_images_loaded = Constants.makeImage(self.walk_images)
        self.span = Constants.getCharacterSpan(self.static_images[0], self.position)
    
    def makeChar(self):
        for image in self.static_images_loaded:
            self.game.game_display.blit(image, self.position.get_p())
            self.game.updateDisplay()
            # A delay would be needed when images are used
            # This is sort of the smoothness index 
            # (Hence the name)
            # time.sleep(Constants.SMOOTHNESS_INDEX)

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
            # time.sleep(Constants.SMOOTHNESS_INDEX)