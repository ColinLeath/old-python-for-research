import Image
import sys
#from time import sleep
import os
import getopt
import glob
FALSE = 0
TRUE = 1
deleteFiles = TRUE 
#need to get path that should have been passed to script.

def usage():
    print 'bad args!'


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h")
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    output = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-o", "--output"):
            output = a
    
    filenames = glob.glob(args[0])
    #for filename in filenames:
    #    print filename

    for filename in filenames:
        extractRedChannelFromImage(filename)
    #print sys.argv[0]
#if len(sys.argv) > 1:
#    imagePath= sys.argv[1]
##	if sys.argv[1]=='-i':
#    print sys.argv[0]
#else:
#    imagePath=r'x:\workingdirectory\testChannel.png'
#    deleteFiles = false
#    #imageRootPath=r'C:\_research_cleath\Documents-By-Date-and-Study\2002-10-01-Stereo-Study\Images\test_L.bmp'
#

def extractRedChannelFromImage(fullFileName,replace=TRUE):

    #open image, ensure it is RGB and split it into 3 channels
    myImage = Image.open(fullFileName).convert("RGB")
    source = myImage.split()
    R, G, B = 0, 1, 2
    
    #zero out other two channels.
    blankImage = Image.new("L",myImage.size)
    myImage = Image.merge("RGB",(source[R],blankImage,blankImage))
    
    if replace:
        #Replace infile
        myImage.save(fullFileName)
    else:
        myImage.save(fullFileName[:-4]+'_out' + fullFileName[-4:])
    


if __name__ == "__main__":
    main()
