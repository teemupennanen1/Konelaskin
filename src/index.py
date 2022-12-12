'''Main module'''
from ui.main import Konelaskin

class Index:
    '''This class is used for running the program'''
    def __init__(self):
        '''Initializes the program'''
        self.konelaskin = Konelaskin()

    def mainloop(self):
        '''Initiates the main loop'''
        while True:
            self.konelaskin.handle_events()
            break

if __name__== "__main__":
    index = Index()
    index.mainloop()
