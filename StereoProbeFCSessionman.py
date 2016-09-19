from StereoSession import Session
TRUE = 1
FALSE = 0


#I think I'm missing something. Here are the imports from the stereosession module. why do I need to do them here?

#Import Modules
import os, sys
import pygame, pygame.sprite, pygame.transform, pygame.image
from pygame.locals import *
import inputbox #refers to inputbox.py which should be in same directory
import time
import string
import winsound
import textrect #refers to textrect.py which should be in same directory
import pickle
import re
import random
import shutil
#import calcspinnerpos

#2002-10-31-1240 import Image PIL used to create overunder images (the pointer)
#import Image

#definitions of variables (used as constants) to make script more readable
DATAPATH = '' #directory where pointer.bmp and data.csv are stored(?) e.g.:
#DATAPATH = 'c:\\program files\\pygame-docs\\examples\\data'
CLOCKWISE = 0
COUNTERCLOCKWISE = 1
NOCHANGE = -1
FLIP = 3

TRUE = 1 #true is any nonzero value...
FALSE = 0
MYQUIT = -99

MAXDEGREES = 360

#looks like every def outside of the class def has to be duplicated here.

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

class resumedata:
    "for pickling data used to resume, needs to be on top level of module"
    list = []
    n = -1
    label = ''
    imagedir = ''
    sessionlist =[]
    sessiontype = '' #currently could be FC (forced choice) or iso (isotropic)
    #any other data needed?


class probeTrial:
    "for packaging trial information for probe study"
    bg = FALSE
    offset = 0

################end dup imports/defines from stereosession.py

class probeFcSession(Session):
    """subclass StereoSession.Session so we can make necessary changes
    should be very cool
    I haven't done this before, at work at least. subclassing.
    What needs to change from the default session?
    Probably only run()
    different key effects. 
    No pointer is used.
    and writing data will be different.
    so, let's remove the pointer init code
    and modify run.

    both k_left and k_right need to save answer and advance.
    need sep save and advance function.
    """
    def _initimagelist(self):
        "Create randomized list of parameters to be used by drawscreen function in creating displays."
        ###self.imagelist = os.listdir(self.dimagedir)
        self.imagelist =[] 
        ####remove directories from list!! damn I think this is the second time I did this!
        ###def myisfile(filename): return os.path.isfile(os.path.join(self.dimagedir,filename))
        ###self.imagelist = filter(myisfile, self.imagelist)
        ####print len(self.imagelist)
        

        # a list of tuples? a list of structs/classes?
        #need to have means of setting session characteristics-- number of trials, number w/bg, offsets.
        #then create list with desired prop and number of elements and randomize it
        #then create elements in order and in order add to "imagelist"
        #numberoftrials.
        #we should create elements in order then randomize list
        #like in 3ds:
        numberOfReps = 40 #how many times must a participant run through the basic sequence, before we will let her be done?
        listBg = [TRUE,FALSE]
        #listOffsets = [-10,-8,-6,-4,-2,0,2,4,6,8,10]
        listOffsets = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
        for rep in range(numberOfReps):
            for bg in listBg:
                for offset in listOffsets:
                    newTrial = probeTrial()
                    newTrial.bg = bg
                    newTrial.offset = offset
                    self.imagelist.append(newTrial)
        
        if self.sortlist:
            self.imagelist.sort()
        else:
            random.shuffle(self.imagelist)
        ###if self.dlabel == 'practice': #practice session should be 120 randomly selected images from main imagedir
        ###    #for practice session, should pass in same directory as run1, run2, but it will be handled differently here.
        ###    self.imagelist = self.imagelist[:120] #if list is less than or =120, returns entire list
        if self.numberoftrials <> 99999: #this allows for reducing the number of trials, like for practice sessions.
            self.imagelist = self.imagelist[:self.numberoftrials]
            self.numberoftrials = 99999 #should be using a constant here.

            
        self.listlen = len(self.imagelist)


    def _showcalibrationscreen(self, showtext=FALSE):
        """displays calibration screen until <<enter>> is pressed
        in this study, the c-screen needs a red center and a blue border/band
        around the displayable extent of the monitor.
        we will say: adjust to see all of the red, none of the blue.
        """
        maxX, maxY = self.START_RES
        bandWidth = 10
        blue = (0,0,255)
        red = (112,0,0)
        brightred = (255,0,0)
        green = (0,255,0)
        centerRE = (maxX/2),(maxY/2-35)/2
        centerLE = centerRE[0],centerRE[1]+(maxY/2 + 35)
        #why not fill with blue, draw red on.?
        #put the red on-- using avg of vals in _drawBackground()
        self.dscreen.fill(brightred)  #2003-01-24-1101 now fill with red, the average of the two check values.
        #draw bands, over-under.
        
        yExtent = (maxY/2)-35
        #need overunder display.
        #draw on surface.
        #draw surface on screen 2x
        #also draw crosshairs 2x (long, narrow rects)
        myHorizCrossHair = pygame.Rect(0,0,maxX,1)
        myVertCrossHair = pygame.Rect(0,0,1,yExtent)
        
        #init rects and get them the right size.        
        
        #rflist=[.04,.1,.12,.14] #reductionfactor
        rflist=[.04,.1,.12] #reductionfactor
        #colorlist=[green,red,blue,red]
        colorlist=[green,red,blue]
        
        def returnScaledCenteredColoredRect(reductionFactor,color): 
            myrect = pygame.Rect(0,0,maxX*(1-reductionFactor),yExtent*(1-reductionFactor))
            myrect.center = centerRE
            return(color,myrect)
        
        rectlist = map(returnScaledCenteredColoredRect,rflist,colorlist)
        
        myHorizCrossHair.topleft = 0,yExtent/2-1
        myVertCrossHair.topleft = maxX/2-1,0
        
        for rect in rectlist:
            self.dscreen.fill(rect[0],rect[1])
        self.dscreen.fill((0,0,0),myHorizCrossHair)
        self.dscreen.fill((0,0,0),myVertCrossHair)

        
        for rect in rectlist:
            rect[1].center = centerLE
            
        myHorizCrossHair.topleft = 0,yExtent/2-1
        myHorizCrossHair.move_ip(0,maxY/2 + 35)
        myVertCrossHair.move_ip(0,maxY/2 + 35)

        for rect in rectlist:
            self.dscreen.fill(rect[0],rect[1])
            
        self.dscreen.fill((0,0,0),myHorizCrossHair)
        self.dscreen.fill((0,0,0),myVertCrossHair)


        if showtext:
            my_string = 'Adjust your position so you can see all of the blue ring and none of the red ring.\n\nPress [enter] to continue.' 
            self._displayMessage(width=300,height=125,yPos=325,displayString=my_string,textColor=(216,216,216))
        else:
            pygame.display.update()
 
        pygame.event.get()  #clear event queue, otherwise, was taking a long time and multiple enters could be pressed, bypassing calibration screen.
        while 1:
            event = pygame.event.wait()
            if (event.type == KEYDOWN) and (event.key == K_RETURN): 
                break

    def _drawBackground(self):
        checkSide = 40
        checkColor1 = (96,0,0)
        checkColor2 = (128,0,0)
        maxX, maxY = self.START_RES
        yExtent = (maxY/2)-35
        #need overunder display.
        #draw on surface.
        #draw surface on screen 2x
        mySurface = pygame.Surface((maxX,yExtent))
        for x in range(0,maxX,checkSide):
            for y in range(0,yExtent,checkSide/2):
                mySurface.fill(random.choice([checkColor1,checkColor2]),[x,y,checkSide,checkSide/2])

        self.dscreen.blit(mySurface,(0,0))
        self.dscreen.blit(mySurface,(0,maxY/2+35))
    
    def _drawScreen(self,myTrial):
        #blank the screen, albeit briefly, between trials.
        self.dscreen.fill((0,0,0)) #screen is a surface! 
        pygame.display.flip()
        pygame.time.delay(500) #should be 50 milliseconds- hal wanted blank to last half a sec.
        #handle drawing of background.
        #same thing done both times to ensure even timing.
        if myTrial.bg:
            self.dscreen.fill((112,0,0))  #2003-01-24-1101 now fill with red, the average of the two check values.
            self._drawBackground()
        else:
            self._drawBackground()
            self.dscreen.fill((112,0,0))  #2003-01-24-1101 now fill with red, the average of the two check values.
        initialDisparity = 7 #(in Pixels) the starting disparity of the probes. This should position one of the probes, currently the left, in front of the surface, such that the max offset of the other probe never takes it behind the BG surface.
        #initialDisparity = 40 #(in Pixels) the starting disparity of the probes. This should position one of the probes, currently the left, in front of the surface, such that the max offset of the other probe never takes it behind the BG surface.
        
        disparity = myTrial.offset
        
        #xpos,ypos is the top left corner.
        #let's choose a center point and have offsets from that point
        #we're having to deal with the center -- hal's numbers have the probe as point
        #there are pygame functions that let you use center, but, for now.
        #
        #left probe center:
        #leftProbeCenterXpos = 655
        leftProbeCenterXpos = 800 - 535 #hal is using center of screen as center of coord system
        #not yet sure what the following val should be.
        #leftProbeCenterYpos = 277
        leftProbeCenterYpos = 270
        #right probe center:
        #rightProbeCenterXpos = leftProbeCenterXpos + (138*2)#138 is the IPD and distance between cameras
        rightProbeCenterXpos = 800 + 535#138 is the IPD and distance between cameras
        rightProbeCenterYpos = leftProbeCenterYpos
                
        ################draw left probe##############
        #draw right eye left probe r.e. is the top half
        probeColor = (255,0,0)
        width,height = 8,4
        xpos = leftProbeCenterXpos - initialDisparity 
        ypos = leftProbeCenterYpos
        #must sub width and height from xpos,ypos since we're giving upper left corner of square
        #let's try using pygame.Rect() and then set rect.center, and then pass that in.
        probeRect = pygame.Rect(0,0,width,height)
        probeRect.center = xpos,ypos
        self.dscreen.fill(probeColor,probeRect)
        #left eye
        xpos = leftProbeCenterXpos + initialDisparity
        ypos = ypos+635
        probeRect.center = xpos,ypos
        self.dscreen.fill(probeColor,probeRect)
        
        ################draw right probe################
        #draw right eye left probe r.e. is the top half
        #we're never moving the r.e.r probe.
        #xpos = rightProbeCenterXpos - (disparity + initialDisparity)
        xpos = rightProbeCenterXpos - initialDisparity
        ypos = rightProbeCenterYpos
        probeRect.center = xpos,ypos
        self.dscreen.fill(probeColor,probeRect)
        
        #left eye
        xpos = rightProbeCenterXpos + (disparity + initialDisparity)
        ypos = ypos+635
        probeRect.center = xpos,ypos
        self.dscreen.fill(probeColor,probeRect)

        pygame.display.flip()
        
    def saveAndAdvance(self,closer):
        #write data for trial and load next image in list
        if self.dsound: 
             winsound.Beep(2000,150)

        date = time.ctime()
        ttime = date[11:19]
        date = date[:11] + date[-4:]
        #current filename format:
        #probeFC_003_-005o_OverUnder.png
        #filename=self.imagelist[self.n]
        #filename="null"
        #try:
        #offsetpos = string.find(filename,'o_O')
        #offset = float(filename[offsetpos-5:offsetpos])
        offset = self.imagelist[self.n].offset
        #currently 20 repeats per offset. Which one is it?
        #offsetImageIdpos = string.find(filename,'_') + 1
        #offsetImageId = int(filename[offsetImageIdpos:offsetImageIdpos+3])
        #offsetImageId = "null"
        background = self.imagelist[self.n].bg
        #except:
        #    print 'cantparsefilename'
        #    offset=-99 
        #    background = FALSE
        #    offsetImageId = -99
        #    
        #we're going to convert closer to binary for now.
        # 0 =  L
        # 1 = R
        if closer == 'L':
            binCloser = 0
        else:
            binCloser = 1
            
        #self.datafile.write('%s,%s,%s,%s,%d,%d,%d,%s\n' % (self.dparticipantname,self.dlabel,date,ttime,self.n,offset,background,closer))
        self.datafile.write('%s,%s,%s,%s,%d,%d,%d,%d\n' % (self.dparticipantname,self.dlabel,date,ttime,self.n,offset,background,binCloser))

        self.n += 1
        if self.n < self.listlen:
            #then load new image, but display intermission screen if blocksize multiple has been reached.
            #print 'n=%d %d mod %d = %d'%(n,n,self.dtrialblocksize,(n+1)%self.dtrialblocksize)#prb: n is 0 based index..
            #if not self.test and (self.n)%self.dtrialblocksize==0: #if remainder of n/trialblocksize is 0 then intermission time:
            if (self.n)%self.dtrialblocksize==0: #if remainder of n/trialblocksize is 0 then intermission time: #we want to test intermission screens.
                if self._showintermissionscreen() == MYQUIT:
                    return MYQUIT #note--do not need to return MYQUIT because self.dcompleted is false
                            #the MYQUIT FLAG was added later...
                self._showcalibrationscreen()
                
            if not self.test:
                self._drawScreen(self.imagelist[self.n])
            else:
                print self.n
        else:
            #it's time to continue on to next directory of files.
            self.datafile.close()
            self.dcompleted = TRUE
            self.dresumed = FALSE #reset this otherwise n read from pickled data will continue to be used

            if self._showintermissionscreen() == MYQUIT:
                return MYQUIT
            else: return

    def initio(self):
        "Initialize Everything--only needs to be done once if running multiple sessions."
        pygame.init()
        self.START_RES = (1600,1200)
        if self.dfullscreen:
            self.dscreen = pygame.display.set_mode(self.START_RES, FULLSCREEN)
        else:
            self.dscreen = pygame.display.set_mode(self.START_RES)
        pygame.display.set_caption('pretty picture')
        pygame.mouse.set_visible(0) #mouse will not appear in display window
        #pygame.event.set_blocked(MOUSEMOTION)
        pygame.event.set_allowed(KEYDOWN) #only KEYDOWN events will be used.
        #pygame.key.set_repeat(500,self.repeatrate)
        pygame.key.set_repeat() #passing in no arguments disables keyboard repeat. (for probeFC study keyboard repeat is not needed.)
        #set default fontsize
        self.fontSize = 40
        self.font = pygame.font.Font(None, self.fontSize)
        
    def run(self): 
        "manage running of session here"
        self.dcompleted = FALSE #reset this attribute
        #init imagelist
        if not self.dresumed:
            self._initimagelist()
            self.n = 0  #init counter
        elif self.n == self.listlen: #should only occur if self.dresumed 
            #handle case where participant saved data and quit at very end of session.
            self.dcompleted = TRUE
            self.dresumed = FALSE #reset this otherwise n read from pickled data will continue to be used
            return  #exit function

        print "self.n, %d"%self.n
        self._showcalibrationscreen()
        #Display The Background -- load first image
        self._drawScreen(self.imagelist[self.n])
        #initialize datafile:
        self.datafile = open(self.ddatafilename,'a')
        if os.path.getsize(self.ddatafilename)==0:
            #this is an empty file, add header row
            header = 'name,sessionlabel,datetime,n,offset,BackGround,closer\n'
            self.datafile.write(header)
        #Main Loop
        while 1:
            if self.test:
                #set event = to an <<enter>> keypress. and set pointer position to random value.
                event = pygame.event.Event(KEYDOWN, {'key': K_LEFT, 'unicode': u'\r', 'mod': 4096})
                pass
            else:
                event = pygame.event.wait()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   #quit and save data
                   self._savedata()
                   return 
                elif event.key == K_LEFT:
                    if self.saveAndAdvance("L") == MYQUIT:
                        return MYQUIT
                    if self.dcompleted:
                        return
                elif event.key == K_RIGHT:
                    if self.saveAndAdvance("R") == MYQUIT:
                        return MYQUIT
                    if self.dcompleted:
                        return
                elif event.key == K_q:
                    self.dsound = not(self.dsound)
                elif event.key == K_TAB:
                    #display position in imagelist in upper left of screen
                    fontobject = pygame.font.Font(None,18)
                    try:
                        showInfo = not showInfo
                    except:
                        showInfo = TRUE
                        
                    displaystring = '%s %d of %d'%(self.imagelist[self.n], self.n, len(self.imagelist))
                    x,y = 300,200 
                    if showInfo:
                        #draw in white
                        self.dscreen.blit(fontobject.render(displaystring, 1, (255,255,255)), (x, y))
                    else:
                        #redraw in black
                        self.dscreen.blit(fontobject.render(displaystring, 1, (0,0,0)), (x,y))
                    pygame.display.flip()

    
                elif event.key == K_SPACE:
                    #go back one image:
                    if self.n >= 1:
                        self.n -= 1
                        self._drawScreen(self.imagelist[self.n])


global s     #for pointing to instance of session class.
#global SESSIONLIST  #the list of labels (I was calling them sessions) which will constitute the entire experience of one participant (one session).
s = probeFcSession() #create an instance of the Session class.
#s.dfullscreen=FALSE
s.initio()  #initialize i/o
#SESSIONLIST = ['isopractice','linepractice','practice','run1','run2'] 
SESSIONLIST = ['practice','practice2','probeFC'] 
VARSESSIONLIST = ['variant']
#note: possible sessiontypes should all be lowercase
#s.possibleSessionTypes = ['probefc','var'] #possible sessiontypes should all be lower case
s.possibleSessionTypes = ['probefc'] #possible sessiontypes should all be lower case


#define constants to make reading code easier.
QUIT = 0
BEGIN = 1
FIRSTTIME = 2
FALSE = 0
TRUE = 1
MYQUIT = -99

def setPerSessionValues():
    #set session attributes particular to a given session label here.
    #set defaults:
    s.dtrialblocksize = 110 
    s.numberoftrials = 99999 # this is bad but I think necessary for now. (the code that resets it to this value is only called when imagelist is initted) . Setting it to this high number basically means that all trials will be used (as opposed to say 60 from a directory of 480)
    s.dintermissiondelay = 90 #seconds
    #in this case, the directory containing the images matches the label.
    #s.dimagedir = 'x:\\' + s.dlabel
    #s.dimagedir = r'c:\_temp\\' + s.dlabel
    #s.dimagedir = r'D:\_Shared_Images\_old\_Aperture\2002-06-06-Study-1-lines\final\\'
    #s.dimagedir = r'x:\_old\_Aperture\2002-10-01-Stereo-Study\images\\'
    #s.test = TRUE
    #s.dsound = FALSE
    if s.dlabel == 'practice': s.numberoftrials = 20  #how long do we want our practice session to be?
    if s.dlabel == 'practice2': s.numberoftrials = 110  #one block will be practice.
    #images are script-generated in probefc. the following line is irrelevant.
    s.dimagedir = r'x:\_old\_Aperture\2002-10-01-Stereo-Study\\' + s.dlabel
    #s.sortlist = TRUE

def continuex(labellist): 
    """
    Use this function to specify handling of different sessions(er, directories of images), based on the labels specified in SESSIONLIST. Note that some funky handling occurs in _showintermissionscreen() of the session class based on whether the session label is 'practice,' 'run1,' or 'run2.'
    This function is called recursively, returning nothing if labellist is empty.
    """
    if labellist ==['']:
        #all data has been collected
        pass
    else:
        print labellist
        s.dlabel = labellist[0]
        #initial values should actually be set in main() where the sessionlists are set.
        #if they're true for all the sessions in that sessionlist.
        s.DoNotShowEndingScreen = TRUE # another default. will manually specify by sessionlable at the end of which session ending screen should be shown.
        #we should be able to do it this way:
        if len(labellist)==1:
            s.DoNotShowEndingScreen = FALSE
       
        setPerSessionValues()
    
        print 'attempting to run %s, with sessiontype %s' %(s.dlabel, s.sessiontype)
        retval = s.run() #run the session
        if s.dcompleted and (retval != MYQUIT):
            continuex(labellist[1:]) #call the continuex function, passing in one fewer label than was passed to this instance.
        
def main():
    """
    the main function- an endless while loop which does not exit unless a quit value is returned from
    s.displaymainmenu()
    """
    while 1:
        response = s.displaymainmenu()
        if response!=QUIT:
            if response == FIRSTTIME:
                print 'firsttime'
                s.dresumed = FALSE  # this is not a resumed session. Need new user data (full name, etc).
            else: s.dresumed = TRUE
            response = s.getuserdata() #get user data. If s.dresumed, this also loads saved data, session position, session label.

            if not s.dresumed: #need to set up initial sessionlists (resumed sessions should have stored values)
                if s.sessiontype == 'var':
                    print s.sessiontype
                    s.sessionlist = VARSESSIONLIST
                    s.sortlist = TRUE
                else:
                    s.sessionlist = SESSIONLIST
            
            if response != MYQUIT:
                if s.dresumed:
                    print 'MAIN: attempting to run %s, with sessiontype %s' %(s.dlabel, s.sessiontype)
                    #s.dtrialblocksize = 2 #settings are retained for subsequent sessions.
                    #s.dintermissiondelay = 10
                    
                    setPerSessionValues()
                    
                    retval = s.run()  #run the session (er, go through the directory of images corresponding to a particular label)
                    #...need to do other sessions as necessary
                    if s.dcompleted and (retval != MYQUIT): 
                        startpos = s.sessionlist.index(s.dlabel) #find how far they've progressed through SESSIONLIST
                        if not ((startpos + 1) == len(s.sessionlist)): #if not last item in list
                            continuex(s.sessionlist[startpos + 1:])
                        else: #we're done.
                            pass
                    
                else:  #start fresh with practice. (full sessionlist)
                    continuex(s.sessionlist)
        else: #exit program
            return

if __name__ == '__main__': main() #this tells the program to call the function main() if it is called directly (e.g. doubleclicked)


