import pygame
import time
from constants import Constants

class Crash:

    def __init__(self, game, cars, char):
        self.game = game
        self.cars = cars
        self.char = char

    def isCrashed(self):
        for car in self.cars:
            if self.spansOverlap(car.span):
                # self.game.crashed = True
                # break
                self.message_display('Crashed')
    
    def spansOverlap(self, car_span):
        # If one rectangle is on left side of other 
        if(car_span[0].x > self.char.span[1].x or self.char.span[0].x > car_span[1].x): 
            return False

        # If one rectangle is above other 
        if(car_span[0].y < self.char.span[1].y or self.char.span[0].y < car_span[1].y): 
            return False
        return True
    
    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((Constants.WINDOW_WIDTH/2),(Constants.WINDOW_HEIGHT/2))
        self.game.game_display.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(0.1)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, Constants.BLACK)
        return textSurface, textSurface.get_rect()
    