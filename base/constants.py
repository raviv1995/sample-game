import pygame
from PIL import Image
from vector import Vector

class Constants():
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    BLOCK_COLOR = (53,115,255)
    WINDOW_HEIGHT = 768
    WINDOW_WIDTH = 1024
    SMOOTHNESS_INDEX = 0.05

    @classmethod
    def makeImage(cls, images, convert=False):
        returnList = []
        for image in images:
            returnList.append(pygame.image.load(image))
        return returnList
    
    @classmethod
    def getCharacterSpan(cls, image, start):
        im = Image.open(image)
        width, height = im.size
        return [start, Vector(start.x+width, start.y-height)]