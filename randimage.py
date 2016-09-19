import Image
import random
import imageop

#Image.init()
#new(mode, size, color=0)
#putpixel (self, xy, value)
#valrange = pow(2,24)
#valrange = 256 
#valrange = 152
#valrange0 = 100 
valrange=[0,256]
#maxx=1200
#maxy=800
#maxxy=[400,400]
maxxy=[1200,1200]
#myimage = Image.new('RGB',[100,100])
myimage = Image.new('L',[maxxy[0],maxxy[1]])
for x in range(maxxy[0]):
	for y in range(maxxy[1]):
		myimage.putpixel([x,y], random.randrange(valrange[0],valrange[1]))
myimage.save('test3.bmp')
