import pygame
from konelaskin import Konelaskin

'''Importing the module for handling calculations'''
class Index:
    def __init__(self):
        self.konelaskin = Konelaskin()

    def mainloop(self):
        '''Initiates the main loop'''
    
        while True:
            self.konelaskin.handle_events()

if __name__== "__main__":
    index = Index()
    index.mainloop()
