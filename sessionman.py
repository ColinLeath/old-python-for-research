from session import Session
TRUE = 1
FALSE = 0
global s     #for pointing to instance of session class.
#global SESSIONLIST  #the list of labels (I was calling them sessions) which will constitute the entire experience of one participant (one session).
s = Session() #create an instance of the Session class.
#s.dfullscreen=FALSE
s.initio()  #initialize i/o
#SESSIONLIST = ['isopractice','linepractice','practice','run1','run2'] 
#SESSIONLIST = ['isopractice','tlpractice','practice','tl'] 
#SESSIONLIST = ['final'] 
#SESSIONLIST = ['fccomp','fcconv'] 
#SESSION_TYPE = ISO
#global ISOSESSIONLIST 
ISOSESSIONLIST = ['isopractice','iso56'] 
LISESSIONLIST=['finalsub']
#SESSION_TYPE = FORCEDCHOICE
#global FCSESSIONLIST #not sure if needs to be global
#FCSESSIONLIST2 = ['lipractice_comp','practice_comp','fc_comp','lipractice_conv','practice_conv','fc_conv'] 
FCSESSIONLIST = ['lipractice_conv','practice_conv','fc_conv','lipractice_comp','practice_comp','fc_comp'] 
#these are labels, which the code below uses to modify the standard behavior of the session class
#sometimes they correspond to directory names.
#should make sessionlist a dictionary containing labels and imagedirs.

#FCSESSIONLIST = ['final']

#define constants to make reading code easier.
QUIT = 0
BEGIN = 1
FIRSTTIME = 2
FALSE = 0
TRUE = 1
MYQUIT = -99

def setPerSessionValues():
    #set session attributes particular to a given session label here.
    #if s.dlabel in ['practice','run1','run2']:

    ##let's test:
    #s.test = TRUE
    #s.dsound = FALSE
    
    #set defaults:
    s.dtrialblocksize = 60 
    s.numberoftrials = 99999 # this is bad but I think necessary for now. (the code that resets it to this value is only called when imagelist is initted) . Setting it to this high number basically means that all trials will be used (as opposed to say 60 from a directory of 480)
    s.dintermissiondelay = 60
  
    if s.sessiontype in ['fc','fc2']:
        s.dtrialblocksize = 120 
        #s.calcspinnerpos = TRUE #constrain pointer to compression or convergence vector.
        #print "setting s.calcspinnerpos = true"
        #the above is now handled when data is loaded.
        
        if s.dlabel[-4:]=='comp':
            s.convergence = FALSE
        else:
            s.convergence = TRUE
            
        if s.dlabel in ['fc_conv','fc_comp','practice_comp','practice_conv']:
            #s.dimagedir = 'x:\\final'             
            s.dimagedir = r'X:\_old\_Aperture\2002-06-06-Study-1-lines\final'
            if s.dlabel in ['practice_comp','practice_conv']:
                s.numberoftrials = 60
        else:
            #s.dimagedir = 'x:\\' + s.dlabel[:-5]
            #s.dimagedir = r'X:\_old\_Aperture\2002-06-06-Study-1-lines\final'
            
            s.dimagedir = r'X:\_old\_Aperture\2002-06-06-Study-1-lines' + '\\' + s.dlabel[:-5]
            #s.dimagedir = r'X:\_old\_Aperture\2002-09-06-Study-4-Forced-Choice\errtest'
    elif s.dlabel in ['final','lipractice','finalsub']:
       s.dimagedir = r'X:\_old\_Aperture\2002-06-06-Study-1-lines' + '\\' + s.dlabel
    #elif s.dlabel in ['practice']:
    #   s.dimagedir = 'x:\\iso56'
    #   s.numberoftrials = 120
    #   #s.dtrialblocksize = 2
    #   #s.dintermissiondelay = 2 

    else:
        #in this case, the directory containing the images matches the label.
        s.dimagedir = r'X:\_old\_Aperture\2002-08-06-Study-3-isotropic-texture' + '\\' + s.dlabel

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
                s.calcspinnerpos = FALSE # we'll make this the default. Should we take care of this in getuserdata?
        #it gets set to a non-default value when values are loaded in session.py

                if s.sessiontype == 'iso':
                    s.sessionlist = ISOSESSIONLIST
                    print 'iso session'
                elif s.sessiontype in ['fc','fc2']:
                    s.calcspinnerpos = TRUE
                    #later need to alternate order. of compression and convergence modes. from one participant to the next.
                    if s.sessiontype == 'fc':
                        print 'fc session'
                        s.sessionlist = FCSESSIONLIST
                    else:
                        print 'fc2 session'
                        s.sessionlist = FCSESSIONLIST2
                elif s.sessiontype == 'li':
                    s.sessionlist = LISESSIONLIST
                    print 'line session'
                else:
                    #this should never happen because of input checking in getuserdata function.
                    #but currently the sessiontypes must be added in both places, a mistake..
                    #should be centralized here.
                    print 'unk session'
                    return "unknown session type!"
            
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


