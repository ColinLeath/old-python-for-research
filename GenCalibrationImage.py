import Image
import random
import imageop
import ImageChops
import ImageDraw

#maxxy=[640,480]
maxxy=[1600,1200]
#maxxy=[1600,565]
maxy=maxxy[1]
maxx=maxxy[0]

pixelsPerSpaceList = [16,31,61]
#pixelsPerSpaceList = [61,31,16]
def pixelsPerSpaceFn(x): return maxy / (x-1)
pixelsPerSpaceList = map(pixelsPerSpaceFn, pixelsPerSpaceList)
#print pixelsPerSpaceList    

#myimage = Image.new('L',[maxxy[0],maxxy[1]])
myimage = Image.new('RGB',[maxxy[0],maxxy[1]])

draw = ImageDraw.Draw(myimage)
mycolor = (256,256,256)
mycolor2 = (256,0,0)
mycolor3 = (0,256,0)
mycolor4 = (0,0,256)
lcolors=[mycolor,mycolor2,mycolor3,mycolor4]

colorcounter=0
for y in range(maxxy[1]):
    #we iterate through the image by row.
    startColumn = maxx /3 
    endColumn = startColumn + pixelsPerSpaceList[0]
    #iterate through pixelsPerSpaceList and if we're on the row where there should be a line, draw it.
    #for each item in our list, see if we're supposed to draw a line in this row:
    for itemIndex in range(len(pixelsPerSpaceList)):
        quit = 0
        if y % pixelsPerSpaceList[itemIndex] ==0 and (quit == 0):
            #if so, draw the line:
            draw.line([(startColumn, y), (endColumn,y)], fill=(256,256,0))
            #draw.line((0, myimage.size[1], myimage.size[0], 0), fill=128)
            
            #for x in range(startColumn, endColumn):
            #    myimage.putpixel([x,y], 256)
            
            # #now we need to put some kind of designation at the end of each line. Let's use pixelsseparated by a pixel.
            # for x in range(y/pixelsPerSpaceList[itemIndex]):
            #     myimage.putpixel([(endColumn+4)+4*x,y],256)
            #     myimage.putpixel([(endColumn+4)+4*x+1,y],256)
           
            quit = 1

        if itemIndex <> len(pixelsPerSpaceList)-1:
            endColumn = startColumn + pixelsPerSpaceList[itemIndex+1]
    
    
    draw.line([(100, y), (0,y)], fill=lcolors[colorcounter])
    colorcounter +=1
    if colorcounter+1 > len(lcolors): colorcounter=0

#note the y+1 in putpixel statement: this does the same as the above but the pixels are offset vertically one row.
#now hal wants the lines back to back-- so change startcolumn and end column.

endColumn = maxx / 3 - 2

for y in range(maxxy[1]):
    #for every row only one line should be drawn!!! 
    #how to do this?
    
    for itemIndex in range(len(pixelsPerSpaceList)):
        startColumn = endColumn - pixelsPerSpaceList[itemIndex]
        if y % pixelsPerSpaceList[itemIndex] ==0:
            draw.line([(startColumn, y+1), (endColumn,y+1)], fill=(256,256,0))
            #draw.text((startColumn,y+1),'n')
#            print '%d,%d'%(endColumn,y)
            break
        
    
del draw
#invert the image(black to white, white to black)
#myimage = ImageChops.invert(myimage)   

myimage.save('test3.bmp')
