""" *************************conventions********************************
spinner zeros pointing straight down. Positive values are _counter_ clockwise from that zero. 180 is straight up, 90, to the right, 270 to the left.

Tilt follows the same convention. 0 tilt means that positive slants will move the bottom half of the surface away from the viewer. 180 tilt means that positive slants will move the top half of the surface away from the viewer. 90 tilt: right half, 270 tilt: left half.

Spin: 0 spin means the lines are perpendicular to the tilt axis. 0tilt, 0 spin means the lines are vertical.
positive spins move the lines in a _clockwise_ direction. 0 tilt, 45 spin, means the lines are pointing down and to the left! -45 spin- lines are pointing down and to the right.
"""



import math


def deg2rad(degrees):
    return degrees/180.0 * math.pi

def rad2deg(radians):
    return radians/math.pi * 180.0

def calcspinnerpos(slant, spin, tilt=0, convergence=0):
    """projected spin angle = atan(tan(spin)/cos(slant))"""
    #must convert from degrees to radians
    slant = deg2rad(slant)
    spin = deg2rad(spin)
    posrad = math.atan(math.tan(spin)/math.cos(slant))
    spinoffset = rad2deg(posrad)
    #print 'spin offset: %d'%spinoffset
    spos = tilt - spinoffset
    
    if not convergence:
        #compression.
        spos = spos + 90
        if spinoffset < 0:
            spos = spos - 180
            #not sure why but that seems necessary
        
    #print 'prior to normalization of range: %d'%spos    
    if spos >=360: spos = spos - 360
    if spos < 0: spos = spos + 360
    #print 'return value: %d'%spos
    return spos


def main():
    """mainfunc
    """
    print 'mainfunc called'
    #slant = input('slant: ')
    #spin = input('spin: ')
    #print calcspinnerpos(slant, spin)
    for slant in [45,30]:
        print "----------------------------"
        for spin in range(-100,100,10):
        #for spin in [0]:
            print 'slant: %d  spin: %02d spos: %02.5f' %(slant, spin, calcspinnerpos(slant,spin))

if __name__ == '__main__': main()
