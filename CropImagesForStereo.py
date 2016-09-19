#note! for this script to run- it is best to have imageMagick installed
#and the following environment variable needs to be set
#MAGICK_HOME=c:\bin\ImageMagick (or wherever you've installed it)(that may be done automatically by the 
#image magick install- I'm not sure)
import Image
import sys
from time import sleep
from ImageChops import offset
import getopt
import glob
import os
from GetRedChannel import extractRedChannelFromImage
FALSE = 0
TRUE = 1
deleteFiles = TRUE
IPDinPixels = 133
RedChannelOnly = FALSE 

#deleteFiles = FALSE 
#need to get path that should have been passed to script.

#NOTE: however 3dsmax was last set using the GUI to save .png files is how it will save them when the script is running and is how this script will save them.
#currently recommended mode to save .png files is 8 bit grayscale (in 3dsmax gui).

#2002-12-09-1222 we need to update this script so that the offset and red channel options can be specified as arguments.

def usage():
    print 'bad args!'
    print 'CropImagesForStereo.py -r -o 133 rightimagefilenameinspecialformat'
    print '-r: output image is red channel of original image \n'
    print '-o 133: set IPD pixel equivalent to be 133'
    sleep(3)

def ImageMagickRetry(imageName):
    """called when PIL gets IO error reading .png file. simply loads and resaves image
    for some reason, doing this causes us to get a permission denied error when we later 
    attempt to delete imageName
    """
    print "trying im for resaving .png"
    #from shutil import copyfile
    #copyfile(imagePathL,imagePathL + '.copy') #backupfile case im messes.
    magickPath = os.path.join(os.getenv("MAGICK_HOME"),"convert.exe")
    print magickPath
    os.spawnv(os.P_WAIT, magickPath,('-quality50',imageName,imageName))
    print "IM done"
    #print "Unexpected error:", sys.exc_info()[0]
    #raise


def main():
    global RedChannelOnly
    global IPDinPixels
    global deleteFiles
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hro:")
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    output = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-r", "--red"):
            RedChannelOnly = TRUE
        if o in ("-o", "--ipdinpixels"):
            IPDinPixels = int(a)            
   
    if args == []:
        myval = raw_input("RedChannelOnly (0/1)[%d]: " % RedChannelOnly)
        if myval <> "":
            RedChannelOnly = eval(myval)
            
        myval = raw_input("IPDinPixels (0-inf)[%d]: " % IPDinPixels)
        if myval <> "":
            IPDinPixels = eval(myval)
            
        imageRootPath = r"X:\_old\_Aperture\2002-10-01-Stereo-Study\finalLines\stAL_0000120t_-40sp_030sl_li_OverUnder.png"
        #imageRootPath = r"X:\_old\_Aperture\2002-10-01-Stereo-Study\finalLines\stAL_0000330t_070sp_030sl_li_OverUnder.png"
        #extractRedChannelFromImage(imageRootPath)
        #sys.exit()
        myval = raw_input("imageRootPath [%s]: " % imageRootPath)
        if myval <> "":
            imageRootPath = myval
        #usage()
        #sys.exit(3)
        #deleteFiles = FALSE
        
    #all that is left in args after getopt is done is the filename and any options the user defined that are not used by the program (errors)    
    else:
        imageRootPath = args[0]

    #if len(sys.argv) > 1:
    #    imageRootPath= sys.argv[1]
    ##	if sys.argv[1]=='-i':
    #    print sys.argv[0]
    #else:
    #    #imageRootPath=r'X:\WorkingDirectory\calibration_R.png'
    #    imageRootPath = r'X:\_old\_Aperture\2002-10-01-Stereo-Study\probeFC\probeFC_017_-100o_R.png'
    #    #imageRootPath=r'x:\workingdirectory\calibrateScreen_R.png'
    #    deleteFiles = FALSE
    #    #imageRootPath=r'C:\_research_cleath\Documents-By-Date-and-Study\2002-10-01-Stereo-Study\Images\test_L.bmp'
    #    
    #    #that means the images you want to work with are named:
    #    #Test_L0000.png
    #    #and
    #    #Test_R0000.png
    #    #print "please specify image root path, e.g., st_0000000t_-50sp_045sl_li_L.png"
    #    #sleep(5)
    #    #sys.exit(0) # return 0 for failure.
    
    #the way the script is presently set up (2002-10-17-1102) the rootpath being passed in should have an R in it.# we need an imagePathL and an imagePathR
    # for imagePathL
    #
    # in the past we did once get fin_0000000t_-00sp_030sl_tx_00000000.png
    # (eight zeros at the end) but that seems an anomoly. so I will not code for it.
    #
    
    # The input value will look something like this: st_0000000t_-50sp_045sl_li_L.png
    # 3dsmax, when it renders something will put (at least) four zeros between the L and the .
    # resulting in an actual file name of 
    # st_0000000t_-50sp_045sl_li_L0000.png
    
    imagePathL = imageRootPath[:-5] + 'L0000' + imageRootPath[-4:]
    imagePathR = imageRootPath[:-4] + '0000' + imageRootPath[-4:]
    
    #myImagePathIn = r'X:/WorkingDirectory/stereoAutoRenderTest/st_0000000t_-50sp_045sl_li_R0000.png'
    #myImagePathOut = r'X:/WorkingDirectory/stereoAutoRenderTest/test_R.bmp'
    #imageMagickPath = r'C:\b\ImageMagick\convert.exe'
    #os.spawnv(os.P_WAIT, imageMagickPath, ('-roll+IPDinPixelsx+0y',myImagePathIn,myImagePathOut))
    
    #first, handle R image:
    myImage = Image.open(imagePathR)
    
    #due to PILs delayed execution feature, errors on opening file will occur
    #during offset function.
    try:
        myImage = offset(myImage, IPDinPixels,0)
    except IOError:
        ImageMagickRetry(imagePathR)
        myImage = Image.open(imagePathR)
        myImage = offset(myImage, IPDinPixels,0)

    #myImage.save(imagePathR)
    #store it
    myImageR=myImage.copy()
    print "loading image %s" % (imagePathL) 
    #now, for the left image:
    myImage = Image.open(imagePathL)
    
    #due to PILs delayed execution feature, errors on opening file will occur
    #during offset function.
    try:
        myImage = offset(myImage, -IPDinPixels,0)
    except IOError:  
        ImageMagickRetry(imagePathL)
        myImage = Image.open(imagePathL)
        myImage = offset(myImage, -IPDinPixels,0)

    
    #myImage.save(imagePathL)
    
    myImageL = myImage.copy()
    #create a clear new image into which to paste the parts of both images needed for the over-under display:
    #print myImageR.mode
    myImage = Image.new(myImageR.mode,myImageR.size)
    #myImage = Image.new("L",myImageR.size)
    
    #at this point we have two images, and we want to combine them into one over-under 1600 x 1200 image.
    #the procedure will be as follows:
    
    #remove 17 lines from the top and 18 from the bottom
    #of both. Then every other remaining line.
    #paste what's left together
    # with 70 lines left inbetween the top and the bottom
    
    #what PIL functions might be helpful?
    #pseudocode:
    
    newImageRow = 0
    
    #len(listRows) should =565
    #for R we will start at 17, taking every other line till a total of 565 is reached
    #for L we will start at 18, taking ""
    
    rangeR = range(0,1200,2)
    #rangeL = range(1,1201,2) 
    
    rangeR = rangeR[18:-17]  #rows 36 - 1164 even
    #rangeR = rangeR[17:-18]  #rows 34 - 1162 even
    #rangeL = rangeL[17:-18]  #rows 35 -1163 odd
    rangeL = rangeR
    
    #
    xsize, ysize = myImage.size
    print "processing right image"
    for row in rangeR:
        #we'll use image.crop and image.paste
        #
        #"""im.paste(image, box)
        #Pastes another image into this image. The box argument is either a
        #2-tuple giving the upper left corner, a 4-tuple defining the left,
        #upper, right, and lower pixel coordinate, or None (same as (0, 0)).
        #If a 4-tuple is given, the size of the pasted image must match the
        #size of the region.
        #If the modes don't match, the pasted image is converted to the
        #mode of this image (see the convert method for details)."""
        myImage.paste(myImageR.crop((0,row,xsize,row+1)),(0,newImageRow))
        #myImage(newImageRow) = myImageL(row)
        newImageRow += 1
    
    newImageRow += 70
    print "processing left image"
    for row in rangeL:
        #if row == 218: im.show()
        myImage.paste(myImageL.crop((0,row,xsize,row+1)),(0,newImageRow))
        #myImage(newImageRow) = myImage(row)
        newImageRow += 1
    
    #that should do it.
    
    imagePathOverUnder = imageRootPath[:-5] + 'OverUnder' + imageRootPath[-4:]
    #imagePathOverUnder = imageRootPath[:-5] + 'OverUnderSW' + ".png"
    
    print "saving overunder image"
    myImage.save(imagePathOverUnder)
    
    if deleteFiles:
        #delete original files:
        print "deleting original files"
        for file in [imagePathR,imagePathL]:
            try:    
                os.remove(file)
            except:
                print "failed deleting: %s" % file
                #Could probably use a verify somewhere to fix this issue..
                #since it appears that the verify causes the image to be closed.
                #should probably verify image after opening it.. force error then.
                import gc
                gc.collect()
                try:
                    os.remove(file)
                except:
                    print "failed deleting %s after garbage collection as well" % file
        
    if RedChannelOnly:
        print "extracting red channel"
        extractRedChannelFromImage(imagePathOverUnder)

if __name__ == "__main__":
    main()
