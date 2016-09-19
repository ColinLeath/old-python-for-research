"""
This module should load a sequence of images in a directory and display them continuously. Until a key is pressed.
"""

#Import Modules
import os, sys
import pygame, pygame.sprite, pygame.transform, pygame.image
from pygame.locals import *

IMAGEDIR=r'C:\_research_cleath\Documents-By-Date-and-Study\2002-09-30-Animation-project\images'
TRUE = 1 #true is any nonzero value...
FALSE = 0

class Animation:
    "an interface for animating."
    #conventions '_' precedes names of functions intended to be private (only called from other functions within the class)
    #verbs for methods and nouns for data attributes
   
    def __init__(self, screen=None): #only runs if class instance is created
        self.screen             = None #this is the handle/reference to the display
        self.imagedir           = 'x:\\' #usually set by sessionman.py or by loading saved session.  
        self.fullscreen         = TRUE 
        self.frames_per_second   = 5 #used to control rotation speed of pointer. The repeat rate above (if set to 1ms) has no effect, as this setting limits the speed.
        self.clock = pygame.time.Clock() #initialize clock used for controlling framerate
        self.repeatrate          = 1  #milliseconds. if a key (e.g. arrow key is held down a new keypress will register every 1 ms)
 
    def initio(self):
        "Initialize Everything--only needs to be done once if running multiple sessions."
        pygame.init()
        #self.START_RES = (1024,768)
        #self.START_RES = (800,600)
        self.START_RES = (640,480)
        #self.START_RES = (320,240)
        if self.fullscreen:
            self.screen = pygame.display.set_mode(self.START_RES, FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.START_RES)
        pygame.display.set_caption('pretty picture')
        pygame.mouse.set_visible(0) #mouse will not appear in display window
        #pygame.event.set_blocked(MOUSEMOTION)
        pygame.event.set_allowed(KEYDOWN) #only KEYDOWN events will be used.
        pygame.key.set_repeat(500,self.repeatrate)
        
        #self.allsprites = pygame.sprite.RenderUpdates((self.pointer))

    def _initimagelist(self):
        "Create list of images:"
        self.imagelist = os.listdir(self.imagedir)
        #remove directories from list:
        def filesOnly(x): return os.path.isfile(os.path.join(self.imagedir,x))
        self.imagelist = filter(filesOnly, self.imagelist)
        self.imagelist.sort() 
        self.imagelist = self.imagelist[15:]
        self.listlen = len(self.imagelist)

    def convertImages(self):
        import Image
        desiredFormat = 'BMP'
        outdir = os.path.join(self.imagedir,'new')
        if os.path.isdir(outdir):
            print outdir + ' exists'
        else:
            try:
                os.mkdir(outdir)
            except: 
                print 'failed to create ' + outdir 

        options = { }
        for imageName in self.imagelist[3:]:
            imagePath = os.path.join(self.imagedir,imageName)
            im = Image.open(imagePath)
        #    im = im.resize((640,480))
            #if im.mode != desiredFormat:
            #    im.draft(desiredFormat, im.size)
            #    im = im.convert(desiredFormat)
            #if format:
            apply(im.save, (os.path.join(outdir, imageName[:-3] + desiredFormat.lower()), desiredFormat), options)
            #else:
            #    apply(im.save, (argv[1],), options)

        
    def run(self):
        "run animation"
        #for n in range(6):
        while 1:
            for image in self.imagelist:
                #Display The Background -- load images
                img, rect = load_image(os.path.join(self.imagedir,image))
                img = pygame.transform.flip(img, 0,1)
                self.screen.blit(img, rect)
                pygame.display.flip()
         #       self.clock.tick(self.frames_per_second)
            self.imagelist.reverse()
             
       
# following function and class are used for the displaying of the pointer
#functions to create our resources
def load_image(name, colorkey=None):
    #fullname = os.path.join('c:\\program files\\pygame-docs\\examples\\data', name)
    fullname=name
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    #Initialize Everything
    #this calls the 'main' function when this script is executed
    s = Animation()
    s.initio()
    #s.imagedir = IMAGEDIR
    #s.imagedir = r'C:\_research_cleath\Documents-By-Date-and-Study\2002-09-30-Animation-project\images\bmpSmall'
    #s.imagedir = r'X:\test_label_bug\bmpLarge'
    s.imagedir = r'X:\test_label_bug\bmpSmall'
    s._initimagelist()
    #s.convertImages()
    s.run()
   
if __name__ == '__main__': main()
