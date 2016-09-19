"""
This module contains a class definition "Session" and support functions/classes for displaying a directory (order randomized) of images to the screen, allowing a user to rotate a pointer on the screen, and recording the pointer orientation thereby specified.


Known issue: 2002-09-04-1121 
    if you create an iso user after running an fc session, the pointer won't be randomly positioned.
    workaround: (esc) and reload the data. The pointer gets reset when the data is loaded.
"""

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
import calcspinnerpos

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

class resumedata:
    "for pickling data used to resume, needs to be on top level of module"
    list = []
    n = -1
    label = ''
    imagedir = ''
    sessionlist =[]
    sessiontype = '' #currently could be FC (forced choice) or iso (isotropic)
    #any other data needed?


#the following timer function & variables were used to trouble shoot pointer lag (pointer would rotate faster through some orientations than others.
#timer = 0
#sf = open('timerka.csv','w')
#def stopwatch(message = None):
#    "simple routine to time python code"
#    global timer,sf
#    if not message:
#        timer = pygame.time.get_ticks()
#        return
#    now = pygame.time.get_ticks()
#    runtime = now - timer
##    print message, runtime, ('seconds\t(%.2ffps)'%(1.0/runtime))
#    print message, runtime 
#    sf.write(message + ',%d\n'%runtime)
#    timer = now


class Session:
    "an interface for running sessions."
    #conventions '_' precedes names of functions intended to be private (only called from other functions within the class)
    #verbs for methods and nouns for data attributes
    #'d' preceding attributes (note I gave up on that, and probably won't repeat the use of that convention) and nothing special for methods
   
    def __init__(self, screen=None): #only runs if class instance is created
        self.dlabel              = '' #label is used to differentiate data (it is recorded in output file). It is also used to affect program flow in some kludges (notably _showintermissionscreen)
        self.dscreen             = None #this is the handle/reference to the display
        #self.dtrialblocksize     = 3.141 #any integer mod this. will not be zero uncomment this line and comment out following to turn off intermissions.
        self.dtrialblocksize     = 60 #Set trialblock size to get intermissions every trialblocksize trials.
        self.dintermissiondelay  = 120 #seconds
        self.dimagedir           = 'x:\\' #usually set by sessionman.py or by loading saved session.  
        self.dresumed            = FALSE #resumed session or not
        self.dsound              = TRUE  #beep when new image loaded or not.
        self.dcalibrationimage   = 'x:\\calibrationimage.png'
        self.ddatafilename       = 'data.csv'  #this is where participant/user spinner/pointer data is stored. Usually it will be 'u' + username + '.csv'    
        self.dfullscreen         = TRUE 
        self.dcompleted          = FALSE #have all the images corresponding to a particular label been viewed & data recorded?
        self.dparticipantname    = 'lukeskywalker' #dummy name--I believe this name is checked for in getuserdata...
        self.dparticipantlistfilename = 'participantdata.csv' #this is where participant full name, acuity, etc are stored.
        self.repeatrate          = 1  #milliseconds. if a key (e.g. arrow key is held down a new keypress will register every 1 ms)
        self.frames_per_second   = 100 #used to control rotation speed of pointer. The repeat rate above (if set to 1ms) has no effect, as this setting limits the speed.
        self.clock = pygame.time.Clock() #initialize clock used for controlling framerate
        self.test                = FALSE #if this is set to TRUE, the program in test mode will display every image corresponding to a label, recording a random pointer setting without needing user intervention until the end of a directory of images is reached. Used to generate dummy data and test script.
        
        #self.calcspinnerpos     = TRUE
        self.calcspinnerpos     = FALSE
        #self.convergence        = TRUE
        self.convergence        = FALSE 
        self.correct_conv_or_compression_value = -999

        #possibly temporary, not sure if this will work:
        self.sessionlist = []
        self.sessiontype = 'fc' #currently only iso or fc. Really should be handled from sessionman...
        self.numberoftrials = 99999 #this value is set to a lesser number for practice sessions.
                                    #this value could cause a problem if we ever wanted to run more trials than this (not likely)
        self.DoNotShowEndingScreen = FALSE #suppresses showing of ending screen. if true.

        
 
    def _initpointer(self):
        "this initializes the pointer value prior to each trial"
        self.pointer.dizzy = -1
        
        if self.calcspinnerpos:
           #first need to get values (slant, spin, tilt) from imagename.
           #following copied from mainfunc, need to refactor eventually.
           filename=self.imagelist[self.n]
           #print filename
           spin=999#'pythonsucks'  #why? because for some reason I'm having to intialize this variable...it's not getting set in the except: handler.
           try:
               #old startpos=string.find(filename,'sl_')+3
               #old tilt=int(filename[startpos:startpos+3])
               #old -- not quite right: tilt = 90 - int(filename[-6:-4])*(350.0000/9.0000)
               #    #if tilt < 0:
               #    #    tilt += 360
               tiltpos = string.find(filename,'t_')
               tilt = int(filename[tiltpos-3:tiltpos])
               spinpos = string.find(filename,'sp_')
               spin = int(filename[spinpos-3:spinpos])
               slantpos = string.find(filename,'sl_')
               slant = int(filename[slantpos-3:slantpos])
               #texture=filename[slantpos+3:slantpos+5]
           except:
               print 'cantparsefilename'
               tilt=0
               spin=0
               slant=0
               #texture='unk'

           self.pointer.calcpos = calcspinnerpos.calcspinnerpos(slant,spin,tilt, self.convergence)
           #store correct value for checking later. could practice dual assignment here--maybe later.
            
           #just for a test:
           #switch back later!
           #sc = self.pointer.calcpos
           #if sc >= 180:
           #   calcpos2 = sc - 180
           #else:
           #   calcpos2 = sc + 180
           #self.correct_conv_or_compression_value = random.choice([sc,calcpos2])

           
           self.correct_conv_or_compression_value = self.pointer.calcpos 
   
    def initio(self):
        "Initialize Everything--only needs to be done once if running multiple sessions."
        pygame.init()
        #self.START_RES = (1024,768)
        self.START_RES = (1600,1200)
        if self.dfullscreen:
            self.dscreen = pygame.display.set_mode(self.START_RES, FULLSCREEN)
        else:
            self.dscreen = pygame.display.set_mode(self.START_RES)
        pygame.display.set_caption('pretty picture')
        pygame.mouse.set_visible(0) #mouse will not appear in display window
        #pygame.event.set_blocked(MOUSEMOTION)
        pygame.event.set_allowed(KEYDOWN) #only KEYDOWN events will be used.
        pygame.key.set_repeat(500,self.repeatrate)
        
        #Prepare Game Objects put -- in separate function?
        self.pointer = Pointer()
        #self._initpointer() moved to self.run()
        self.pointer.dizzy = -1
        self.allsprites = pygame.sprite.RenderUpdates((self.pointer))

    def displaymainmenu(self):
        self.dscreen.fill((0,0,0)) #screen is a surface! fill it with black
        my_font = pygame.font.Font(None, 22)
        tboxwidth = 300
        tboxheight = 300
        xpos =  self.dscreen.get_width()/2 - tboxwidth/2
        ypos = 250  

        my_string = "Welcome to the Sedgwick lab!\n \nto begin, press [enter]"
        my_rect = pygame.Rect((xpos, ypos, tboxwidth, tboxheight))
        rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 0)
        if rendered_text:
            self.dscreen.blit(rendered_text, my_rect.topleft)
        pygame.display.update()
        #pygame.key.set_mods(KMOD_NONE)
        while 1:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                #attempting to be able to handle more complex keypresses:
                #keys = pygame.key.get_pressed()
                #pygame.key.get_mods()&(KMOD_SHIFT|KMOD_ALT) ==(KMOD_ALT|KMOD_SHIFT)
                #print pygame.key.get_mods()&(KMOD_SHIFT|KMOD_ALT|KMOD_CTRL) ==(KMOD_ALT|KMOD_SHIFT|KMOD_CTRL)
                #print (KMOD_ALT|KMOD_SHIFT|KMOD_CTRL)
                #print pygame.key.get_mods()
                #print keys
                if event.key == K_F12:#new user
                   return 2
                elif event.key == K_RETURN: #begin
                   return 1
                elif event.key == K_F5: #quit
                   return 0
  

    def getuserdata(self):
        """
        This function will get initial particpant data (acuity, fullname, etc.) if this is not a resumed session. If it is a resumed session, the user's saved data will be loaded.
        """
        # init some values 
        answer = '-1'
        #list directory and keep only those names starting with 'u' and ending with '.csv,' then remove the 'u' and the '.csv,' for a list of previously entered user names.
        mylist = os.listdir('.')
        def ff(x): return re.match('u.*\.csv',x)
        mylist = filter(ff,mylist) #keep only names beginning with 'u' and ending with '.csv'
        def ff(x): return x[1:-4]
        mylist = map(ff,mylist)    #strip first 1 and last 4 character(s) from strings in list.
        self.listofnames = mylist + ['','q','quit']

        if not self.dresumed: #this is participant's first time-- need experimenter to enter some info
            #defaults:
            fullname = ''
            acuity = ''
            dominanteye = ''
            experimenter = ''
            #self.sessiontype = '' default set in intialization of class
            accepted = FALSE
            while not accepted:
                answer = ''
                fullname = inputbox.ask(self.dscreen, "P's full name", fullname)
                acuity = inputbox.ask(self.dscreen, "P's acuity", acuity)
                dominanteye = inputbox.ask(self.dscreen, "P's dominant eye", dominanteye)
                experimenter = inputbox.ask(self.dscreen, "Experimenter", experimenter)
                self.sessiontype = inputbox.ask(self.dscreen, "Sessiontype (iso,fc,fc2)",self.sessiontype).lower() #lower not really necessary since user can only put in lowercase.. but.
                my_font = pygame.font.Font(None, 22)
                tboxwidth = 300
                tboxheight = 250
                xpos =  self.dscreen.get_width()/2 - tboxwidth/2
                ypos = 200  
                
                #now, display values so experimenter can confirm.
                if self.sessiontype.lower() not in ['iso', 'fc','fc2']:
                    #for now, just put in a default value.
                    self.sessiontype = 'iso'
                
                my_string = 'Are these values o.k.?\n    Full name: %s\n    Acuity: %s\n    Dominant eye: %s\n    Experimenter: %s\n    Session type: %s'%(fullname, acuity, dominanteye, experimenter, self.sessiontype) 
                my_rect = pygame.Rect((xpos, ypos, tboxwidth, tboxheight))
                rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 0)
                
                if rendered_text:
                    self.dscreen.blit(rendered_text, my_rect.topleft)
                
                pygame.display.update()

                while answer not in ['y','yes','n','no']:
                    answer = inputbox.ask(self.dscreen, "(y/n) ",'')
                accepted = answer not in ['n','no']

        self.dparticipantname = string.strip(inputbox.ask(self.dscreen, "Your name")) #this is the name user will use to resume their saved session.
        
        if not self.dresumed: #this is their first time--need to ensure unique name
            while self.dparticipantname in self.listofnames:#need to tell to enter unique name#need to reset self.dparticipant
                self.dparticipantname = inputbox.ask(self.dscreen, "taken! Your name")
            #now, write out data to separate file
            f = open(self.dparticipantlistfilename,'a')
            if os.path.getsize(self.dparticipantlistfilename)==0:
                #this is an empty file, add header row
                f.write('pname, fullname, acuity, dominanteye, experimenter, time, sessiontype\n')
            f.write('%s,%s,%s,%s,%s,%s,%s\n'%(self.dparticipantname, fullname, acuity, dominanteye, experimenter, time.ctime(),self.sessiontype))
            f.close
       
        #set data file name
        self.ddatafilename = 'u' + self.dparticipantname + '.csv'
        
        if self.dresumed:
            while 1: #make sure user data exists 'q', 'quit' will exit function.
                print "checking existence of " + self.ddatafilename
                if self.dparticipantname.lower() not in ['q','quit']:
                    if os.path.isfile(self.ddatafilename):
                        print 'file exists'
                        break
                    else:
                        self.dparticipantname = inputbox.ask(self.dscreen, "retry: Your name")
                        self.ddatafilename = 'u' + self.dparticipantname + '.csv'
                else:
                    return MYQUIT
            #now, load previously saved data, and that's it!
            f = open(self.ddatafilename[:-4]+'.dat','r')
            myresumedata = pickle.load(f)
            self.imagelist = myresumedata.list
            self.n          = myresumedata.n
            self.dlabel     = myresumedata.label
            self.dimagedir = myresumedata.imagedir
            self.listlen = len(self.imagelist)
            self.sessionlist = myresumedata.sessionlist
            self.sessiontype = myresumedata.sessiontype
            if self.sessiontype in ['fc','fc2']:
                self.calcspinnerpos = TRUE
            else:
                self.calcspinnerpos = FALSE
                self.pointer.calcpos = 999 #need to re-init pointer or new value won't be chosen from a random selection from a range of values (will just flip between two instead)
                

    def getimagedir(self):
        "a function for getting directory containing images (currently not used)"
        inputbox.ask(self.dscreen, "Directory",dimagedir)
        
    def _initimagelist(self):
        "Create randomized list of images:"
        self.imagelist = os.listdir(self.dimagedir)
        random.shuffle(self.imagelist)
        ###if self.dlabel == 'practice': #practice session should be 120 randomly selected images from main imagedir
        ###    #for practice session, should pass in same directory as run1, run2, but it will be handled differently here.
        ###    self.imagelist = self.imagelist[:120] #if list is less than or =120, returns entire list
        if self.numberoftrials <> 99999: #this allows for reducing the number of trials, like for practice sessions.
            self.imagelist = self.imagelist[:self.numberoftrials]
            self.numberoftrials = 99999 #should be using a constant here.

            
        self.listlen = len(self.imagelist)
        
    def _showcalibrationscreen(self, showtext=TRUE):
        "displays calibration screen until <<enter>> is pressed"
        img, rect = load_image(self.dcalibrationimage)
        self.dscreen.blit(img, rect)
        
        if showtext:
            my_font = pygame.font.Font(None, 22)
            tboxwidth = 300
            tboxheight = 125
            xpos =  self.dscreen.get_width()/2 - tboxwidth/2
            ypos = 325  
            my_string = 'Adjust your position so you can see all of the blue ring and none of the red ring.\n\nPress [enter] to continue.' 
            my_rect = pygame.Rect((xpos, ypos, tboxwidth, tboxheight))
            rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 1)

            if rendered_text:
                self.dscreen.blit(rendered_text, my_rect.topleft)

        pygame.display.update()
        
        pygame.event.get()  #clear event queue, otherwise, was taking a long time and multiple enters could be pressed, bypassing calibration screen.
        while 1:
            event = pygame.event.wait()
            if (event.type == KEYDOWN) and (event.key == K_RETURN): 
                break
        
    def _showintermissionscreen(self):
        """
        This function shows the intermission screen.
        It contains some kludges based on session label to affect the display of the intermission screen.
        """
        if self.test:
            self.dintermissiondelay = 5
            
        self.dscreen.fill((0,0,0)) #screen is a surface! fill it with black
        tboxwidth = 500
        tboxheight = 200
        xpos =  self.dscreen.get_width()/2 - tboxwidth/2
        #xpos =  250
        ypos = 220  
        blocks = (self.n/self.dtrialblocksize)
        
        #kludge 1:
        if self.dlabel == 'tl':  
            blocks = blocks + 2
        elif self.dlabel == 'run2':
            blocks = blocks + 10
        elif self.dlabel == 'iso56':
            blocks = blocks + 2
 
        blocks = str(blocks)        
        if blocks in ['11','12','13']:
             ordinal='th'
        elif blocks[-1] == '1':
            ordinal = 'st'
        elif blocks[-1] == '2':
            ordinal = 'nd'
        elif blocks[-1] == '3':
            ordinal = 'rd'
        else:
            ordinal = 'th'

        remainingblocks = ((self.listlen-self.n)/self.dtrialblocksize)
        print 'remainingblocks: %d, listlen: %d, n: %d, trialblocksize: %d'%(remainingblocks,self.listlen, self.n, self.dtrialblocksize)
        
        #kludge 2: 
        if self.dlabel == 'practice':
            remainingblocks = remainingblocks + 16
        elif self.dlabel == 'run1':
            remainingblocks = remainingblocks + 8

        if remainingblocks == 1:
            sngpl = ''
        else:
            sngpl = 's'

        my_font = pygame.font.Font(None, 22)

        #kludge 3:
        #if not((self.dlabel == 'run2') and (remainingblocks ==0)):
        #if (remainingblocks!=0) or (self.dlabel.find('practice')>-1):
        if self.DoNotShowEndingScreen or (remainingblocks!=0):
            #if not the screen displayed after the very last trial:
            #if not at the end of a directory, or if at the end of practice session:
            my_string = 'Congratulations!\n\n\nYou have completed the %s%s block of %d trials,\nwith %d block%s remaining. \n\nTo continue, rest %3.1f min. until a new screen appears. \n\nTo quit now, press [esc].' % (blocks, ordinal, self.dtrialblocksize, remainingblocks, sngpl, (self.dintermissiondelay/60.0))
            print my_string
            my_rect = pygame.Rect((xpos, ypos, tboxwidth, tboxheight))
            rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 1)
            if rendered_text:
                self.dscreen.blit(rendered_text, my_rect.topleft)
            pygame.display.update()

            pygame.time.set_timer(USEREVENT, self.dintermissiondelay*1000) #A user event will be put on event queue after time specified.

            while 1:
                event = pygame.event.wait()
                if (event.type == KEYDOWN) and (event.key == K_ESCAPE):
                    self._savedata()
                    return MYQUIT
                elif event.type == USEREVENT:
                    break
            
            
            
            my_string = '\n\nPress [enter] to continue.\n\nTo quit now, press [esc].' 
            my_rect = pygame.Rect((xpos, ypos, tboxwidth, tboxheight))
            #rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 1)
            rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (50, 255, 50), (48, 48, 48), 1)
            if rendered_text:
                self.dscreen.blit(rendered_text, my_rect.topleft)
            pygame.display.update()

            pygame.time.set_timer(USEREVENT, 8*1000)#set event to fire every 8 seconds to prompt beep

            while 1:
                event = pygame.event.wait()
                if (event.type == KEYDOWN): 
                    if event.key == K_ESCAPE:
                        self._savedata()
                        return MYQUIT
                    elif event.key == K_RETURN:
                        break
                elif event.type == USEREVENT:
                    winsound.Beep(2000,150)
        else:
            my_string = '\nCongratulations!\n\nYou\'re finally done! \n\nPress [enter] to quit.' 
            print my_string
            my_rect = pygame.Rect((xpos, ypos, tboxwidth, tboxheight))
            rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (50, 255, 50), (48, 48, 48), 1)
            if rendered_text:
                self.dscreen.blit(rendered_text, my_rect.topleft)
            pygame.display.update()

            while 1:
                event = pygame.event.wait()
                if (event.type == KEYDOWN): 
                    if event.key == K_RETURN:
                        self._savedata(silent=TRUE) #ensures they can't get back in again(with same user name)!
                        return MYQUIT
        
    def _savedata(self,silent=FALSE):
        "saves data, and displays screen saying so, unless function parameter 'silent' is TRUE"
        self.datafile.close() #close data file so all data in buffer is written out.
        myresumedata = resumedata() #instance of resumedata class
        myresumedata.n = self.n
        myresumedata.list = self.imagelist
        myresumedata.label = self.dlabel
        myresumedata.imagedir = self.dimagedir
        myresumedata.sessionlist = self.sessionlist
        myresumedata.sessiontype = self.sessiontype
        f2 = open(self.ddatafilename[:-4]+'.dat', 'w')
        pickle.dump(myresumedata, f2) #save (pickle) data to file f2.
        f2.close()
        try:
            #copy saved data to backup directory on \\\\g6-200
            filename = self.ddatafilename
            shutil.copyfile(filename, '\\\\g6-200\\bdata\\' + filename)
            filename = filename[:-4]+'.dat'
            shutil.copyfile(filename, '\\\\g6-200\\bdata\\' + filename)
            filename = self.dparticipantlistfilename
            shutil.copyfile(filename, '\\\\g6-200\\bdata\\' + filename)
        except:
            #send error message-- this would not work if cable gets disconnected!
            os.system('net send g6-200 failed to copy ' + filename)
            
        if not silent:
            self.dscreen.fill((0,0,0)) #screen is a surface! fill it with black
            tboxwidth = 250
            tboxheight = 250
            xpos =  self.dscreen.get_width()/2 - tboxwidth/2
            ypos = 300  
            my_font = pygame.font.Font(None, 22)
            #if not the screen displayed after the very last trial:
            my_string = '\n\nYour data has been saved.\n\nThank you for participating in our study!\n\nTo return to the main menu, press [enter]'
            my_rect = pygame.Rect((xpos, ypos, tboxwidth, tboxheight))
            rendered_text = textrect.render_textrect(my_string, my_font, my_rect, (216, 216, 216), (48, 48, 48), 1)
            if rendered_text:
                self.dscreen.blit(rendered_text, my_rect.topleft)
            pygame.display.update()

            #code to set up a delayed return to main menu even if no key is pressed(?):
            #pygame.time.set_timer(USEREVENT, self.dintermissiondelay*1000)
            
            while 1:
                event = pygame.event.wait()
                if (event.type == KEYDOWN) and (event.key == K_RETURN):
                    return 
                #elif event.type == USEREVENT:
                #    break

    def run(self):
        "manage running of session here"
        self.dcompleted = FALSE #reset this attribute
        #init imagelist
        if not self.dresumed:
            self._initimagelist()
            self.n = 0  #init counter
            #self.pointer.dizzy = -1 #moved below so pointer initialization occurs on resume as well.
        elif self.n == self.listlen: #should only occur if self.dresumed 
            #handle case where participant saved data and quit at very end of session.
            self.dcompleted = TRUE
            self.dresumed = FALSE #reset this otherwise n read from pickled data will continue to be used
            return  #exit function

        print "self.n, %d"%self.n
         
        self._initpointer() #reset pointer values.
        
        self._showcalibrationscreen()
        
        #Display The Background -- load first image
        img, rect = load_image(os.path.join(self.dimagedir,self.imagelist[self.n]))
        self.dscreen.blit(img, rect)
        pygame.display.flip()
        
        #initialize datafile:
        self.datafile = open(self.ddatafilename,'a')
        if os.path.getsize(self.ddatafilename)==0:
            #this is an empty file, add header row
            if self.calcspinnerpos:
                header ='name,sessionlabel,date,imagename,time,n,texture,slant,spin,tilt,spec_tilt,conversion,convergence,correct\n'
            else:
                header = 'name,sessionlabel,date,imagename,time,n,texture,slant,spin,tilt,spec_tilt,conversion,diff,abs_diff\n'
            self.datafile.write(header)
        #Main Loop
        while 1:
            if self.test:
                #set event = to an <<enter>> keypress. and set pointer position to random value.
                event = pygame.event.Event(KEYDOWN, {'key': 13, 'unicode': u'\r', 'mod': 4096})
                if self.calcspinnerpos:
                    sc = self.pointer.calcpos
                    if sc >= 180:
                       calcpos2 = sc - 180
                    else:
                       calcpos2 = sc + 180
                    self.pointer.dizzy = random.choice([sc,calcpos2])
                else:
                    self.pointer.dizzy = random.randrange(359)
            else:
                event = pygame.event.wait()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   #quit and save data
                   self._savedata()
                   return 
                elif event.key == K_LEFT and not self.calcspinnerpos:
                    self.clock.tick(self.frames_per_second)
                    self.pointer.direction = COUNTERCLOCKWISE
                    self.allsprites.clear(self.dscreen, img)
                    self.allsprites.update()
                    pygame.display.update(self.allsprites.draw(self.dscreen))
                    
                elif event.key == K_RIGHT:
                    self.clock.tick(self.frames_per_second)
                    #stopwatch('%d'%self.pointer.dizzy)
                    #stopwatch()
                    
                    if self.calcspinnerpos:
                        self.pointer.direction = FLIP
                    else:
                        self.pointer.direction = CLOCKWISE
                        
                    self.allsprites.clear(self.dscreen, img)
                    self.allsprites.update()
                    pygame.display.update(self.allsprites.draw(self.dscreen))

                    #print 'pointerpos: %d'%self.pointer.dizzy
                    
                elif event.key == K_UP: #show spinner
                    self.pointer.direction = NOCHANGE #ensures sprite is not rotated
                    self.allsprites.update()#necessary to clear sprite from previous trial
                    pygame.display.update(self.allsprites.draw(self.dscreen))
                    
                elif event.key == K_DOWN: #hide spinner
                    self.allsprites.clear(self.dscreen,img)
                    pygame.display.update()
                elif event.key == K_q:
                    self.dsound = not(self.dsound)
                elif event.key == K_TAB:
                    #display position in imagelist in upper left of screen
                    fontobject = pygame.font.Font(None,18)
                    if self.calcspinnerpos:
                        displaystring = '%d %s %d %d'%(self.n,self.imagelist[self.n],self.correct_conv_or_compression_value,self.pointer.dizzy)
                    else:
                        displaystring = '%d'%self.n
                    
                    #if on is None or on is FALSE:
                    #    self.dscreen.blit(fontobject.render(displaystring, 1, (255,255,255)), (1, 1))
                    #    pygame.display.flip()
                    #else:
                    #    self.dscreen.blit(fontobject.render(displaystring, 1, (0,0,0)), (1, 1))
                    #    pygame.display.flip()
                    #    on = not on
                     
                    self.dscreen.blit(fontobject.render(displaystring, 1, (255,255,255)), (1, 1))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    self.dscreen.blit(fontobject.render(displaystring, 1, (0,0,0)), (1, 1))
                    pygame.display.flip()
    
                elif event.key == K_SPACE:
                    #go back one image:
                    if self.n >= 1:
                        self.n -= 1
                        img, rect = load_image(os.path.join(self.dimagedir,self.imagelist[self.n]))
                        self.dscreen.blit(img, rect)
                        pygame.display.flip()
                        self._initpointer()
                elif event.key == K_RETURN:
                    #record pointer position and load new image or display intermission screen or exit function, depending.
                    if self.pointer.dizzy != -1: #only proceed if the pointer has been moved from its initial random position.
                        if self.dsound: 
                            winsound.Beep(2000,150)
                        #write data for trial and load next image in list
                        #print '%s,%d' % (imagelist[n],pointer.dizzy)
                                        

                        #
                        # All of the following lines handle the writing of information to the file that will later be
                        # used for the data analysis.
                        # note that at different times, different file name formats have been used for the images
                        # so old code lying around may have been concerned with the older schemes. Perhaps this old 
                        # code can be removed.
                        # old naming schemes could be revived if a different approach is taken to rendering the
                        # images--e.g. using the animate tool to create a sequence of images with different spins and slants
                        # instead of the current incarnation where only one frame is rendered per scene.
                        
                        date = time.ctime()
                        ttime = date[11:19]
                        date = date[:11] + date[-4:]
                        #get tilt:
    		        	#old filename format: 	dgtile90-45sp_30sl_090t0003.png
    		        	#new filename format: 	dsplat_090-120t_060sp_045sl_tl_0007.png
                        #newer filename format: rpxsmo_0000150t_030sp_030sl_tx_0000.png
                        filename=self.imagelist[self.n]
                        spin='pythonsucks'  #why? because for some reason I'm having to intialize this variable...it's not getting set in the except: handler.
                        try:
                            #old startpos=string.find(filename,'sl_')+3
                            #old tilt=int(filename[startpos:startpos+3])
                            #old -- not quite right: tilt = 90 - int(filename[-6:-4])*(350.0000/9.0000)
                            #    #if tilt < 0:
                            #    #    tilt += 360
                            tiltpos = string.find(filename,'t_')
                            tilt = int(filename[tiltpos-3:tiltpos])
                            spinpos = string.find(filename,'sp_')
                            spin = int(filename[spinpos-3:spinpos])
                            slantpos = string.find(filename,'sl_')
                            slant = int(filename[slantpos-3:slantpos])
                            texture=filename[slantpos+3:slantpos+5]
                        except:
                            print 'cantparsefilename'
                            tilt=0
                            spin='0'
                            texture='unk'
    
                        #problem: need to rezero at 360/0
    		        	#if the following needs to be done in excel, here it is:
    		        	#=IF(AND((ABS((J2-I2))>180),(J2>I2)),J2-360,IF(AND((ABS((J2-I2))>180),(J2<I2)),J2+360,J2))
    		        	#where J has the spec_tilt, and I has the tilt.
                        if not self.calcspinnerpos:
                            conversion = self.pointer.dizzy
                            if conversion == -1:
                                conversion = 999 #-1 is now a valid value due to the follwing:
                            elif (conversion > tilt) and abs(conversion-tilt)>180: #if conversion is more than 180 away from the actual tilt, then subtract 360.. The purpose of this is to handle cases such as when the user specifies a tilt of 1 degree, when the actual tilt is 359. For the purpose of graphing the data, 1 should be graphed as 361, in that case. Honestly I have had trouble thinking this through, but this solution appears to work.
                                conversion = conversion - 360
                            elif (conversion < tilt) and abs(conversion-tilt)>180:
                                conversion = conversion + 360
    
                            diff = conversion - tilt  # diff and abs_diff are useful to write out in the data file
                            abs_diff = abs(diff)      # to allow a quick glance at the data file to show whether a participant
                                                      # is understanding the task (getting the pointer somewhere in the vicinity). Many large diff values indicate a problem.
                        else:
                            conversion = self.correct_conv_or_compression_value

                        if self.calcspinnerpos:
                            #as a kludge we will record correct values in the form specified below in the place of abs_diff
                            #0 = wrong
                            #1 = right
                            #3 = impossible--actually we'll tease out the impossible ones later.
                            # in the database, we need to know whether it was a convergence or compression trial.
                            # we need to know spin.
                            #if convergence and spin=90.
                            #so for now, we need to record
                            #convergence? t/f
                            #was value right or wrong. At impossible spins we expect the distribution to be 50/50.
                            #that's it.
                            #print 'dizzy: %d, outval: %d'%(int(self.pointer.dizzy), int(self.correct_conv_or_compression_value))
                            #some bug: although both are floats-- I bet that is the problem-both are floats prior to conversion, but comparing floats was leading to incorrect values 1.0000000001 <> 1.000000000 for example. That is my guess.
                            correct = int(self.pointer.dizzy) == int(self.correct_conv_or_compression_value)
                            #print 'correct? %d'%correct
                            self.datafile.write('%s,%s,%s,%s,%s,%d,%s,%s,%d,%d,%d,%d,%d,%d\n' % (self.dparticipantname,self.dlabel,date,filename,ttime,self.n,texture,slant,spin,tilt,self.pointer.dizzy,conversion,self.convergence,correct))
                            
                        else:                          
                            self.datafile.write('%s,%s,%s,%s,%s,%d,%s,%s,%d,%d,%d,%d,%d,%d\n' % (self.dparticipantname,self.dlabel,date,filename,ttime,self.n,texture,slant,spin,tilt,self.pointer.dizzy,conversion,diff,abs_diff))

                        self.n += 1
                        if self.n < self.listlen:
                            #then load new image, but display intermission screen if blocksize multiple has been reached.
                            #print 'n=%d %d mod %d = %d'%(n,n,self.dtrialblocksize,(n+1)%self.dtrialblocksize)#prb: n is 0 based index..
                            #if not self.test and (self.n)%self.dtrialblocksize==0: #if remainder of n/trialblocksize is 0 then intermission time:
                            if (self.n)%self.dtrialblocksize==0: #if remainder of n/trialblocksize is 0 then intermission time: #we want to test intermission screens.
                                if self._showintermissionscreen() == MYQUIT:
                                    return #note--do not need to return MYQUIT because self.dcompleted is false
                                            #the MYQUIT FLAG was added later...
                                self._showcalibrationscreen()
                                
                            if not self.test:
                                img, rect = load_image(os.path.join(self.dimagedir,self.imagelist[self.n]))
                                self.dscreen.blit(img, rect)
                                pygame.display.flip()
                            else:
                                print self.n
                            self._initpointer()
                        else:
                            #it's time to continue on to next directory of files.
                            self.datafile.close()
                            self.dcompleted = TRUE
                            self.dresumed = FALSE #reset this otherwise n read from pickled data will continue to be used

                            if self._showintermissionscreen() == MYQUIT:
                                return MYQUIT
                            else: return


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

#classes for our game objects
class Pointer(pygame.sprite.Sprite):
    """
    pointer which user can spin
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image(os.path.join(DATAPATH,'pointer3.bmp'), -1)
        self.original = self.image
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        #self.rect.bottomright = self.area.center
        self.rect.center = self.area.center
        self.move = 0
        self.dizzy = 0
        self.calcpos = 999
        self.direction = CLOCKWISE

    def update(self):
        "my comment"
        if self.dizzy == -1:
            #randomize spinner orientation on first display on new trial
            #print 'calcpos: %d' % self.calcpos
            #prb: self.calcpos was not getting set back to 999 (done on init pointer) after alternating with fc sessions.
            if self.calcpos == 999:
            #if not self.calcspinnerpos: #that doesn't work...
                #simply get random val in range of possible degrees
                self.dizzy = random.randrange(MAXDEGREES)
            else:
                #return random selection either going with convergence (compression) or against it
                if self.calcpos >= 180:
                    calcpos2 = self.calcpos - 180
                else:
                    calcpos2 = self.calcpos + 180
                self.dizzy = random.choice([self.calcpos,calcpos2])
                #self.dizzy = self.calcpos
            #print 'random %d' % self.dizzy
        self._spin()

    def _spin(self):
        "spin the pointer"
        center = self.rect.center
        if self.direction == COUNTERCLOCKWISE:
            self.dizzy += 1
            if self.dizzy == MAXDEGREES:
                self.dizzy = 0
        elif self.direction == CLOCKWISE:
            self.dizzy -= 1
            if self.dizzy <= -1:
                self.dizzy = MAXDEGREES-1
        elif self.direction == FLIP:
            if self.dizzy >= 180:
                self.dizzy = self.dizzy - 180
            else:
                self.dizzy = self.dizzy + 180
        rotate = pygame.transform.rotate
        self.image = rotate(self.original, self.dizzy)

        self.rect = self.image.get_rect()
        self.rect.center = center

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    #Initialize Everything
    #this calls the 'main' function when this script is executed
    print "currently this script does nothing when called by itself but it could fairly easily prompt the user to enter all needed parameters and run a session (or use default parameters)"
    pass
   
if __name__ == '__main__': main()
