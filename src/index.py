'''Main module'''
from konelaskin import Konelaskin

class Index:
    '''This class is used for running the program'''
    def __init__(self):
        self.konelaskin = Konelaskin()

    def mainloop(self):
        '''Initiates the main loop'''

        while True:
            self.konelaskin.handle_events()

if __name__== "__main__":
    index = Index()
    index.mainloop()
