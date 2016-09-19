--12/07/01
--Began writing script (MyScript.ms) which will automate the creation of displays to test participants' abilities to  estimate slant. The script creates three panels, top, bottom, middle, and sets up camera and lighting. The script should also make it easy to rotate the middle panel.
--Still to do: 
--	camera position,  12/10/01 - done
--	fix lighting (create omnilight and turn off, add self-illumination)
--	
--	auto rotate/ Create rotate utility...

12/10/01
9:00 - 1:15
Backup process: backup MyLog.ms & MyScript.ms to floppy. Unfortunately floppies are notoriously unreliable. Could use zip disks or internet eventually..
Take disk home once a week.--Use two zip disks.
Each Friday, take zip disk home, each Monday, bring back other.
Worst case scenario: Lose two disks, and computers.
If lab burns down Friday PM, last backups are one week old.

12/11/01
9:05 - 12:45
Yesterday, was able to add & specify surfaces (colors & lighting) in the code.
Discussed backup system with Hal.
Discussed getting CDRW for data storage.
Began to work on automating rotation of center panel.

Automated rotation of center panel.
Got scene to look the way Barbara suggested (rotate panel around camera target, camera & target even with bottom of rotating panel).

to do:
Work with texture maps. see notes.
Remove differential at bottom of scene: set objects colors/materials equal... or something.

12/12/01
9:07 - 12:45
O.K., Shear Toggle button is working (removes differential).
Now working on Texture
A Random texture
Non Regular texture
Marble or stone
bitmap v. procedural.

(1) Made a switch in code to create two large panels instead of many small ones joined together to use for viewing textures. Did some initial texture mapping work-- need to do more

(2) Modified rotate panel to rotate as spinner is adjusted (creates animation effect). Also added check box to rotate panel about World axis. However I note in the top view that the left edge of the rendered picture (given current camera setting in the code) is slightly to the right of the world axis. Could worry about that later- spent too much time already on 'world axis' bit, I think.

Still to do: learn more about maps so that could overlay a texture map on the whole multi panel....

12/13/01
9:13 - 13:06
Went through tutorial to learn more about materials and surface editing & 3dmax interface.
Possibly will need to use a 'nurbs' surface to create one surface out of the group of materials?
Still not sure how to do it...

12/14/01 
9:07 - 12:52
Continuing with tutorial-- need to check out nurbs.

12/17/01
9:10 - 12:55
O.k. The materials approach to overlaying a texture on a sequence of colored boxes does not seem to be leading anywhere.
Possibly the newer version would make this easier. But there should be a way to do it now.

Ok, one possibility seems to be creating a two-sided material applied to a shape consisting of rectangle shapes. the back material can be a texture the front material can be broken down by panels. the two sides can be made translucent, so the back and front combine.
Now to try to code the thing...

12/18/01
9:10 - 12:55
Forgot I need to:
(1)Make splines as one shape (if possible)
(2)cap holes
(3) apply materials...

Want to know algorithm for procedural textures.
Can we write our own?/ view source.

12/19/01
9:15-1:20
Seems like if we could write our own procedural texture, no need to divide things out by creating a segmented mesh.

Note, can also use a checker map (on a rectangle shape), with a u, v, w mapping modifier applied, and the v tile set close to zero. Only drawback is that all the bands will be the same width.
We can make this an option in the program.

12/20/01
9:15 - 1:10
Ok. got the wire routed and network set up.
got the mesh panels being created in the script, with material-- Need to finish setting that up.
also need to search about procedural scripts.
!


12/21/01
9:15 - 1:00
O.k. It is up an working using mesh w/ surface- rotate utility works.
Still need to modify toggle shear, 
and to look up possibility of making ones own procedural texture.
and clean up script.

12/24/01
9:10-1:15
Does Carol have the forms? is she even here today?
toggle shear: turn bottom to black: Transparency to 100, selfillum (of back material, currently the texture) to zero? or some combo like that.

O.k. the max script seems to be doing everything I want it to do.

Found sources for procedural textures, and should be able to find some tutorials on line (more than what I found).
o.k.

12/26/01
9:10 - 1:00
To do: work on procedural texture manipulation. - random dot texture...?
Perhaps get a copy of python, vim, mpad, c compiler
Also, opengl opensource front ends.

Also, get wood texture in code.

To turn off pattern, disable back material, set translucency to zero.


to do: black, toggle, viewing from back of texture (rotated 120 degrees)

camera: same angle that we'll be at when look

(1) correct viewing angle
(2) hood
(3) self illum down..
(4) 15, 30, 45 hinge left, right
flip images..
(5) bands narrow enough to be lines.

(4) Make it easier to adjust texture version.

viewing geometry.

12/27/01
to do today:
(2) learn more about procedural textures
(1) tune script based on what we did yesterday:
 	working with mesh-based set up, allow for: 
	(a) rotating surface 120 degrees (need to flip material sides, when texturemap is turned off, or something
	(b) easy altering of color of bands/texture of both bottom and top panels
		this could possibly be done by making everything but the two top-level doublesided materials instances of common materials, so bottom panel could still be turned off, but any change to a submaterial would affect both panels.
(3) Get software from computer lab when you go!! don't forget to take zip disk this time!!
	--vim, mpad, python (activstate with wpython/pythonwin)
	& $20 to Ed Johnston on 12th floor, I believe-


ok., 1 is done
Question remaning: why does nothing show in the viewport????
I still don't know.
Still to do:
need to set up camera to match actual viewing position.
need to beable to rotate from right side of view as well as left side. Can set points at edges of FOV once FOV is set, and rotate about those points, modifying rotate utility.

all I need to do is to set the lens to 50mm then hal knows the distance at which to set the chinrest based on the width of the projected image (measured on the surface of the screen). That width corresponds to 39 or so degrees of the person's field of view.


So, I should be able to set the camera position, and place two helper points about which to rotate the plane about the left or right edges of the FOV.
for tomorrow, I'll do that.


12/28/01
9:10 - 1:10
To do today, 
(1)set camera fov to 39.598 degrees (50mm lens)
(2)put points at right and left edges of fov for which to rotate panel about
(3)modify rotate util to make it easy to rotate about these points
(4)Remove unused code / comments from script - since we don't need the box or flat panel methods anymore.

(5)procedural textures.
(6)software from lab.

o.k.
slight change of coding plans:
Let's keep the third panel, make it work for the mesh version.
(a)create button to turn on and off the third panel
(b)create button to reposition camera and rotating panel

allons!

Alright.
Need to review some basic trig for calculating positions of l &R corners of FOV
Barbara viewed some images.
We prefer narrow lines instead of bands, in this case I made them a width of .5 units
(a) She suggested making the display like telephone poles so that they do not fall off as much (in width) as they recede
(b) She suggested making images in which there is not a frontal plane, but two planes at angles other than perpendicular to line of sight.
(c) She described her & hals research study in part as attempting to make the transversals more useful cues for slant perception. Apparently the effect in stereo of having a comparison plane is quite significant for affecting the perceived slant of a surface.

(e) the health insurance saga should be over soon. on Monday I'll wrap it up.

(f) Script wise: need a better interface. Run everything from utilities? Probably need to reinsert box code to make telephone pole-like visuals.
(g) also a means of rotating the camera easily (probably utility button).

12/31/01
9:07 - 2:30 (to get the feeling of actually accomplishing something).
See the 28th for what to do.
make up and save images.
index saved images so we can know what the parameters were (cyl or mesh, width, spacing, camera position)

Everything is working- rotate panel about right and left edges of fov, or center. Rotating camera also
however:
(1)the aperture view is not easy to move into from the default settings: camera must be moved, rotating panel must be moved. That should be fairly easy to automate.
(2) if aperture view is to be used with cylinders for stripes, need to have plane behind cylinders.

The only thing to do on weds is to make images for viewing (need to index the specs of each image, however).
and to automate #1.
2 we could worry about after that.
Procedural textures after that.

1/01/02
9:15-1:03
Ok, made it so it is easy to switch to aperture view (3 planes) and back. (switch in code called threeplanes)
made 32 images for hal, varying width of wide stripes by half, and comparing aperture and non-aperture views.

now, I guess it is proc text time.
yes, and hal found a problem with the proc text mapping- I'll have to try to figure it out tomorrow

2002/01/03
9:05 - 12:55
to do:
make new displays, hinged from middle, 2 panels only, telephone poles, separation is the average of the narrow and wide used yesterday, tilting forward, and tilting back.
Also, see if other textures besides the cellular seem to work well on the surfaces we're using.
Stone, marble, dent, who knows what else.

good maps:
dent - however, horizontal lines appear
gradient map is very cool- but stong default horiz. - set w angle to 90 and this is no longer a problem. Note: UVW1 map applied. zalign, box map, lwh 10,10,10
marble with a size of 10 works fine. but has scintillation
noise works well. size 10, regular (not turbulence/fractal)
perlin marble is impressive... different possibilities. tiling of 10, different colors- purple, green.? Levels of 1.. it does scintillate, though.

2002/01/04
9:10 - 12:55
Don't forget to give money to Ed Johnston
today, continue working on maps. and perhaps, create images for showing again.

splat, very nice
stucco, could be good as well. It is very responsive to blur.
size 40, color 2 purple, threshold .43, iterations 6.
using acquire absolute seems to allow me to match top and bottom panels even with the huge size difference!

Turns out I was using the elements of materials not materials themselves to try to create material looking things.
The Oak material is good- rotated 90 degrees. w

2002/01/07
9:20-13:07
O.k. was working on setting up network rendering.
Steps needed to set up oak texture:
(1)get "oak quarter sawn" material from material library
(2)set selfillum to 100
(3)make a copy of the material, and rename the copy.
(4)apply the two materials to the two panels. To turn the bottom panel off, set self illum to zero before rendering.
(5) Apply UVWMap modifiers to each surface.
(6) Set mapping to planar.
(7) l,w,h should be  - 45,45,45 seems close to what I was using before. tiles all 1
(8) In the material editor, for the oak map (click the M next to diffuse), set the W angle to 90.
(9) select acquire in one of the uvw maps and select the other surface. Choose absolute mapping.

that's it.

--Got network rendering working, which rocks!, now all jobs can be run on other computer and picked up when complete..
Still some problems sharing/referencing map jpgs with unc paths, however.
also, the net render is putting a bunch of 0000s at the end of names, eg tex210000.png

2002/01/08
9:20 - 13:00
I ran through the materials in the material lib, drawing from all materials, not just ones that matched our barred design, saved renderings, and showed these to hal.
After that, he mentioned he wanted to attempt to do something about the tendency for the two panels to be visually joined, even when tilted.
(1)make sure there is an offset between bars/boards in fence. Could also use bars of a differing scale, perhaps.
(2) put a black line of separation between the two panels
(3) experiment with a point source of light.
(4) also, rotate things at right/left edge.

2002-01-09
11:00 - 14:45
Today, continue to work with textures and with the gap and with shading using a point source. Save some suitable images.
O.k. I played a lot with different possibilities using a gap, using various types of lights and textures.
effects I believe I noticed:
(1) With a light and strong shading, the predominant effect seems to be that dark regions recede and light come forward
(2) There also appears to be a problem with distortion if you look at image in a way different from way picture was taken. Especially notable in oak bump map.

2002-01-10
9:20 - 13:05
(1) to do: decent ambient light without strange color.
(2) problems with rendering reflected light, problems displaying radiosity.

--
Hal looked at some of the displays I made yesterday, and continued to work on  figuring out how to keep things from fading into the gloom. The trick is to set the abient light, under render..environment. to 70,70,70 -- a dark grey. The light source itself is 180, 180, 180, a light grey. For materials, diffuse and ambient should probably be kept locked.

That problem solved he set to work on lighting techniques.
--
research questions:
(1)is there information there?
(2)does the visual system use it?
---
goal for this display:
o to not have slanted surface dimmer than frontal surface?

somehow, it is possible to place the omnilight such that the brightest reflection is at the center of the tilted surface, and not on the frontal plane? no...

--
If I were designing a visual system, I would have it use commonly available sources of information. Are there previous examples of uncommon stimuli being usefult to the visual system? Are light gradients on slanted surfaces common? Are sufaces without horizontal cues common? Was the stereopsis issue Barbara was working with a common visual occurrence which would have to be dealt with by the system?

Is there information from light gradient differences?

Horizon shading, where the front is bright and the back fades into the gloom. There is effectively a slant that we are used to seeing at least in computer genned images and lit shots- but perhaps that is the simple phenom of dark being perceived as further away than light.

Hal was explaining that phenomenon, and brought out some demonstration photographs, one of hills, the other of pits in the ground. Turned upside down, the hills should be valleys, the pits, bumps. He saw this, but I did not. Does cognition affect visual perception? What sort of less than instantaneous phenomena affect visual perception? What context cues from the past may affect perception? What kinds of learning affect perception?

How can one measure perception that will not allow the bringing in of cues from the past or learned techniques?

--
the lightness or darkness of one surface is not the issue, it is whether gradient differentials give cues, or just gradients?

2001-01-11
9:20 - 1:20
Today talked with hal about different things.
Hal looked at images produced by shading and became interested in the effect of shading on perceiving small slant differences.
I made up some images and looked at them in the dark room.
There definitely appears to be an effect of having a comparison surface.
There might not be any point to having a gap between the surfaces since there aren't any horizontal lines that tend to appear connected.

There is a problem with ridges in the shading.
The differences work best when the light brightness creates a difference along a large portion of the edge. If the light only appears at the far right edge of the tilted surface, there is less of an effect and less of a perceived difference between different angles.

2001-01-14
I'm 26!
10:00 - 13:45
today, let's work on the shading issue- the ridges in the gradient.
Also, narrow the gap to .25 or less (currently 1)

meng
Bosco

To work on:
(1) Continue to work on shading to find out what gives best effect and what gives what effect. Try different light positions, and different amounts of slant, different colors, dif textures.
(2) Look for a more technical guide to 3dsmax, "The algorithms behind the image" discreet site, or elsewhere.

2001-01-15
9:07 - 12:52
see 1, 2 from yesterday.
-
made many displays - displaying effects of shading combined with textures or bars.
also investigated trying to find more detailed descriptions of how rendering is carried out.
Posted to web board - question 
should refine that question tomorrow. Looking for more details, equations, something like the old renderman documentation.

tomorrow can look at images created.
refine question.
perhaps work on tool for measuring perceived slant.

2001-01-16
9:34 - 13:19 (more)
My dad's birthday!
Today, continue with documentation work - check/refine web board question.
look at images created.

2001-01-17
9:20 - 13:00 or less
today installed a 4GB external scsi drive on g6-200-2, and moved image files and others of g6-200, making available 489mb of space. Also updated emerg. repair disk for g6-200-2
Tomorrow--python script to display images.
Also installed ALICE on g6-200, but it appears to not be able to display full-screen images. Should check graphics cards.

2001-01-18
today spent most of the realizing we needed to properly terminate the scsi drive I installed yesterday!!!
Got python to display an image, but need to do something with pygame, probably.

2001-01-22
9:30 - 1:55
it is a beautiful day.
Let's get to work.
got image display working.
now working with pyopengl to display a 3d rotating thing on top of a background.
See texas.py demo in demo/gle

2001-01-23
9:25 - 12:45
continue with yesterday's work.

2001-01-24
9:05 - 12:50 
Work on getting background to display in pyopengl, and then rotate an object in front of that.
try textured things that have horizontal.

--
2001-01-25
9:20 - 1:05
small angles with horizontal lines - cloth texture. 5, 10, 15 20
with and without bottom.
perspective information at edges

O.k., we're making new displays...
the key data to remember is that we're using a light at the right edge of the display level with the camera target.
shininess:7
s strength: 39
self illum: 0
r0
g15
b0

there is a .25 unit gap between top and bottom surfaces.
(those details are currently not in the script)
There is also a UVW map on top and bottom panels. See entry on 1/07 for more on that.

Also: in rendering..environment, the ambient light level is set to 70,70,70
In material editor, diffuse and ambient are locked.

for what hal was looking for (blue cloth) use fabric2.jpg

bc01 - 5 deg + bottom
bc03 - 10
bc05 - 15
multiplier of 255,255,255 light of 1.3


bcarpet- light mult = .9 currently


no need to use 48 bit- just takes up more than 2x the disk space!

24 bit/48bit vs. truecolor?

2002-01-28
9:15 - 1:00
Today wee need to get an image loaded as background in a GL window.

O.k., the scenario is that we have a program that will display texas and our background, but not at the same time... we need to learn the different things that are going on in this program to figure out how to combine them in the way that we want... Should search on internet to see if anyone is already doing this. Should also see how hard it is to do what we've done in alice--might want to get a better video card.

Could use rotating features of texas to render scene---
well, now I probably know what to do to draw something that rotates in front of my background and to have it respond to keypresses and how it redraws.. Excellent. Just positioning issues then.. and concerns about how long redrawing the screen will take. I'm here 15 min too long again!. Let's go. need backup disk. Left mytexas.py displaying not texas but my plane....Yeah!

2002-01-29
9-3:07 -- but I've got a rotating thingy infront of a background. I've got an eventhandler handling script for arrow keypresses. I've learned a bit more about programming.

2002-01-30 wednesday
9:15 - 13:00
today should get display and rotating thingy working!! using nehe 7...

tomorrow - work on making predominantly horizontal images- wood patterns running horizontal

2002-01-31
9:01 - 12:46
creating displays with combination of predominantly horizontal lines and shading.

now, create three-panel display- just like last one with cedar boards.. this is because with the horizontal cue- the change occurs least along the middle line that we were looking at.

I should automate the application/creation of uvxwmaps and lights!!!

network rendering is popping up a kinetix window. how to stop?


Instructions for setting up materials on surface--
(in addition to those found somewhere above)
o the materials I want may be in the material library.
o still need to do uvxw map application--- get that in script.

2002-02-01
9:15 - 13:00
made different views incorporating 3 panels, and also three panels with the middle having silhoette perspective. The perspective view (wedges of blackness) seemed to influence perception of depth-- the 3panel view without perspective seemed to me to reduce perception of slant, because the two frontal panels cut down on the viewing of the edges of the slanted panel, and it is at the edges that the greatest perspective effects of horizontal lines occur in this display.
Monday, will make narrower 3-panel displays. I suggested giving viewers a rich picture and asking them to estimate slant, so we would have a way of determining the best slant perception that was possible monocularly. Hal mentioned that having a longer surface reduced slant perception--if a slanted surface was stretched out, the slant appeared less. So Hal suggested making a display of 3 squares, one on top of the other- the largest 3 squares that will fill the monitor when placed on top of eachother. The middle one slants.

2002-02-04
9:15 - 1:15.
working on 3-panel display of squares.
O.k., we've got our display of squares scripted. For some reason, the rotate utility needs twice the angles as all previous displays. Possibly I broke the script and should generate a new regular display to see if they rotate properly?
At any rate, currently for the display of squares: 180 =90 in the rotate util


2002-02-05
9:15 - 1:00
copied all images from maps over to c drive on g6-200-2. This should reduce problems encountered with netrendering. ideally, would just use all libraries & graphics from networked drives.

got donut-- in script;
question is do you have misperception of axis of rotation based on orientation of texture.

2002-02-06
Made utility to rotate axis about which panel rotates. Had to move things around scene to accomodate large angles of panel.
Tomorrow: take ethics online test, then come back and think of ways to animate this change.

2002-02-07
0910-1255 
online course at http://cme.nci.nih.gov
has been completed.

comparison series with grid like pattern - tile, berber carpet.
yesterday texture rotated
two slant angles:
90 to 45
whole thing slant angle 

tomorrow do two more of the same, with the berber cloth and green tiles.

--
3dsmax user meeting
7-9 pm
thursday feb 7th
12 w 21st st 12th floor.

2002-02-08
0915 - 1300
The user's meeting was quite impressive. No, there must be a better way to describe it. But first! Lettuce render.
Need to find way of backing up materials created, and scenes which it would be good to keep copies of.
No lighting in donut series...

perhaps what happens in slant perception is that the eye needs to pick up something to run along that goes the direction of the slant...

is the horizontal component of the berber carpet stronger than the vertical?
Compression issues as well

2002-02-11
0910-1255
What am I doing this morning?
Did I write it down in my pad, and not here? I believe I was going to render a set with a smaller grid.

O.k. went over displays with smaller grid.
for tomorrow, start working on python script, most likely using pygame, to display rendered images and use line to indicate axis of rotation.
Great!
Once we have rotating line, need to have randomization without replacement (randomization of a list of files), and data storage

2002-02-12
0915-1315
work on python script!
the file is chimp.py in pgame docs examples

2002-02-13
0915-1300
O.k. The pointer problem is under control.
Now, need to be able to handle image randomization and data storage.
So, we'll start with finishing up the controls and use of a directory, randomization & recording of data.

2002-02-14
0915-1300
-1317

2002-04-26-1003



Yesterday was the campus staff & faculty meeting, but I missed it!
This a.m., a firedrill- should be right now, 9:20
Ok, the basic functionality is in the script:
	issues: hal might like a resume function (or some such thing) if problems in middle of trial require a restart.
	also, if data.csv is locked, program won't run. Should perhaps pop error box. file name is spinner.py, requires pointer3.bmp and inputbox.py. Appends data to data.csv

2002-02-15
0915 - 1300 (may leave early to get to metropark, NJ around 1:00-- don't know how long it takes!)

Today, need to get script running on g6-200-2
script is running on #2

(1) need to find gvim executable to install editor on #2
(2) need to render more scenes at different tilts.

what was the trick to make it easy to do that? Could I rotate camera and reshoot? Why not?
the trick I was considering was leaving texture unchanged, and rotating whole panel. Previously, I would rotate the axis of rotation, and the texture. we'll see.

2002-02-19
0910-1310

Let's get those last series rendered.
The tilts we want are (90 is vertical)
112.5 (113)
67.5 (67)
45

to get these we will rotate camera to:
-22.5 (-23)
22.5	(22)
and
45 degrees respectively

we will do a series with cedar
and with 
uvwtile 5 marble tile
Berber also?--we'll ask

Need to make rotate utilities handle half degrees?? look into that.

finished rendering and tested collecting data on 20 of the scenes.

to do: 
o standardize names so they can be sorted alphabetically by texutre then by tilt, then by spin.
o make spinner program record data which matches name spec. 0/180 is horiz, 90 is vertical

2002-02-20
0920-1337
fixed script so spinner is randomized on first appearance, and so that it asks for directory name
tomorrow:
(1)make script get tilt and put in data file, and possible ohter variables.
(2) run through whole set practice?
(3) date/time of each trial

2002-02-21
twenty fifth is monday, when library book is due.
0915-13:10
to add to script:
(1)Date/Time written out for each trial.
(3)parse file names to write out tilt as well.
find sl_, take next three digits as tilt
(2)run through whole set.
(4)also write out whether cedar or gtile

note: for all recent tile images, we've been using a uv tile of five. to make dealing with names easier I'll remove the _uv5 from file names. Note: this makes duplicate names. Should add _uv1 to files in the old tile directory...

(5) also separate out digits off file name for specifying spin

--
so, what should we do with data when we're done with it?


(6) tomorrow work on learning how to graph data appropriately

2002-02-22
0920-13:10
(1)perhaps add to script calculation of diff, and abs_diff - done
(2) Got graphs working in new version of excel.
to do:
Create cylindrical grid.
make distance between lines similar
o back up data as well as script!
o render set with 30 degree tilts.

2002-02-25
9:40 - 13:25
Today we're going to re-run through trials to get more data. And then graph results again.
We will be breaking down data-- see scratch paper, in addition to old graphs of diff v spin and diff v tilt.

Consider using word for notes so that graphs can be pasted in this log and not lost... I probably should do that . or find another way of organizing things.

Modified script to beep when enter key is pressed and also fixed bug in which -1 wasn't being written out if enter was pressed without using spinner. Also made it possible to go back and redo images.

Began working on complex graphs 

need to make spin graph stronger

2002-02-26
0915-1310
Finish up first graph, and then ponder better way of working with data?

o perhaps we should have script write out spins...
o tommorrow, continue working on template- then run through old datasets with query! and that's it!

2002-02-27
0918-1300
it is wednesday
is anything new?
...
yes, actually.

o today we're working on the template still 
finished template and looked at data graphs with hal.

tomorrow:
render 40? images
90 tilt set of cedar and green tile with slants of 30 and 45 degrees!

2002-02-28
0915-1255
o render new displays.
--dcedar90-45sp_030sl_090t
--dcedar90-45sp_045sl_090t
--dgtilr90-45sp_045sl_090t
--dcedar90-45sp_030sl_090t

o backup material lib... should make own matlib separate? done: colins_material_library.mat
o backed up scene in use: _mydonut1.max

30 deg is probably not enough slant

Looked at these less slanted displays---very interesting.

-->discuss below first.
(2) the small slants make more visible the tendency to match the spinner to certain aspects of the display.
	-the task becomes almost a simple matching task(?)
	o perhaps include arrow(s) on pointer to indicate direction of slant - have arrows point towards end of surface furthest away from you.
	--- so, we also, obviously need to render and have surface slant in opposite direction.

--noted that perhaps not enough compression info on wide boards- would there be more on narrower boards?


o one interesting experience was that I got two surfaces right after another--effectively seeing it slant-- and yet how did I specify the axis?

(1) Should probably be working with plain grids and lines to avoid texture artifacts:
	o the green tile seems darker in the middle, making display seem folding in middle.
	o the boards: the darker board always(?) seems to slant more than the rest.

finally there is a fine line in one of the displays.-cedar boards with a spin of around 40?


so, what do we take away from this? any hypotheses?
(a) People can detect 30 deg slants-- the fact that the slant is there and its direction. -- threshold research.
(b) But people will believe the surface is slanted around the incorrect axis by focusing on certain dominant cues of the scene. with the boards this is just the convergence of the horiz lines. with the tiles, it is perhaps the compression of the squares and ability to compare the size of an edge of a square on the edge of the circle.

(c) anything else?
-- even if they actually see the surface slanting about its axis, they will incorrectly indicate the axis of the resting static display.

Is there anything new about that? Can this info be useful or add to anything else in any way? Beats me.

questions for hal: could he always see the surface was slanted and see dir of slant?


onward:
(a) look at data
(b) find an isotropic texture with things going on at different scales.


2002-03-01
0945-1350
today worked with materials to create a material to display a random texture, lines on the random texture, and lines only. The composite texture will spin.

Monday will render some images with these values for observation in the dark room. backing up matlib.

2002-03-04
0845-1230
see above
today:
completed constructing material and rendered three sets:
(1)Texture only 
file://localhost/X:/dsplat90-45sp_45sl_090t_tx
(2)Lines only:
file://localhost/X:/dsplat90-45sp_45sl_090t_li0009.png
(3)Texture and lines:
file://localhost/X:/dsplat90-45sp_45sl_090t_tl0001.png

made the following observations:
(a)With the texture, I can see that objects at one end are smaller than object at other, but I don't see slant?
(b)I do see even when no slant is obvious, that there appears to be more space on one side of the pointer than the other side, even though the pointer is in the middle.

(c)...Hal is wondering why, if one can cognitively pick out cues that let you know that the surface is slanted, why doesn't the surface appear slanted? What other cues are telling you that it is flat?

--so, we discussed ways of reducing the effect of accomodation. I mentioned small lcd displays. And also just printing out the texture on paper. We did the latter and found real paper to appear about as flat as the same projection on the display.

tomorrow: find way of making polka dot texture in python or 3ds in which parameters can be varied.

2002-03-05
0910-1255
aye yae yae, polka dot time.

--angle of view of surface also affects perception of slant--according to hal who was experimenting with a large ceiling tile yesterday.

o in future - add transparency to stripes...

o give participants substantial practice, because hal believes after some practice, participant will settle into a steady way of answering.

Today: got a polka dot pattern that looks fairly like a surface.
tomorrow using that pattern, generate surfaces all slanted at 45 deg, but with tilts varying from 0-180 in 15 deg steps or less frequent (if can't animate changes in tilt-- well I can by rotating camera.)

tomorrow, also need to get polkadot pattern in with other code. Perhaps need to start modularizing myscript.ms to make things easier to read/organize/access/use.

2002-03-06
0925-1310
o creating renderings of polka texture at different tilts.
o problem: the circles in the display allow pointer specification to be a simple matching task: match to length of ellipse axis.
--other problem: 3ds max had problem handling 2000 circles. Possible solution: to reduce the number of steps used in creating the circle spline shape.
o so, now look at data from splotches (splat)
o actually - we could try using triangles, not circles.
--no that's not really better than the splotches


(1)Look at data
(2)add a fine grained speckle to the whole surface
(3)make stripes somewhat translucent--see through.


2002-03-07
0915-1300
see 1,2,3 above.
perhaps do series with only small spins, because large spins may present ambiguous displays and create a context which adds variability to participant responses.

add to list:
(4) adjust script to output from 0 to 359 degrees
(5) adjust pointer to have a small arrow for indicating direction of surface furthest away from viewer. (direction of slant)

-what would people do if told to specify axis of tilt of a flat surface with spinning lines on it.

see a slanted surface
which way would a marble roll
use pointer rotating about center with an arrow at one end- about half the length of the old pointer.

(6) offset lines so does not go through middle -- done- need to save material

2002-03-08
0920-1330 - extra half-hour
0030 over
see 2,3 above

(7) learn how to use include files-- to make script management easier!!!!

--does participant have normal vision?
--dominant eye test
--eye chart test
--cash in envelope.
--receipts, consent form
--data confidential
--reading instructions

tomorrow: double-check images rendered, correct file names, change filename parsing in script

2002-03-11
0935-1435
0115 over
-checking images rendered, naming scheme, and filename parsing.
--there were many problems with images rendered:
all had to be re-rendered; the pixel aspect ratio was wrong for all but the first two, and the first two had strangenesses in their materials.

The program spinner.py has been modified to parse from the file name useful data.
In addition the spinner program will convert spinner values if more than 180 away from the actual tilt.

2002-03-12
0855-1620
0340 over
showtime
Joanna Olewicz due at 0930

2002-03-13
0940-1540
0225 over
currently total 0750 over
to do
go through image set again..

Generated all graphs...
Excel crashed once.
not much else to write at this point?
backed up data, spreadsheet, database.

0900-1245
It would probably be helpful if I did not describe things in terms of extremes-- need to be more careful in how I interact- not saying I don't care, posing things as questions. Hal must practice to interact with people in the way he does.

Today, finished graphing pilot data.
backed up spreadsheet and this log.

For monday, I can write up instructions for investigator- and perhaps think of other things I forgot to detail. 

2002-03-18-0939
0930-1315
Today, I will continue working on writing up instructions from experience running a participant.
make note of hal's idea of surface with circles:
make circles, keep track of placed circles, for each randomly generated circle, before drawing make sure it is x distance away from every other circle in the list.


o pursue alternative to splat texture- so we know how it is constructed. dispersed disks

2002-03-19-0903
0900-1245
o continue working on dispersed texture... it should be working, but there is some wierdness.

2002-03-20-0926
0920-1305
There was significant wierdness with the max script: inability to delete-re-initialize an array. and mypolka.ms not running unless run twice (though gc()) at the end solved that issue.

So, the texture generation program works. Currently set to randomly place points at least 12 units apart. Getting it to place 300 took some time, given a field of 200 by 300 units. The randomly placed circles of color 192 and background 64 are very nice to look at through the aperture.

The script makes it easy to choose between circles and ngons. The generated coordinates are saved to a file, so they do not need to be generated each time.

today
o work on putting a pattern across whole surface. I imagine a spotted plane--transparent, but with more opaque black spots. That sounds exciting.

randomness is very nice to look at - I'm not sure why it is not used more in design.

o also try different shapes/forms, different colors and textures. The goal being something that can be used to replace the splat texture we were using. So no reason to spend weeks on this.

o hal also suggested looking more at three-d and preferably two-d noise functions...

-pentagons

o for tomorrow, work on rending different scenes combining noise function and shapes, perhaps...

2002-03-21-0922
0920-1305
Working more on getting better control of display and working on last item above.

bg is 64
mat is 192

2002-03-25-0937
0935-1320
more renderings of the textures.
we're close to the lost dnoise16 with 
size=2
high .6
low .1

levels 10

They do... they look exactly like oyster crackers!


2002-03-26-0946
0945-1330
looking at scenes created with med and small pentagons
using material dnoise16_8 for mesh panel


2002-03-27-0928
0925-1310
look at hal's data for comparing small and medium pentagons
also work on adding stripes to display!!!! then we're basically ready to run people again---maybe we can take care of this quick and get on to the next adventure. Perhaps it will not be as straight forward as it seems. It will be a good challenge to work with participants...

dnoise16_8, opacity has been set at 30 with an environment background of ?? (in script, I believe)

tomorrow and friday:
Work on procedure to generate displays
focus on the work of automating random generation of 
displays---a new random sequence for each ...144?? my goodness.
And then perhaps work with smaller level surface buffing.

2002-03-28-0932
0930-1315
did random pixel generation with python
got material working for lines, texture, and texline displays
wrote utility to spin panel
tomorrow:
automate creation of 144 displays --randomizing pentagons for each display.


2002-03-29-1036
1035-1420
ok, we have all the pieces-- should have it working on monday!!


2002-04-01-0944
0920-1325 --20 over
spoke with hal about raise--or he spoke with me, and by July 1, should be up to $17k/yr--which is only an increase of $80/month before taxes, certainly an improvement.

Today- get the rendering component of displaygen script to work. ok!

problem: netrender from maxscript is not working--possible solutions:
(1) Find out why
(2) cause everything to be created in separate frames: drawback: huge file is generated--filenames must be genned from imagesequence: i.e. image0001= "slkfjlksaajlkajsakfjaslkj.png"

2002-04-02-0841
0840-1225 - 1235 ten over

(1)should work on netrender issue and polishing script--the file actually probably won't be so huge.


notes from book _texturing and modeling a procedural approach 1994:
p89 Bombing technique (Schacter and Ahuja, 1979)
fBM p 284
p98 the art of noise.

The midpoint displacement method (Fournier et al. 1982) p 80

(1) issue about knowing where one is in the list of images: how many left--have python put text to screen when a number is pressed.
(2) encoding file information in file itself, as opposed to file name: tilt, slant, spin, texture.
(3) Generate sequence of isotropic textures, just like yesterday, but isotropic.

2002-04-03-0929
0925-1305 - 1314
(1) Set up rendering also just like yesterday, but combination of lines and texture (tl)--no sweat.
(2) the naming issue is hideous, because it appears we cannot store data easily in .pngs.. must continue to use filename, and change parsing routine-- if we ever want to use old images, must get back old parsing routing.
Another possibility is to put every image in a database- a zodb, perhaps--or use some other way to standardize the way image properties are stored-- no good idea. For now, forget old images (should get rid of them), and modify parsing routine.
(3) script will now parse new image names correctly and will also display position in sequence in upper left for 1 sec if you press the tab key.

40 minutes over to date
2002-04-04-0925
0920-1305 (or less)
to do:
(1)run through line set
(1.5)work with hal and my data
(2)run through texture set
that's it.
(3)more than 90 degrees off classify as reversals and don't include data in average.

for tomorrow, continue to work on template, and should get lines and texture data analyzed (put in template, make copy).
(2)run through texture screens myself.

2002-04-05-0927
0920-1305
see above!
(1)could use assistance attempting to understand data.
(2)let's look at textures.
(3)analyze texture data.

for monday:
(1)do regression line graphs for texture data
(2)run and analyze tl data
(3)contemplate methods of data analysis
(3) contemplate number of trials
(3) contemplate 30, 40, and threshold.

2002-04-08-0935
0935-1305 - would just about use up all my extra time..0935-1320
see above:
(1) do regression line graphs for texture data
(2) run and analyze tl data

2002-04-09-0943
0940-1305  -20  (only 5 extra min)

2002-04-10-0926
0920-1305
working on data issue, issues of spin..

2002-04-11-0925
0920-1305
What are we doing today?
so, we're going with no noise texture--just plain stripes. Need to save display to be that way...

then make diagram containing specification of physical layout of scene rendered to produce displays.


Make edge of donut correspond to edge of display

2002-04-12-0940
0940-1325
issues:
spinner.py needs to handle practice trials, 
group trials -- intermission.
Calibration image.

2002-04-15-0937
0935-1320
Continue work on script and refine display production..

programming task is now a bit more complex.
we need people to be able to save their session data and resume where they left off.

Session will be doing the following:

 
 
Ok--everything but resume appears to be working...

should check to see if there is a new pygame and text manip tools, but basically, it is doing what we want...
and just to be aware of what's out there.
Tomorrow--suspend and resume:
escape key should have a save option.
how will we store individual's data? probably in individual data files in data directory. So everyone... yes.

question (1) first time, or returning player?
easy, no sweat--save list, save n, and resume where left off. sep data files, and saving list are all we need to do.--saven in an easy place.


also, set up session.py, not class to do blocks like hal wants..
rename session.py
 
 
o flush datafile at end of each session and each trialblock time?--yes datafile is written at end of each session, just need to add a flush to the show calibration screen function.


2002-04-16-1155
0930-1315
spent a fair amount of this morning getting so I can use this computer to develop the scripts for work.

o let's first work on the 
o intermission issue--key

intermission issue resolved by getting events after waiting (clears queue)
and also check to make sure pointer is initialized before proceeding. (prevents subsequent enter keypresses from advancing one too far ahead)

Now--save and restore.
save data using username and label.
480 trials--480 images in one directory.
Can store data in a username.label file --label will distinguish between trials.
Restore will ask for username... will have to think about this more later.


2002-04-17-0926
0925-1310 [1355] 45 min over...
see above.
what functionality is needed for a suspend and resume?

(1) ability to resume--program should ask:
first time user? y/n
--> y-> get user name, other info
    ->  ask for user name -- question-> how much can/should user be trusted?
    -> verify that user name has a resume file- if no, ask again
    -> load list of imagefiles, and n, participant name, etc.
    -> continue where left off.
    --> when finished, write users data to a ucolinleath.dat file.
        ->each dat file will contain participant's data which can be loaded into database.
--> the escape key needs to have a catch on it?
thank you screen?

Main menu:
    practice sessions: -> 12 trials of isotropic tecture for instruction & specific feedback
                        -> 12 trials of line display- (randomly selected) a range of spins, instructions should include the info that the lines are being spun.
    Session 1: 2 blox, 2 * 60 = 120

the setup, instruction, and practice blocks may take the entire first hour.  


so, what will we do with participants' data?
probably save it in files like uUsername.dat--one for each user.
o have script automatically back up files when done with them?(copy to different location?--possibly d drive on g6200.
so the only tough issues really are saving and resuming.

o    user account for participant- particpant account..

got sessionman.py fleshed out...
now need to work on details-session loading, checking etc... everything should be straightforward. no complicated logic left.(?)

2002-04-18-0926
0925-1310 :45 over.

pascal record or c struct

class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

1608--quite a bit over, but to get it for the most part working...


o is old data getting erased by program when checking file existence? need to check!!! and also make back up of user data

2002-04-19-0923
0920-1305 or less  10 over..
see above, need to actually store imagelist and n if esc key is pressed when n < imagelist.count

fridays hal is gone until when? no need to have lights on until that time.
at 11, we'll turn light back on


prb: user could endlessly resume last session.--need to mark a user as complete somehow??
talked to hal about specs..
wants intermission screen to say you've completed block x of x, continue or break? -and then save the data there.
1314

o spinner too fast

2002-04-22-0932
0930-1315

today- we need to 
o get resume option on intermission dialogue
o second intermission dialogue telling when one can proceed.
o "you have completed your xth block of y, to continue with a new block, wait (approx. 2min) until a new screen pops up and proceed. To save your data and quit now, press [esc]. "

o also for first time users, need to enter and save full name, acuity, dominant eye, experiementer.
o use a tk window?, a web form?

o calibration image. - done


Still to do: 
o finish intermission dialogue
o first time user data entry
o put user data in a separate folder than programs?


2002-04-23-0925
0920-1305
o no need for first time? question--- have secret key press for experimenter to get to FIRST time data entry sequence.
o now: press f12 to get into first time user mode
see above.


o really need to concentrate now on getting sessions to appear as one long block.
o can do kludges based on labels. O.K.

o problems left: on final display of intermission screen, need to change options-- no continue!
    o erroring on completion of final session. with labellist out of bounds..how?

tomorrow:
 o still have problem with quitting/resuming on final intermission screen of a session
 o still need to do initial data screen
 o still need to label calibration image

2002-04-24-0920
0920-1305
finished fixing quittting/resuming bug.

o initial data screen
o label calibration image. --done

want to use a tk form for experimenter data entry---
alternative: input boxes sequentially, then display all data to see if ok. then save.

o still to do: the break is over
    o participant account
    o on quit, copy data to g6-200-2?
    o thank you screen...

2002-04-25-0930
0930-1315 - may try getting off right away to city college to get appointment with chair of department.
o still to do
    o participant account-- password
    o on quit, copy data to g6-200-2
    o thank you screen

o how to have python write to error log incase something goes wrong??

--to do tomorrow:
o to data save dialog: "If you want to continue, press enter-- to return to main menu press enter- something like that"
o 

2002-04-26-0947
0945-1330
What am I doing?
o various things
o check spinner constancy
o practice session images need to be 120 randomly selected images from main directory

ongoing:
o summary of old results with lines
o document code so hal 4 years from now could get a clue.

That's it.

o spinner speed variability corrected using pygame.clock.tick()
o instruction: initial position of pointer is random added to instruction document.
o practice session 120 random images, done

to do:set up other sessions. practice directories.

2002-04-29-0929
0930-1315 -1328
o stripes to 96, 128 and tiles - done! tile redrawn.. lineinverse4.bmp. Material readjusted: dnoise_8_16_5
then render

o displaycalibrationscren.py

to backup:
    lineinverse4.bmp
    colins_matlib.mat
    noisescene_small.scn
    showcalibrationscreen.py
    gen144.ms
    
2002-05-06-0919
0915-1305
working on tile issue...
and then?
render displays

2002-05-07-0924
0925-1310
o to do, have script set up materials -- put dnoise_16_5 in known slot in meditor. Load pentmat, etc.

o does color look darker at far end?

ok, we're getting ready to launch rendering of 480 images.

backup what you need to backup first:

then go!


2002-05-08-0957
0930-1300
Well, I came it at 1700 yesterday and found that only the first 20 had rendered before an out of memory error caused the thing to crash.
I put in a gc() [garbage collection] call at the end of each rendering loop and the script ran fine after that.

now: get sessions set up as specked, and then run.

2002-05-09-0915
0915-1300!
working on making gen144 script more flexible, so I can specify images to be rendered by details (spin, slant, tilt), instead of by using ranges of numbers: for n= 1 to 100 do.

Also doing work on hood to prepare for study run.

2002-05-10-0920
0915-1300
gen practice images/finish list approach, then work on continuing projects.


You don't need to explicitly declare variables before you can use them. MAXScript creates an undeclared variable the first time you use it, and initializes it to hold the special value undefined. It defines implicitly declared variables as local if you use them for the first time inside a function or block, or as global otherwise. There are language constructs that let you explicitly declare and initialize both kinds of variables and it is good practice to use these to be sure what kind of variable you have

function returns value procedure operates on ____

2002-05-13-0928
0928-1313
iso practice images genned nicely
now select line images.
then, ongoing projects.

Actually, I think what I'll do first is set up the data analysis templates.

what to do with data?

for each person there will be a run1 & run2. These individual points will probably be averaged to create what is used for final data analysis.
15 min for computer to run 120 practice images.



still working on settin up data templates

2002-05-14-0921
0920-1305
let's work on getting here earlier!!0900-1245 goal on non-carmen days.

still working on data templates should finish today.!!

I need a tool for programatically graphing data.
spss?
statistica?
mathematica?

paste script used in here-- with fmt function.,

Function fmt(str, args)
' ###########################################################################
' #
' # file:
' #     fmt.inc
' #
' # description:
' #     fmt function.
' #
' # author:
' #     Uwe Keim, keim@zeta-software.de
' #     zeta software GbR, Germany.
' #
' # version:
' #     2000-01-02 Uwe Keim   file created.
' #
' ###########################################################################
' ///////////////////////////////////////////////////////////////////////////
' // fmt function.
' works like the printf-function in C.
' takes a string with format characters and an array
' to expand.
'
' the format characters are always "%x", independ of the
' type.
'
' usage example:
'   dim str
'   str = fmt( "hello, Mr. %x, today's date is %x.", Array("Miller",Date) )
'   response.Write str
    
    Dim res     ' the result string.
    res = ""

    Dim pos     ' the current position in the args array.
    pos = 0

    Dim i
    For i = 1 To Len(str)
        ' found a fmt char.
        If Mid(str, i, 1) = "%" Then
            If i < Len(str) Then
                ' normal percent.
                If Mid(str, i + 1, 1) = "%" Then
                    res = res & "%"
                    i = i + 1

                ' expand from array.
                ElseIf Mid(str, i + 1, 1) = "x" Then
                    res = res & CStr(args(pos))
                    pos = pos + 1
                    i = i + 1
                End If
            End If

        ' found a normal char.
        Else
            res = res & Mid(str, i, 1)
        End If
    Next

    fmt = res
End Function

Sub modchart2(startrow As Integer)
'
' modchart2 Macro
' Macro recorded 5/14/2002 by Valued Gateway 2000 Customer
'
' Keyboard Shortcut: Ctrl+m
'
    Dim pos, n As Integer
    Dim Series As Object
    Dim valuestring As String
        
    pos = startrow
    
    'ActiveChart.PlotArea.Select
    'ActiveChart.SeriesCollection(1).Values = "='f960'!R242C8:R261C8"
    'ActiveChart.SeriesCollection(2).Values = "='f960'!R262C8:R281C8"
    n = 0
    For Each Series In ActiveChart.SeriesCollection
        valuestring = fmt("='f960'!R%xC8:R%xC8", Array(pos, pos + 19))
        If n < 12 Then
            Series.Values = valuestring
            Debug.Print n
            n = n + 1
            End If
        pos = pos + 20
        Next
End Sub


2002-05-15-0919
0919-1304
continue preparing excel spreadsheets for use in data analysis.
if I was to combine positive and negative spins, how would I do it?
reverse sign of both spin and difference from actual spin-- a reflection over both axes.

tomorrow, continue finishing data analysis setup and 
probably run some trials with me!

2002-05-16-0913
0915-1300
see above.
what other graphs should we make besides tilt v spin?

diff v spin sl_30, sl_45


2002-05-17-0937
0935-1320
continue with your trials.. only 13 or 14 x 60 left.

appears that copying of file over-- at intermission screen quit is not getting all the data. My guess is: there is no file.close() prior to copying the file. However, when leaving the main loop the file gets flushed? -- Yeah, that's my guess.


2002-05-20-0917
0915-1300
finish looking at displays.
ongoing projects.
problem mentioned above was fixed

let's go!

at 300, problem with intermission screen
By inspection, not seeing what problem is.

finished looking at displays-- put data into template--worked well!

Now, code documentation. Both maxscript, and python.
Though, should see if that 300, run2 bug comes again.


300 bug not reproduced....

2002-05-21-0916
0915-1300[05]
today, continue on code documentation

and update script for investigator to include instructions on running software.

2002-05-22-0919
0920-1300
continue with code documentation.
Ok! it appears I am done with  code documentation!!! Yes!
So, now to summarize old results. 
and, perhaps, go over code doc with the hal 4years from now spec? I think the code comments work to that spec already, but maybe go over code with hal.


2002-05-23-0917
0915-1300
Today: summarize old results.

also: show hal my data from line displays.

Tomorrow morning, run through routine with hal as a naieve participant.

2002-05-24-0914

2002-05-28-0959
0915-1300
Got alcohol swabs.
So here I am. Hal is gone for two weeks. I have my own office. And many participants to run.

to be ready to run participants: 
(1) Cardboard for making circular demo displays.
(2) fix script, review in mind. 
(3) Means of tracking participants hours (spreadsheet)

Let's email everyone first. then go down list.

be here tomorrow at 9 for Zhaoxu. Fix felt on door. Draw stripes. Type script. answer emails. backup data. All is well?

2002-05-29-0900
for some reason, script is not backing up data after completing a directory of images--
actually, that's how it's programmed--it won't actually make a backup copy of the data until the participant presses escape. What I changed earlier was to make sure it wrote out the datafile on the local machine.

I'm keeping notes regarding my interaction with each participant in an excel file in c:\_temp\python\realdata\participanttime.xls
backed up on zip in _spinstudydata\

Better keyboard diagram.

2002-05-30-1012
1015-14:00
Missed emily this morning because I was off handling library issues...
double-scheduled monday, although there is time to fix that problem.

in short:
need to develop scheduling procedure--email/phone protocol, etc.

Just use more common sense, and slow down.



2002-05-31-0904
sched proc:
Like eksupar volunteered, try to get idea of whole schedule (so can have idea when to schedule others).


now for some real work.

- print out revised script
- finish summary of early work. 

- always add 15 min to not be cheap?


2002-06-03-1014
running participants: eksupar and alice, their first time.

2002-06-04-0839
get phone number of people to be able to call them when they don't show up.

today: look at elaine's data--get it in spreadsheet, db.

tell them to bring sweaters in case room gets cool (warm in morining, cools off midday)

2002-06-05-0854
0854-1400
1038
what to do with Elaine's data- check policy on outliers.

most of day running participants.
Still working on writeup of old panel efforts.
running participants is distracting from writing work (which I notice I don't concentrate on well).

I don't need to be in early any more.

Improved database querying-- now can get p's data by name and data label, as opposed to range of values!

Eksupar and Alice's data are now in spreadsheet-- theirs is nice! and they were quick.

2002-06-06-0856
1018
Finished first, and perhaps last draft of summary of shear trials.doc
Yuan finished his trials today. Emily began hers. Jenny and Summra are scheduled for monday!

Tomorrow, emily should finish.
Also work on how to graph data, and how to figure out what pointer readings would be if participant is following lines exactly.
1610 

2002-06-07-0905
1045-1430
revise/read over summary of old results with lines.
1158
1218
Now for 
(1) How to display data (histogram)
(2) What is pointer spec if actually following lines?
Let's take care of 2 first.

Then we'll have method section and data analysis method left.
2144

tomorrow:
consider display of data:
get emily's data in excel.

2002-06-08-1425
emily's data

display of data; stat analysis.

problem: in order to work on one of hal's requests, we need to combine/transform the data from the negative spins.
How can we do that?
thankfully, it looks like you've already done it in query last960_2

it should be straightforward to get the graphs that hal wanted.

so, now, I'm looking at the graphs, and considering the data analysis question. Is there an effect of lines on participant's specification of tilt?

What questions do we wish to ask of the data?


began working on methods section because I'm not sure what to do about data analysis, further graphing options.
1652

2002-06-10-0925
0925-1310

Histogram and methods.

worked on histogram

2002-06-11-0911
0910-1255
Hal wants bins.
bin approach if number mod binwidth < binwidth then bin = non-remainder part (what is correct name?)

do in query in access.

2002-06-12-0939
1015
1327

continue with histogram
then methods section.
or line projection... yeah, review that.

2002-06-13-0848
0930 -1315
gen histograms for all participants.
then methods, line projection.

speed of pointer?

write util in 3dsmax to get projected pointerline and then draw pointer oriented to what it determines?


tu.value = atan(atan((xv(tan(tspv))/(cd-xv*sin(tslv)))/atan(xv*cos(tslv)/cd)))

o statistical analysis of 3ddata


2002-06-14-0932
0930-1315
hal's data then work on line projection, or methods.


2002-06-17-0937
0930-1315
goal: to get the line calculation working today.
worked on proj line calculation. Hal pointed out problem with approximating x/y with tanthetax/tanthetay

no solid solution yet.

2002-06-18-0901
0901-1245/40

today, data with new line// projected slant line.

hal's formulation (a much better one):

projected spin angle sigma prime for hal, thetau for me
thetau = atan(tan(thetaspin)/cos(thetaslant))

now we're working on a modified histogram
should be simple--same histogram as last time, except, the cdiff value is the difference from the projected spin line, not the slant.
so, we'll need a diff value from the spin, from the projected spin, and all the data should still fit into the same histogram graph.

so, in excel, perhaps just make new templates to contain the new histogram data, instead of redoing their old stuff. 
Sounds good.

let's go.

for access query:
"hal" Or "colin" Or "summra" Or "emily" Or "yuan" Or "alice" Or "eksupar" Or "elaine" Or "jenny"


last960_2
cdifspin: [last960]![cspectilt]-([data]![tilt]-[last960]![cspin])
old--saving here while work on kludge to get proj spin....
3.1415926535897931

2002-06-19-0945
0940-1325

cdifspin: CInt([last960]![cspectilt]-([data]![tilt]-Atn(Tan([last960]![cspin]*[pi]/180)/Cos([Data]![slant]*[pi]/180))*180/[pi]))

2002-06-20-0914
0915-1300

To do after reviewing histograms with Hal:
(1) work on bin size/centering issue, use cint instead of int in access.
done

(2) for each participant make projected spin graphs (no more than 5 minutes a person?) and redo ag graphs.
done - not for npspin though-- still off center. (int, not cint)

(3) Repititions: is there a systematic difference between histograms of first and second runs/ run1/run2.
InStr(1,[Data]![sessionlabel],"practice",1)
"0"
removed from query

done, no sig nificant difference, though with first practice 12 errors were more likely with the lines than perpendicular to them.



(4) is there a difference in pairs of values corresponding to images from run1-run2.. Looking for a bistability in image here.. perhaps distribution centered around 0 and then smaller ones around 90 or 180 apart.


run1/run2 ag data.

2002-06-21-0948
0945-1330

not telling us about reversals (the histogram of differences between trial one and trial two spec values).

still do do with data- look at tilt- systematic difference.

need to decide on design of second part of study.
need to decide on what design of combined display (lines & pentagons)

monday:
dig out old displays:
look at them.
surfacy stuff.
keep components of display glued together.

2002-06-24-0918
0915-1338 +30
see above for to do. If extra time, can work on methods section.

2002-06-25-0937
0930-1315
continue with doc of display construction. work on improving value range.
working on displays...
I think making pentagons and lines the same color works.

2002-06-26-0920
0920-1305

display construction continued.
work on methods section. for lines portion of display. Also could work on statistical analysis issue.

Hal Likes the idea of making  pentagons and lines the same color!

Now, could simplify the material arrangement in the base display/ prepare it to generate images where pentagons are the same color as the lines.


The display does look a bit washed out with all those pentagons at a value of 128 in addition to the lines, with the background at 64.

2002-06-27-0945
0945-1330 (1404)

to do: work on methods section and then possible render images for next round of study. Cool.

in instructions to hal, forgot to say adjust pointer...!!


We have our things to do for the rest of today and tomorrow:
randomization issues in script. Randomly rotate every pentagon, eachtime every ddisplay is generated.
Every time a display is generated, use a new random sequence. Could write code in python and have other computer generate random sequences.

first:, we need to generate 960 pentagons, my god, to be sure it's an isotropic texture.
Then, we need 960 pentagons + lines, plus 96 pentagons. The 96 pentagons we can take from the first batch--96 pentagons include 4 from each slant/tilt combination 2* = 4*12*2

960 pentagons should require no code change, except the stipulation of rotating every pentagon again after each pentagon has been moved. So let's work on that.

likewise, the 960 pentagons + lines require no code change.


1404

2002-06-28-1412
Yikes Dena showed up!
so now..

We're going like 2 to 6- that's fine.

we have 480 images. To get 960 I'll probably have to double the spins. The names of the directories will keep them from overwriting. Or could change the filename prefix.

We should spend our time looking at the first 480, And need to work out the plan for rendering the other images.

(1) for 480 more, just re-run the same script (diff prefix filenames). It will finish tomorrow. We will be here tomorrow. zero twice issue. Don't like the kludge.

also need to handle material settings in script.
for pents + lines.

so we put them all in one directory, and point sessionman to that directory.
perhaps with some practice images.

for tomorrow, that is straightforward, the remaining images should be rendered by then.

All that is left is 960 pents + lines (material editor issue)--> should be able to render. Also, 96 0 spin 
2 slants * 12 tilts = 24. Since typically there are four data points for each spin (negative, positive, times two)  * 4 = 96. I could just take 96 from the previously generated lines & pentagons. O.k. then.

Get remaining images rendered for tomorrow. Tomorrow spend time running trials (no more than two hours). Tomorrow start first set of 480-- actually, by changing prefix, e.g., for prefixes in () do.. we can run them all at once so let's do that. By monday we should have everything or at worst have to do 96 more.

Then can work on methods section again.

So today, get everything set up for tomorrow and start rendering of ...

that's all!!
still to do: handle material properly in script (for lines) but for tomorrow we're o.k. will be resuming rendering soon
1531 

2002-06-29-1102
alright. So we're going to look at 2 hrs of pentagons. or about that.
And figure out how to start rendering lines display. no problem, really.
off we go.
1129
problem:
last 100 images, the randlist of coords could not be written to disk because drive was full. Spent some time cleaning up old, unused programs, and now there's plenty of room (364mb).

so the space is free, but now need to wait for generation of 100 more images. 
At the least, I can start generating the lines after these finish, even if I'm not able to start viewing pgons yet.
whoops. I deleted all my script files. good thing I have backups... I hope.

2002-07-01-0911
0910-1355
Looked at pentagons.
Prepare for rendering line + Pentagons.

Forgot about two blocks of 60 for practice for our evaluation of our isotropic surface. Thankfully Hal decided that for he and I that was fine.

For the tex and lines, however, do not forget the two blocks of practice.

2002-07-02-0911
Completed looking at isotropic pentagons...
The data is now in spreadsheet.
Before leaving render the next 480 of tx+ lines. 
backup data.
Tomorrow, get whole tl set up set up..
on this computer, because hal will still be using sessionman on 200-2

tomorrow, render last 96 0 spin pentagons.

Monday, do tl setup yourself.

2002-07-03-0917
we have a problem, the gen script quit after making only 77.. We can tweak it a bit and rerun it.

and hal is interested in something before the methods section, what was that?

It was looking for effect of tilt on specified tilt, is it significant?

How can we do this? Using isotropic texture, look at mean dif by tilt?


here's the plan:
get script set up for hal to gen96 pentagons. So he can run it on friday. Simple.
Turn everything off on computer (close all programs except 3dsmax). Reboot computer?
Then let it run, it should work.


2002-07-08-0914
960 images have been generated, so the problem last time was a windows/3dsmax shortcoming. for some reason the gen96.ms is not being included, so will have to run those this pm.

Hal's data is complete, so can work on that. And data analysis by tilt, methods, etc.

o email people asking if they'd like to participate

o prepare session manager/ session script to handle new trials
    isoprac: 12 @ 45deg
    tlprac: 12 @ anydegree random from tl only
    practice: 132 @ randomsel from whole directory.

o set generation of 96 images running.

2002-07-09-0921
0920-1305
we have two people scheduled, one for tomorrow, and two others tentatively scheduled. We still will want two more.
Mozilla mail is not working for two accounts--and generally doing strange things. What a pain.

I should make sure I have an updated copy of the script, and I should run through images with hal.

The new 96 iso images actually did not render (only , but I shall use the ones used for the isotropic texture test instead.

If it had worked, we would have have had 24 * 4 = 96 images. Why didn't it work?
for one, we only had one prefix in FILEPREFIXES, "iso96" should have had two.

secondly, our 0 spin kludge doesn't handle long sequence of zeros, so basically, it rendered every image twice because, since the previous spin was always zero the rendered image was always labled -0....

now, let's make sure our script is o.k. and then start running the study.

2002-07-10-0934
0935-1320

make new physical aid
go over script
1200, see emily..
replace 30 deg practice images.
replaced.


problems with session.py!!!
fixed problem where multiple enter presses while waiting for calibration screen are cleared from queue (does not advance past calibration screen)

now strips whitespace from initially chosen user name!!!

remember in future to always strip white space from user input!

2002-07-11-0915
0915-1300
today, complete running tl trials (or most of them, 0930-01130

update script with corrections hal noticed.

work on new data analysis templates.

let's go.

backup data.

to review where I was last with the isotropic data:
hal and I looked at the means and standard deviations by spin (0-90, by tens), separated by tilt. And aggregate values.
Significant finding that SDs for 45 degree values were always less than SDs for 30 degrees.

We did not see any significant effect by spin (a similar disparity in mean difference from actual value in both hal and I).

Data analysis by tilt, how will we do this?

How about just like with spins: for each tilt do means and standard deviations of the difference value.  For both hal and I.

alright, I have the means, sd's by tilt.

What is the hypothesis that there is no effect of tilt on perceived tilt?

That hypothesis, Ho, Ho is that each tilt's mean difference from every other tilt's mean difference is not significant.

So if a mean for 1 tilt is significantly different from the mean of another tilt, than failure to support Ho was found.

How do we know if 1 mean is significantly different from another?

just from lookin

2002-07-15-1434
0930-1330
finished looking at images myself, and got pauline, ngoc, and my data in excel spreadsheet.

2002-07-16-0918
0920-1305
what to do with isotropic from 1200 images. Not sure. Let's make the query.

Like "texli01" Or "texli02"
v
Like "fin2_00" Or "fin_000"

sessionlabel is tl
we have the images. What to do with isotropic texture?


2002-07-17-1018
0920-1305
susan finished- we now have four completes including me.
The task for the day/week/month is to find a way of comparing distributions of data quantitatively.

Given the obvious differences in the data, this should not be difficult.

(a) basically, the [this is a cool problem] distribution of differences of the specified tilt from the actual tilt for the isotropic data is fairly normally distributed about a mode of 0.

so no worries there.
What are statistics which describe the normality of a distribution.

ways of deciding data is normally distributed or not.

o.k.

(b) the lines only data can be summarized generally by two normal distributions about 0 and 90

so, we could just chop it in half at 45 and do the same fit test. To the transformed data.


--
if you were writing a program to sort data by which model it fit best, how would you do it?


(c) the lines and iso combination could be analyzed from the perspective of some people going primarily with the lines, and others going primarily with the pentagons.

--
Our statistical analysis can consist of a computer program which sorts participants based on analysis of their data (post-hoc analysis, which could later be confirmed or rejected). For one experimental condition, we should see all participants put in one category (bimodal?), for the other condition, all participants in the other category (unimodal). We shall have power issues. The concept of power. For the third condition (tl), it appears that participants will fall one way or the other ( more unimodal ag, or more bimodal (following the lines) ag).


signal analysis, data sorting.

how will we do this?


well, The statistics books are not too helpful in providing tests for normality, however, we can get the equation for the normal distribution, which should be all we need.

what do we have?
a bunch of difference scores. And a bunch of difference scores transformed.
We can take the mean of these difference scores.
We can find the standard deviation.
We're looking for a goodness of fit.

Why not just do that. Take the data, do mean, s.d. for each set.
We know this is ridiculous. Should have assistance of SPSS or statistica.

We can have two data files, simply containing participant's names and their difference scores and their converted difference scores.

These can be read in, made into lists by participant and whether it's converted or not and experimental condition. Means and standard deviations can be calculated. Sounds good.
We have cdiff and cdiffspin


2002-07-18-1301
0920-1305
so, hal and I spent the half-day talking about how to analyze the data.
an interesting discussion.
one result is that I'll work on a macro/system for viewing the histograms by slices. click, clikc, clik.

He is more interested by spin slices than by statistics on the aggregate.

2002-07-19-0940
0940-1325
We're going to be working on automating viewing of slices of a graph in excel.

eyes were going so, resized screen res to 1024 x 768, same res as laptop screen, but almost 4x the size. This may help alot.

So we have a basic slice operation working reasonably well.
What should we abstract, and how?

The chart, for one. Let's try.
We have achieved chart independence 1113 

able to spec cols by number 1243 

now, we need to be able to cycle through columns based on sourcedata.values of chart.
c-1 turn on or off 1, c-2 ditto, etc.
sounds good. need to get list of columns containing sourcedata of chart! should be easy as long as we unhide all chart columns before continuing.




Function ColNo2ColRef(ColNo As Integer) As String

    If ColNo < 1 Or ColNo > 256 Then
        ColNo2ColRef = "#VALUE!"
        Exit Function
    End If
    ColNo2ColRef = Cells(1, ColNo).Address(True, False, xlA1)
    ColNo2ColRef = Left(ColNo2ColRef, InStr(1, ColNo2ColRef, "$") - 1)
    'ColNo2ColRef = Left(ColNo2ColRef, InStr(1,colno2colref)
    'cells(1,
    'cells(1,2).address(true,a
End Function
Sub slice()
'
' slice Macro
' Macro recorded 7/19/2002 by Valued Gateway 2000 Customer
'

'

    'Dim mc As New Chart
    'mc = ActiveChart
    'ActiveSheet.ChartObjects("Chart 20").Activate
    mychart = InStr(1, ActiveChart.Name, " Chart ")
    mychart = Right(ActiveChart.Name, Len(ActiveChart.Name) - mychart)


    'Dim clist(26) As String
    Debug.Print "\n/n--------------------------------------"
    For Each Series In ActiveChart.SeriesCollection
        'valuestring = fmt("='f960'!R%xC8:R%xC8", Array(pos, pos + 19))
        'If n < 12 Then
        '    Series.Values = valuestring
        '    Debug.Print n
        '    n = n + 1
        '    End If
        'pos = pos + 20
        Debug.Print (Series.Name)
        'Debug.Print (Series.XValues)
        'Debug.Print (Series.FormulaR1C1Local)
        Debug.Print (Series.FormulaLocal)
        'ActiveChart.SeriesCollection (1)
        Next


    'none of the following work:
    'Debug.Print ActiveChart.ChartTitle
    'Debug.Print ActiveChart.Index
    'Debug.Print ActiveChart.CodeName
    

    ActiveChart.ShowWindow = True
    
    'ActiveWindow.Visible = False
    ActiveWindow.WindowState = xlMinimized
    Windows("960tl.xls").Activate
    
    'mychoice = True
    
    'myvar=("A","B","C")
    'Dim clist(26) As String
    'clist(1) = "a"
    'Debug.Print clist(1)
    
    'Debug.Print ColNo2ColRef(16)
    
    Columns("P:S").Select
    'Columns((16,17,18)).Select
    'Columns("R1564C16:R1564C19").Select
    'columns(
    
    mychoice = Not Selection.EntireColumn.Hidden
    
    Selection.EntireColumn.Hidden = mychoice
    
    'If Selection.EntireColumn.Hidden Then
    '    Selection.EntireColumn.Hidden = False
    'Else
    '    Selection.EntireColumn.Hidden = True
    'End If
    
    '''Columns("O:T").Select
'''    Selection.EntireColumn.Hidden = False
'''    Columns("T:AA").Select
'''    Selection.EntireColumn.Hidden = False
        
    Columns("U:Z").Select
    Selection.EntireColumn.Hidden = mychoice
    'If Selection.EntireColumn.Hidden Then
    '    Selection.EntireColumn.Hidden = False
    'Else
    '     Selection.EntireColumn.Hidden = True
    'End If
    
    ActiveSheet.ChartObjects(mychart).Activate
    'ActiveSheet.ChartObjects("Chart 20").Activate
    'mychart.Activate
    ActiveChart.ShowWindow = True
    'Debug.Print mychart
    
End Sub

2002-07-20-1011
problem:

session.py bug:
for sdecruz went straight to screen before calibration screen (no break).

2002-07-22-1027
0920-1305
So,
did not think of alternative approach to graphing problem:
zeroing out the columns of data for the the spins one does not want to see., saving that data elsewhere and putting it back when wanted. Would probably need to preserve


How should we make this work now?
use case:
hit ctrl-d to cycle through spins after selecting a chart.
hit ctrl-e after selecting a graph to enter the columns one wants to see. Example, if I want to see spins 10,20,40, I'd enter: 1,2,4 in an input box.

InputBox("Enter spins you wish to see separated by a comma: ", "listofspins")
string.split(listofspins,",")

for every column not in list, hide that column.

that's it!

Needed tech:

from graph, we need to get value of the first column. (so we know that spin zero starts at column Q), and can determine which columns to hide.

problem, if columns are hidden, the value of the first column is not known.

unelegant solution: unhide all columns within a range encompassing all graphs prior to reading chart seriesdata, then get first column and go from there.


other solution: get chart series data. get column of first data currently displayed. go left until find first unhidden column. Use first unhidden column+1 to calibrate scale (0-9).

Let's try that.

Hang on, we know the name of the data series (10,20,all, etc.)

that's all we need.

1211 we have first colletter and firstcolspin.

1321 its working, somewhat-- not getting slice with all values and not getting 0 spin slice. tomorrow!


Function colref2colno(colref As Variant) As Integer
    colref2colno = 0
    On Error Resume Next
    colref2colno = Range(colref & "1").Column
End Function
Sub slice()
'
' slice Macro
' Macro recorded 7/19/2002 by Valued Gateway 2000 Customer
'

'

    'Dim mc As New Chart
    'mc = ActiveChart
    'ActiveSheet.ChartObjects("Chart 20").Activate
    mychart = InStr(1, ActiveChart.Name, " Chart ")
    mychart = Right(ActiveChart.Name, Len(ActiveChart.Name) - mychart)


    'Dim clist(26) As String
    Debug.Print "\n/n--------------------------------------"
    
    For Each series In ActiveChart.SeriesCollection
    'Dim series As New se
    'series = ActiveChart.SeriesCollection.Item(1)
        'valuestring = fmt("='f960'!R%xC8:R%xC8", Array(pos, pos + 19))
        'If n < 12 Then
        '    Series.Values = valuestring
        '    Debug.Print n
        '    n = n + 1
        '    End If
        'pos = pos + 20
        If series.Name = "all" Then
            firstcolspin = 10
        Else
            firstcolspin = CInt(series.Name) / 10
        End If
        'Debug.Print (Series.XValues)
        'Debug.Print (Series.FormulaR1C1Local)
        firstcolletter = CInt(InStrRev(series.FormulaLocal, "!"))
        '=SERIES("all",ngoc!$O$1565:$O$1625,ngoc!$P$1565:$P$1625,11)
        'Dim lastcolletter As Variant
        lastcolletter = CInt(InStr(firstcolletter + 2, series.FormulaLocal, "$"))
        'Debug.Print firstcolletter
        'Debug.Print (lastcolletter - (firstcolletter + 2))
        firstcolletter = Mid(series.FormulaLocal, firstcolletter + 2, (lastcolletter - (firstcolletter + 2)))
        'ActiveChart.SeriesCollection (1)
        Exit For
        Next
             
     Debug.Print "fcs " + CStr((firstcolspin))
     Debug.Print "fcl " + (firstcolletter)
     'Debug.Print (lastcolletter)


    'none of the following work:
    'Debug.Print ActiveChart.ChartTitle
    'Debug.Print ActiveChart.Index
    'Debug.Print ActiveChart.CodeName
    If firstcolspin = 10 Then
        'we want to show the whole graph
        'otherwise we want to hide all but the next in sequence.
    End If
    

    'so, we know the column we want to show = firstcolletter + 1
    'We need startcolletter.
    'Debug.Print 'firstcollletter:' firstcolletter
    firstcolno = colref2colno(firstcolletter)
    Debug.Print firstcolno - firstcolspin
    'startcolletter = ColNo2ColRef(colref2colno(firstcolletter) - firstcolspin)
    'Debug.Print startcolletter
    startcolno = (firstcolno - firstcolspin) - 1
    Debug.Print firstcolno
    Debug.Print startcolno
    Dim clist(11) As Integer
    For n = 0 To 10
        clist(n) = startcolno + n
        Next
    
    'now, iterate through, and hide all columns but the one we want
    
    ActiveChart.ShowWindow = True
    
    'ActiveWindow.Visible = False
    ActiveWindow.WindowState = xlMinimized
    Windows("960tl.xls").Activate
    
    If firstcolspin = 9 Then
        'we want to show the whole graph
        'otherwise we want to hide all but the next in sequence.
        'firstcolno = startcolno
        For n = 0 To 10
           Columns(clist(n)).Select
           Selection.EntireColumn.Hidden = False
           'Selection.EntireColumn.Hidden = False
           Next
    Else
        For n = 0 To 10
           Columns(clist(n)).Select
           Selection.EntireColumn.Hidden = Not (clist(n) = (firstcolno + 1))
           'Selection.EntireColumn.Hidden = False
           Next
    End If
    
    'mychoice = True
    
    'myvar=("A","B","C")
        
    'Debug.Print ColNo2ColRef(16)
    'Columns(startcolno).Select
    'Columns("P:S").Select
    
    
    'mychoice = Not Selection.EntireColumn.Hidden
    'Selection.EntireColumn.Hidden = mychoice
    'Columns("U:Z").Select
    'Selection.EntireColumn.Hidden = mychoice
    
    ActiveSheet.ChartObjects(mychart).Activate
    ActiveChart.ShowWindow = True
    
End Sub

2002-07-23-0924
0937 


Sub Macro2()
'
' Macro2 Macro
' Macro recorded 7/23/2002 by Valued Gateway 2000 Customer
'
' Keyboard Shortcut: Ctrl+x
'

For n = 1 To 256

    If n Mod 2 = 1 Then
        With ActiveSheet
        .Columns(n).Select
        .Range(.Cells(1, n), .Cells(10, n)).Select
        Selection.Copy
        .Range(.Cells(64, (n + 1) / 2), .Cells(64, (n + 1) / 2)).Select
        .Paste Link:=True
        End With
'        'Selection.EntireColumn.Hidden = True
        End If
    Next
End Sub

Ok. we have a hack that works for cycling through slices. Now let's make something that lets you tpe in the spins you want displayed.

1320 we sort of have a hack working for selecting a list of items to be hidden, but it doesn' work quite right. tomorrow, finish.


Sub slice2()
'
' slice Macro
' Macro recorded 7/19/2002 by Valued Gateway 2000 Customer
    
    mychart = InStr(1, ActiveChart.Name, " Chart ")
    mychart = Right(ActiveChart.Name, Len(ActiveChart.Name) - mychart)
    
    spins = InputBox("enter spins/10 separated by a space (use '10' for sums): ")
    
    spinsdesired = Split(spins)
    'Sort (spinsdesired)
    For n = 1 To UBound(spinsdesired)
        spinsdesired(n) = CInt(spinsdesired(n))
        Debug.Print spinsdesired(n)
        
        Next
    
    Debug.Print "--------------------------------------"
    
    For Each series In ActiveChart.SeriesCollection
        If series.Name = "all" Then
            firstcolspin = 10
        Else
            firstcolspin = CInt(series.Name) / 10
        End If
        firstcolletter = CInt(InStrRev(series.FormulaLocal, "!"))
        '=SERIES("all",ngoc!$O$1565:$O$1625,ngoc!$P$1565:$P$1625,11)
        lastcolletter = CInt(InStr(firstcolletter + 2, series.FormulaLocal, "$"))
        firstcolletter = Mid(series.FormulaLocal, firstcolletter + 2, (lastcolletter - (firstcolletter + 2)))
        Exit For
        Next
        
     counter = 0
    For Each series In ActiveChart.SeriesCollection
        counter = counter + 1
        'Debug.Print series.FormulaLocal
        Next
             
     Debug.Print "fcs " + CStr((firstcolspin))
     Debug.Print "fcl " + (firstcolletter)
    

    'none of the following work:
    'Debug.Print ActiveChart.ChartTitle
    'Debug.Print ActiveChart.Index
    'Debug.Print ActiveChart.CodeName
       

    'so, we know the column we want to show = firstcolletter + 1
    'We need startcolletter.
    'Debug.Print 'firstcollletter:' firstcolletter
    firstcolno = colref2colno(firstcolletter)
    
    'startcolletter = ColNo2ColRef(colref2colno(firstcolletter) - firstcolspin)
    'Debug.Print startcolletter
    If firstcolspin = 10 Then
        startcolno = (firstcolno - 0)
    Else
        startcolno = (firstcolno - firstcolspin) - 1
    End If
        
    Dim clist(11) As Integer
    For n = 0 To 10
        clist(n) = startcolno + n
        Next
    
    'now, iterate through, and hide all columns but the one we want
    
    ActiveChart.ShowWindow = True
    
    'ActiveWindow.Visible = False
    ActiveWindow.WindowState = xlMinimized
    Windows("960tl.xls").Activate
    
''''    If firstcolspin = 10 Then
''''        ''we want to show the whole graph
''''        ''otherwise we want to hide all but the next in sequence.
''''        Debug.Print "hello 10"
''''        For n = 0 To 10
''''           Columns(clist(n)).Select
''''           Selection.EntireColumn.Hidden = False
''''           Next
''''
''''    ElseIf firstcolspin = 9 Then
''''        ''show all (sum) (in 0th position)
''''        For n = 0 To 10
''''           Columns(clist(n)).Select
''''           Selection.EntireColumn.Hidden = Not (n = 0)
''''           'Selection.EntireColumn.Hidden = False
''''           Next
''''
''''    ElseIf firstcolspin = 0 Then
''''        ''show all but zero:
''''        For n = 0 To 10
''''           Columns(clist(n)).Select
''''           If counter > 1 Then
''''            Selection.EntireColumn.Hidden = Not n = 1
''''           Else
''''            Selection.EntireColumn.Hidden = Not n = 2
''''           'Selection.EntireColumn.Hidden = False
''''           End If
''''           Next
''''
    ''''Else
        Debug.Print "hello not 9 or 10"
        For n = 0 To 10
           Columns(clist(n)).Select
           hidethiscolumn = False
           For m = 1 To UBound(spinsdesired)
                Debug.Print "sd(m): "
                Debug.Print spinsdesired(m)
                Debug.Print "n: "
                Debug.Print n
                If CInt(spinsdesired(m)) = CInt(n) Then
                    Debug.Print "hiding this column"
                   hidethiscolumn = True
                   Exit For
                End If
                Next
           'Debug.Print hidethiscolumn
           Selection.EntireColumn.Hidden = hidethiscolumn
                
           'Selection.EntireColumn.Hidden = False
           Next
    ''''End If
    
    'mychoice = True
    
    'myvar=("A","B","C")
        
    'Debug.Print ColNo2ColRef(16)
    'Columns(startcolno).Select
    'Columns("P:S").Select
    
    
    'mychoice = Not Selection.EntireColumn.Hidden
    'Selection.EntireColumn.Hidden = mychoice
    'Columns("U:Z").Select
    'Selection.EntireColumn.Hidden = mychoice
    
    ActiveSheet.ChartObjects(mychart).Activate
    ActiveChart.ShowWindow = True
    
End Sub

2002-07-24-0945
currently attempting to get hack to work.
so complicated, and I really don't understand what's going on.
it should be easy.
I'll sit down and work through it.

1012 
well, that worked.
spin2 is not a hack- works nicely 
and for now I leave spin() as the hack that it is.
and move on to data analysis.

perhaps should look to making the macros work across multiple workbook files....
look into that.

no problem.

now let's get the data in the spreadsheet of the people who've finished.

fyi,here's the non-hack code.

Sub slice2()
'  ctrl-q
' slice Macro
' Macro recorded 7/19/2002 by Valued Gateway 2000 Customer
    
    mychart = InStr(1, ActiveChart.Name, " Chart ")
    mychart = Right(ActiveChart.Name, Len(ActiveChart.Name) - mychart)
    
    spins = InputBox("enter spins/10 separated by a space (use '-1' for sums): ", "spins", "0")
    Debug.Print "spins " + spins
    spinsdesired = Split(spins)
    'Sort (spinsdesired)
    For n = 0 To UBound(spinsdesired)
        If spinsdesired(n) <> "" Then
            spinsdesired(n) = CInt(spinsdesired(n))
            Debug.Print spinsdesired(n)
            End If
        Next
    
    Debug.Print "--------------------------------------"
    
    For Each series In ActiveChart.SeriesCollection
        If series.Name = "all" Then
            firstcolspin = -1
        Else
            firstcolspin = CInt(series.Name) / 10
        End If
        firstcolletter = CInt(InStrRev(series.FormulaLocal, "!"))
        '=SERIES("all",ngoc!$O$1565:$O$1625,ngoc!$P$1565:$P$1625,11)
        lastcolletter = CInt(InStr(firstcolletter + 2, series.FormulaLocal, "$"))
        firstcolletter = Mid(series.FormulaLocal, firstcolletter + 2, (lastcolletter - (firstcolletter + 2)))
        Exit For
        Next
        
                 
     Debug.Print "fcs " + CStr((firstcolspin))
     Debug.Print "fcl " + (firstcolletter)
    

    'We need startcolletter. ' where the graph source data actually starts.
    'Debug.Print 'firstcollletter:' firstcolletter
    firstcolno = colref2colno(firstcolletter)
    
    'startcolletter = ColNo2ColRef(colref2colno(firstcolletter) - firstcolspin)
    'Debug.Print startcolletter
    If firstcolspin = 12 Then
        startcolno = (firstcolno - 0)
    Else
        ''if first colno is 17 and first colspin is 1 startcolno = 16.
        ''but since the sum data is in the column before zero, we need to subtract 1.
        startcolno = (firstcolno - firstcolspin) - 1
    End If
        
    Dim clist(11) As Integer
    'we're trying to make a list where the clist index corresponds to the spin
    'so we can translate directly between spin and column number.
    'the problem is the sum is in the first column.
    'so we'll have to make it that the spin is offset by one with totals at 0?
    'previously I was having totals be at 10...
    'the way the code is now, it seems 0=sums, 1=spin0.. etc.
    For n = 0 To 10
        clist(n) = startcolno + n
        Next
    
    'now, iterate through, and hide all columns but the one we want
    
    ActiveChart.ShowWindow = True
    
    'ActiveWindow.Visible = False
    ActiveWindow.WindowState = xlMinimized
    Windows("960tl.xls").Activate
    
        'here we iterate through our list, comparing each value to
        'the contents of the spinsdesired list.
        'if there ever is a match then we know we want to show or hide that column.
        
        For n = 0 To 10
           Columns(clist(n)).Select
           hidethiscolumn = True
           
           
           For m = 0 To UBound(spinsdesired)
                Debug.Print "sd(m): "
                Debug.Print spinsdesired(m)
                Debug.Print "n: "
                Debug.Print n
                'subtracting 1 below because spins are offset.
                If spinsdesired(m) <> "" Then
                If CInt(spinsdesired(m)) = CInt(n) - 1 Then
                    Debug.Print "showing this column"
                   hidethiscolumn = False
                   Exit For
                End If
                End If
                Next
        
           Selection.EntireColumn.Hidden = hidethiscolumn
                
           'Selection.EntireColumn.Hidden = False
           Next
    ''''End If
    
    
    
    ActiveSheet.ChartObjects(mychart).Activate
    ActiveChart.ShowWindow = True
    
End Sub
'seems should work now. let see.
'part of the problem was, arrays are zero based (was thinking that in vb they weren't)
ongoing:

Like "tl" Or "iso56" Or "run1" Or "run2"

1329 
tomorrow- finish susan, and alison..

make space on backup disk!

2002-07-25-0929
0930-1315
finish susan, and alison, 
make space on backup disk.

Vicky Fisher will be here at 10:00
whoops. Sslotnick will be here at 10:30
Vicky could come this afternoon at 2pm as well.
o.k.

sslotnick had the same problem, where there was no break given-went straight to calibration screen. What's the deal?

1236 
all the data's in waiting for last participant's.
work on backup disk.
1249
done

o for tomorrow, continue working on data analysis procedure.
o Write up report about findings.

The data analysis script we had: in python. See above for reminder. Test data for fit to two models, and get 0-1 value for fit for each, sort by that. Expect line data to be all one way, iso all the other, and tl, in between.

Also, refresh mind on hal's approach. comparing each spin, converted spin distrib with idealized isotropic spin distrib.

What would hal's data be like? He could have run it if he wanted to.

2002-07-26-0925
summary of data:
from inspection: following iso or not (predominant)?
ss: iso
jill: iso
sdcruz: iso
nathan: lines
pauline: lines
ngoc: iso
colin: iso
susan: lines

for each spin is it unimodal
what is the central tendency

standard d

1306
Worked with hal at looking at data.
Perhaps should do some sort of aggregate data
means of differences. by spin
mode mass by spin density.


o aggregate graphs.

2002-07-29-0937
for hal, we have.
means of differences by spin.

Like "mantha" Or Like "vicky" Or Like "jill" Or Like "alison" Or Like "susana" Or Like "nathan" Or Like "pauline" Or Like "ngoc" Or Like "susan"
1316 we have looked at the different aggregate graphs (an improvement)
and are now attempting to understand the process whereby susan was able to make consistent settings in a manner we did not expect.


2002-07-30-0924
0924-1310
we can focus on-
We spent time:
(1) Using something called (by Hal) "Scott's Law" to do rough checks on appropriate bin size for various types/sizes of samples used in our histograms.
the suggestion is that bin size = 3.49 x SD x n^-(1/3)
we found that the bin size for the aggregated data was suggested to be close to 3 (2.8), and the bin size for most of individual data was suggested to be much larger- though ranging from 3 to 20. 6, as a general size for the individual data seemed appropriate.

(2) actually done before: 1-- we looked again at susan hong's data, which when transformed causes the modes on the right side of the histogram (if individual is putting pointer perpendicular to the lines (following compression)) to go beyond the pointer setting the individual would specify if following compression of the lines exactly. by up to 6 degrees! Decreasing as spin approached 90.

Hal's hypothesis (after I pointed out that using the simple spin transformation (as opposed to the 2-d projection of spun lines) would make the difference less pronounced) was that perhaps with the lines data, individuals were following the projection into 2-d, while that with the addition of the isotropic data, indivs were following the projection of the lines in 3-d.

I should try that transformation-- it looks like it could zero the graph in on 30-- (account for variance from following compression exactly).



2002-07-31-1014
0930-1315
statistica 6.0 appears to have installed fine.

for today:
(1) Look at "shong effect"
(2) Work on getting graphics into powerpoint.

prb: slice macro cannot handle situation when two windows of same spreadsheet are open.

with respect to (2), 
hal is interested in comparing 

--
changing cdif spin to use simple spin transformation
--
old (from above):
cdifspin: [last960]![cspectilt]-([data]![tilt]-[last960]![cspin])
current:
cdifspin: CInt([last960]![cspectilt]-([data]![tilt]-Atn(Tan([last960]![cspin]*[pi]/180)/Cos([Data]![slant]*[pi]/180))*180/[pi]))

1438 

large mistake:
more later
cdiff: IIf([Data]![spin]<=0,([Data]![tilt]-[Data]![diff])-[Data]![tilt],([Data]![tilt]+[Data]![diff])-[Data]![tilt])

how diff values are transformed.

2002-08-01-0938
0930-1315
fixing error. 
should finish today

still fix Colin's data,
and make correction to gen code based on fix.
back up fix.

powerpoint.


2002-08-02-0940
0940-1325
powerpoint is probably first priority.
let's work on that.

works well when one takes the chart one wants, pastes it into a new workbook (by itself), and then copies that chart into powerpoint

otherwise, a near complete copy of the monster workbook with all the data in it is copied into powerpoint as well, which takes a long time, and makes the powerpoint file very large.

o fix Colin's data. (correction transform)

o make correction to gen144 maxscript .

query for aggregate data for exp 2 (texli), 
Like "mantha" Or Like "vicky" Or Like "jill" Or Like "alison" Or Like "susana" Or Like "nathan" Or Like "pauline" Or Like "ngoc" Or Like "susan"
(does not include "colintl" because he also participated in first study)


2002-08-05-0951
0950-1335

o make correction to gen144 maxscript.

1) pentagons (96iso) -> make ag hist
2) make graph rotated of  (you remember)
The plan is:
use the 4 avg indiv data points, from alice at 0 tilt-- so each tilt will have only 4 datapoints / spin.
alice at 210

Then he'll go to her histogram at 30 for all??.

3) put labels on ag graphs for compression, convergence (2d), actual (on transformed data)

1036 "I think it's a really good idea of just using that histogram from the start-"
"great- -!"


how to make the lines on the bare graphs?

2002-08-06-0938
0935 - 1320
today:
o make correction to gen144 maxscript.
o put lab computers on a different subnet?

o work on getting the labels hal wanted on the graphs.
convergence line
compression line

zero difference line.

degrees to radians in python 2.3!
def deg2rad(degrees)
    import math
    return degrees/180.0 * math.pi

def rad2deg(radians)
    import math
    return radians/math.pi * 180.0


save of query for exp2, last 960:
sessionlabel
Like "tl"

2002-08-07-0919
0920 - 1305

today?
work on those graphs.

problem: at least the 6 bin width graphs have a problem in that-
no only the graphs on this page-- must be in how I made them.


tomorrow:
continue working on powerpoint presentation!

2002-08-08-0934
0930 - 1315

2002-08-10-1001
1000 - 1345

powerpoint pres.

2002-08-12-0935
0930-1315
sinister.

Used lattice modifier to make  wireframe effect that hal desired.

2002-08-13-0922
0920-1305
1230
slide show appears to be almost done.
can document graphs,
and clean up backup disks.


2002-08-14-1057
0920-1305
Many possible tasks while hal is gone
Discussion of the 14th:
(1) look at Barbara's old article and consider how her display could be made in 3ds

(2) forced choice study using line images (study 1) run1: compression grad, run2: convergence grad.

> documenting graphs and the methods section.
house keeping, organizing files., backups.



(3) Statistical analysis model data..

-now 1208 focus on forced choice.

need to calculate where pointer should be. Would like to constrain pointer to that direction. or 180 from that direction.

should be easy.


did have problems that time I tried before.

-> given a tilt, a slant, and a spin, where should the pointer be?
focus on the slant and the spin.

1241
calcspinnerpos works!

todo:
disable spinning
enable flipping to convergence or compression position.

possible solution:
instead of having a random position for initial pointer value, have a calculated position randomly selected from right or wrong values.
disable the left arrow key.
have the right arrow key change the spinner direction 180 degrees.

sounds good.
the difficulty is getting the initial spinner value to the spinner object?
no, create a new property in the spinner class. Set that property every time (when self.dizzy gets set to -1)
if that prop is not a default value, then instead of randomizing do what is described above.

1309
o.k.
quitting for day.
Still to do:
parse imagename for spin, etc values.
disable left arrow.
make right arrow rotate pointer 180.

That should be it.
Should also change data recording to simple yes /no colum (whether correct or not)



2002-08-15-0924
0920-1305
finish script run forced trial study.
parse: check
disable left arrow: check
make right arrow rotate pointer 180. check
(need to test all)

to do:
make calcspinnerpos calc based on tilt, etc?


1056
o.k. it's been almost an hour and a half, and it took a lot of that to get the pointer pointing in the right way.
the problem is, the pointer position, tiltposition, and spin conventions are not documented, so I had to guess, realize I was wrong, and refigure them all out.

to do:
1. write up / draw up doc on those conventions.
2. get output to record a simple yes/no 0/1 about whether participant successfully got the calculated spinner position (convergence vector or compression vector) or was 180 degrees off.
3. switch arrow from convergence to compression for second set of images.


*************************conventions********************************
spinner zeros pointing straight down. Positive values are _counter_ clockwise from that zero. 180 is straight up, 90, to the right, 270 to the left.

Tilt follows the same convention. 0 tilt means that positive slants will move the bottom half of the surface away from the viewer. 180 tilt means that positive slants will move the top half of the surface away from the viewer. 90 tilt: right half, 270 tilt: left half.

Spin: 0 spin means the lines are perpendicular to the tilt axis. 0tilt, 0 spin means the lines are vertical.
positive spins move the lines in a _clockwise_ direction. 0 tilt, 45 spin, means the lines are pointing down and to the left! -45 spin- lines are pointing down and to the right.

conventions doc added to top of calcspinnerpos.

todo:
2. simple yes/no/impossible output.
3. switch arrow from convergence to compression for second set of images.
+90 or -90?

4. we have a bug. Whereby if one resumes after exiting the program, the spinner is not initialized properly. Spinner initialization called in wrong place?
bug appears to be solved.

5. When doing compression sometimes the return value has the opposite of correct... true with convergence also?
only with negative or 0 spin offsets?

--->when spin offset is 0, there is no correct value for compression.


plan:
instead of writing out difference or absdiff, write out 0,1,3 for wrong, right, impossible.

the problem with compression (-spin offsets being wrong) does not seem to be a problem with convergence.

also, 
6. need to make sure vals coming out of calcspinnerpos are in range 0-359

--->when spin offset is 90, no correct value for convergence.

1226
o.k. calcspinnerpos working for both convergence and compression.
now, to record data.

1259
awesome!
program appears to work completely.
1. check writing of header file
2. need to set up session: two runs compression, convergence, and need to change flag.

1307
to do tomorrow:
1. set up session.
2. run study.
3. consider how final data analysis will work.

2002-08-16-1137
0920-1305

experienced the no-break bug again with a session size of 120, at the second session to the end. 
should look into this some more...

finished the convergence/compression data gathering hal was interested in. Convergence turned out to be harder to determine than compression.

Hal has me looking into this problem where with compression and a 0 degree spin (no correct answer) I was correct only 1/3 of the time.

What I shall have to do is get out a bunch of zero spin images run through them with the compression test and look at the values that are being compared..

let's go.

2002-08-29-1115
after a long vacation we're starting work.
1115 - 1500

first we should address that bug we were working on. We also need to run another participant on the isotropic data.

and two on the forced choice.

I'll first try to make sure everything is working so we can handle the participants, and then send out some emails to the people on our lists/ or who previously participated.

Let's go.

1158
I ran the test, and it appears it was just chance that I got  0.33 and 0.29 of 24 right twice.
How do I figure the probabilities of that occuring? a 50/50 chance, 24 times?
ho = .5

2^24 possible combinations.

the probability of any given proportion P of successes among N cases is
p(P=r/N)= p(X=r)

r is number of successes

for instance if N=6 and r=4
p(X=4) =p(P=4/6)=(6 4) p^4q^2

6 4 mean 6 combinations of 4 things.

p(8 successes in 24 trials) = (24 8)p^N

since each sequence has the same probability there are (24 8) of them

the probability of observing r successes in N independent trials is
(N r)p^r q^(N-r)

(N r) = N!/(r!(N-r)!)

24!/(8!(16)!) * .5^24 = 0.0438

2704156/ (50/50) is giving me 0.16 so something's wrong.

1246
that's enough time on that... seems like there's not a problem.

this last time I got 27 out of 48...


on to the next problem.

We need to make sure the script still works in non forced choice mode.

Then email people to find a participant.

1331
O.k. looks like we're set for the Iso participant. We're currently only giving them one practice block, though I could change this...? I'll ask hal.

to do:
ask hal how many practice blocks for the iso participant?
no practicebloks for the forced choice?

735471/

1339 
beginning emailing people to find more participants.
after this I begin organizing data, graphs, programs, etc. oh my.

1431
attempting to remember who the participants we don't want are:

probably just not pauline and not vicky and not elaine. Nathan was a bit buggy. ss was slow. so was yuan.

1507
done for the day. Tomorrow as per email to hal, need to set up practice for forced-choice and begin/continue organizing.


2002-08-30-1423
1415-1800 !!
Diana Simkovich is scheduled for Tuesday at 12:30 for two hours.

today.
we need to make sure we're ready for Diana and Samantha.
this involves setting up the practice sessions as hal specified in his email.
as follows:
12 + two practice sessions for the isotropic. (120 trials)
12 + 60 convergence, 12+60 compression.

1438 ready for the iso.
1455
problem: multiple participants running different types of studies. Their session lists

It's possible diana would show up this afternoon and finish by monday, but that isn't likely. We could put in an option somewhere to choose ISO or forcedchoice.
first let's make sure FC is working.

Here's the plan.
    When the experimenter presses f12, one of the options will be to choose the study type. Currently this will be FC or ISO.
    The sessionlist should be saved with the participant's data, and thus should become a propert of the session class.
    If the choice is FC, the order in the sessionlist should alternate.

1615
it appears that the iso sessiontype option is now working.
the fc option is a bit tougher.
need to alternate between s.convergence equaling true and having it equal false.

here's a plan:
    we'll put a little conv or comp at the end of each sessionlabel in the sessionlist. and check the last four characters to determine whether to make the session convergence or compression constrained.

note, we currently have one good user with the new saved data format: username is '1'

1634
possibly done with sessionman, now need to modify handling of practice session based on sessiontype. Hal wanted 60 trials for the fc, 120 for the iso.

Ideally would handle this from session man, but would have to add another number of trials property.. which if not set defaults to everything in directory... that sounds easy enough.

that could obviate the need for practice directories (though they're still helpful to ensure easy images are selected)

I think for now, I'll just go with what worked before, and be done!

1655 Nah. I did it, easily. Now session.numberoftrials can be set from sessionman it is immediately reset to 99999 after use.

1711
still to do:
the intermission screen for the fc sessiontype.
if we set the intermission spacing to 120, will that mess things up?
(and have practice only last 60?) not seamless?
add new property to class: ShowScreenAtEnd?
fine. NO, things will be messed up.!

intermission screen should be handled from session man?

Problems:
    we should separate the number of trials from the number of things in a directory.
    this is annoying.

the intermssionscreen function is going to be ugly. we'll see if we can make it work.


sessionman should specify after which sessionlabel the ending screen is shown.
showendingscreen. If not showendingscreen some sort of intermissionscreen will be shown. which guesses at remaning blocks.

In the case of FC sessiontype, we need to stop in the middle and tell them to ask for instructions. (or give P instructions).

it's time to go.
Still to test:
o does ending screen ever get shown?

we have a problem. We set the dtrialblocksize to 120, but the practice is only 60 long.
we need to suppress showing of intermission screen at end of that session.
set a .suppressscreen?
We need to carry over the count somehow, so that the person

1816
more later.

2002-09-03-1000
0945-1330
Diana Simkovich will be here at 12:30 for 2 hrs to run the iso study. need to be ready.
    o consent form.
    o physical display.

 
2002-09-04-0904
0900-1245
Samantha should be here around 10:30. We should make sure that our code runs acceptably.

prb: self.calcpos isn't getting reset... to 999 after fc trials.


*******nor is it getting reset if you create a new iso user... (only when their data is loaded).
    **a note about this was made in the code.
    no new iso users will be created, so we won't use it.

1129
now, we're on to a new task

o doc/organize the data, graphs, programs, etc.

o work on getting the histograms into publishable form legible in b&w at the size of 1/2 a journal page.

o a condensed way of presenting something about indiv differences--an ag histogram for line-followers and another for the non-followers.




organizing the graphs. what a mess.
organize by experiment:

    o those things I made for dena.
    o pilot study
    o 


we're currently working on something called:
OrganizingForArchiving folder.
Picking up where "summary of shear trials " leaves off. and containing a hierarchy of the related files with explanatory readme .txts.

continue tomorrow. 1301 


2002-09-05-0923
0930-1315
policy on saving images, archiving, deleting, etc.
I am a librarian of sorts at the moment.


Sort out the ones we actually used in studies, at least.

2002-09-06-0934
0930-1315
Continue archiving.: goal finish old stuff.
monday, finish new stuff.


put code used to generate displays in the respective folders... put the three-d max files used at each stage in the respective folders. Anything else left over?

schedule:

dianas: 12:30 - 14:15
    fri: 16:00-
mantha: 10:15 - finished.
summra: fri: 11:00 - 


2002-09-09-0937
1129
we've finished our readme and sorting of files. What remains is some more cleaning up of the x drive and a labelling of the graphs in excel, and then finishing isotropic and forced choice analysis of data.

1326
alright, 
we should have completed our organizing. I guess we'll now see how well we deal with it, maintain it and build on it.

tomorrow:
analyze new data
still to do:
labelling of charts!!!

that's all.

2002-09-10-0928
0930-1315
So, today lets take care of that iso data and fc data and see if we can deal with our new file organization.


1224
as somewhat expected,
the probability bug has come back and bit us.

Using statistica's ibinom() function to get the integral of the probability distribution.

1312
well, the basic problem is in the code...
hal helped me find it by looking at the data first, not the code to see if any systematic errors were apparent. After including the actual specified value and the comparison value, systematic errors were apparent.

2002-09-11-0926
today:
correct mistake from yesterday.

It wasn't the calcspinnerpos code at all, it was some stuff from the earlier version of the program interfering.

1104
there is a problem:
The following images are not identical:
file://localhost/X:/_old/_Aperture/2002-09-06-Study-4-Forced-Choice/errtest/f480_0000000t_-90sp_045sl_li_0000.png

No, it's not a problem, it was just how the image was loaded by opera that particular time.

1112
when you try the rate goes down to .33..
when you try, you're more likely to adjust the pointer.
What happens when you adjust the pointer?

When you raise the pointer, when there's no random sel, by default, you're wrong....


2002-09-12-0932
-13:15
Yesterday, I found, that when I choose a methodology and follow it: always pointing down or to the right, I get 0.5 % exactly.

This makes sense, because for every image, the correct answer is oneway one time and the other way the other time, so following a consistent methodology means you'll always do 0.5.

Could one ever do more than 0.5?

One would have--

In truth, the correct answer should not be connected to the display properties?

one could do more than 0.5, if one messed up in following one's methodology, such that you put the pointer one way, one time and the other way the other time, but what is the probability of that?

It is more likely that for a given display the setting for a given image will be the same direction both times(?)

It seems I could randomize the assignment of the correct value, just like I randomize the pointer, and perhaps this problem would go away for reasons I don't understand?

Easy enough to try.

2002-09-13-0936
today:
backup files.
attempt to further contemplate the mysteriousness with the program.

0953
the Calcpos module would be good to write unittests on.

the whole thing, actually.

Then I could say to hal, "we know all these parts of the program work"
hmm. I should practice writing unit tests.

1029
made it so you can get all the info about the image you're viewing and your pointer specs. by pressing tab

now: make it so hal can run through the data. (change sessionman, put right dir info in)

and get on to preparing graphs for presentation.

1308
print quality appears to be able to improve with better printers.
using the 600 dpi printer in the graduate computer room produce some graphs with high enough resolution to be used in black and white.

now we get to write methods section!
1319
about backing up images used.

2002-09-16-0931
today we're writing methods.

let's go.

2002-09-17-0921
methods.
need vector drawing program.

1048
so, it looks like that old aperture methods section we wrote is not correct.

It should be correct for the line display, but not the isotropic & tl display.

If I remember correctly, after we worked on the line display (after we ran the line display study), we sat down and attempted to re-decide how we wanted the line + pentagon display to look.

we got rid of the speckle and decided to make it so the pentagons and the narrow stripes were the same color (no coming forward or going back effects).

2002-09-18-0936
Alright,

1016
make the job something I can do in a distracted state (filing papers).

1057
I thought there may have been a series of practice circle images.

1119
Hal appears content with this document.
however:
It needs to have explanations of the standards being used for spin, slant, tilt.

It should have a diagram demonstrating the effect of tiling (easy enough).

He explained that a diagram of the important proportions about the physical setup is all that is necessary. If there are already drawn out diagrams, we can use those.

1204
now for diagram showing tiling.

2002-09-19-0927
0942
note that the tiling/mapping was messed up in all the scene files we were using

U, V,  were set to 90,
but they should be zero
W should be 90. that is all.

1146
a little confusion about FOV and for good reason. We were missing several things.

(1) The aperture in the 3ds scene had been made wider. from 2.6 to 2.68 I think.

(2) The camera's field of view is irrelevant because the viewable area is determined by the distance of the aperture from the camera, in our case.

1238
The width of the image on the screen which the physical aperture should line up with is: (apparently from notes) 13.45 * 2 cm. I think, according to what Hal told me, that 200 units / (width of image subtended by field of view) should correspond to 51.7/(13.45 *2).

1242
I'd say we're done with the physical set up section. And on to 

1317
well, quite possibly I will finish tomorrow. Which would be nice.

2002-09-20-0935

1101
factoring.

2002-09-23-0940
1325.. yah a bit late today.

0948
old stuff being cut:

Method
Method for studies 1 - 4 
Study 1: lines
2: tex + lines
3: iso
4: fc
how should we organize this- schedule our work?
We should separate out the parts which are consistent for all studies.
Then write about the things which are unique about particular studies.
Note: refer to surface texture as being the thing that is spun.
Note: we need to define spin, slant, and tilt?
Cruft to perhaps be used later:
Summary:
Nine participants took part in this study. Seven were recruited from the graduate and O.D. students at SUNY College of Optometry; the PI and his assistant also participated. The participants' task was to monocularly view through a circular aperture a sequence of two-dimensional computer renderings of slanted surfaces and to specify "the direction the surface appears to be going away from you." The following paragraphs will detail (1) the characteristics of the renderings and (2) the conditions under which the renderings were viewed.
Degrees of freedom of the plane
The plane (combined mesh and pentagon surface) can be spun (rotation orthogonal to the line connecting camera and target, centering about target), slanted (rotation orthogonal to the surface of the plane, about a line in the plane that passes through the camera's target (center of the plane)), and tilted (rotation of the line about which the plane is slanted that is orthogonal to the line connecting camera and target).
Include diagrams here! (Fig. II)
Layout
Fig. I presents the layout in three dimensional space of the elements of the scene. (could use 3-d shot in presentation, or use multi-viewport view. If the former, note that for the purposes of illustration, the donut has been enlarged and moved further from the camera, but the general proportions remain the same.)

2002-09-24-0936
1320

today we are:
working on the data analysis portion of the document.
and labelling graphs.
that is all.

1308
need to fix labels of the graphs. those which aren't converted tilt difference, shouldn't have converted tilt difference in their title.

2002-09-25-0944
so, Impossibly late today because of my new habit of internetting before work combined with my old habit of riding with carmen...

Puts us all the way to 1330

today, we're finishing up the doc regarding data analysis and fixing graph labels.


1249
What is 
sheet 1 in last960-converted-difference-and-misc...

2002-09-26-0931
1315
we'll finish today...


1214
files to backup:
the graphs &
the aperture methods doc.

1325
finished at least first draft (data an section may need revision)

still to print.

2002-09-27-0926
1310
today, review what was printed yesterday.

1141
done reviewing.
There was a guy, perhaps not a grad student in the grad student computer room! Next time I see him there I'll get him out! (if so)

Now to fix that old bug.
(correct bug in maxscript labelling of generated images)


how will we fix that bug?

let's look at how we fixed it in the data- it's historical.

What were the transformations I did and why didn't I write them down in here???


We can look at the data base.

a:
The spin values were not correct. 
here is the transformation that we used:
for all positive spins:
-90 is added
for all negative spins:
90 is added
000sp -> 90
-00sp -> -90

we can do the same transformation at the time of labelling... or we can try to get the problem at the root...

I believe the problem was the axis we rotated things around.

2002-09-30-0946
take care of the bug.
Then, stereo.

1059
bug appears to have been fixed. By looking at an older copy of the script and making sure current version was doing same. The axis

old:			--rotateaxisvalue = 0
new:			rotateaxisvalue = 90

old:             in coordsys world about $target01 rotate $camera01 (0-ntilt) y_axis
new:             in coordsys world about $target01 rotate $camera01 (90-ntilt) y_axis

1115
bug appears fixed (compared old with new)

Now making animation of 30 deg lines only spin

1222
now making python program to display an animation...
1320
must browse to open script or will not find needed include scripts.
Could set include dir or something else.

2002-10-01-0945
1330

working on the animations.

Questions:
are .bmp's faster?
what happens with big images?

and need to backup.

files

1044
wrote new filtering function so that image directories may contain directories (of other images, usually) without messing up the program! --> not in session.py yet)

wrote program to convert images from png to bmp. using pil. seems to be the second time I've done this. but, remember, it is in the animation.py script.

2002-10-02-0937
0945
1330

1110
talking to hal about auto-free things was fun.

showed him his data from the Forced Choice experiment- nothing extraordinary, and there weren't any strangely low percentages for the spins where there were no correct answers.

Here are the specs/specifications on the computers we have been using (this was collected because we were attempting to determine why g6-200-2 is running the animations slower than g6-200. G6-200-2 is the one used to run the experiment. G6-200 is the one I use.

g6-200
128 MB RAM
200 MHZ pentium
4mb vram
Matrox Graphics, Inc. MGA Millenium
Chip Type: MGA-2064W B2 R2
DAC Type: TI TVP3026(175MHz)
nt 3.51 upgraded to 4.0 with sp 3

g6-200-2
nt 4.0 sp 5
64 MB RAM
200 MHZ pentium
4mb vram
ATI Technologies XPRESSION
Chip Type: Mach 64 GT-B

1123
now creating new backups of data.

to do on g6-200-2 backup image data.

2002-10-03-0950
0945 - 1330
it appears the tape drive backup errored.

1205
Hal went through the logic of display making for stereo with me.
It is also in the help for the program we're using.

we're using 12 units as the difference to offset the camera for making stereo pairs.
51.7 * 4 ~= 200
6 * 4 = 24

6 cm is generally the distance people's eyes are apart.

1321
I tried moving the thing back, but the method I used was not effective.

2002-10-04-0946
what are we doing today?

Would be nice to find way of aligning/producing images so we know how to do it automatically.

Hal was also interested in higher resolution images.

distance between eyes should actually be 23.21 units not 24..
[I think the 23.21 units was calculated using 6cm separation between cameras]

IPD

1305
so, we need the max resolution for creation of stereo images.

things to worry about:
o crosstalk
o color mapping
o and what is done with unused horizontal information?

2002-10-07-0951
1335
today, we can refresh ourself on what we've been doing.
It's been a long weekend.

I can also work on looking at why the backup failed.

1038 the tape is still doing something..

1040
now making a rendering
that would be 1600 x 565

when the display was calibrated, it mentioned that 70 blanking lines were used. So, from a 1600 x 1200 image, only 565 of the rows in the image are being used.

1337

2002-10-08-0953
Yep 1335

we're going to make the script so the lines are flipped and back to back...
hmm.

1335
tomorrow, we're going to the win3d.com site ..

2002-10-09-0935
1057
wrote hal another email regarding proxyblocking.

now on to win3d.com site.

2002-10-10-1002
a bit late-
so we're going to 1345- 

Our basic goal is to find a way to do the spinner program using the stereo display methodology.

the firt thing we hould do is intall the sdk and 

the  key i not working.

this sucks

1011
1020
to do:
get hal to buy an ms natural keyboard elite.

Allright

to do:
Install sdk
run demos

1050
so far, it's a no-go.

Their demo programs don't run.

let's try making our own image to be displayed by the hardware--
take screen capture, then edit.

So far, so good.

1110
well then.

now, all we have to do is write our own algorithm to create right 

what should we do?

Get the spinner program to run in stereo.

(1) We generate left and right eye images using 3dstudio.

(2) We make those images into a stereo pair--the bms format (is this necessary?)

(3) We get the images into the overunder format: ensure there are 70 blank lines between them.

(4) We draw the pointer in the appropriate place so that it appears for both left and right eye.

1137
pygame is ok with 1600 x 1200.

1143
remember that in the animations, bmps load faster than pngs (no conversion).

The basic problem is, that everything put up by pygame needs to be run through the algorithm that makes the over-under images.

not so.

one could tell people to press the stereo switch when the non-stereo stuff will be displayed.
but if one has to gen an algorithm- one could just gen fixed displays for everything not requiring user input.

o.k.

so we gen a bunch of stereo pairs.

Their res should be 1600 x 1200.

how can we do that?

well-
we can max out the height of the image. Then we need to center each image on the center of the aperture, as the aperture corresponds to the plane of the monitor. So we'll have to crop from one side and add to the other for each image.

Assuming we have two images of desired resolution one for left, one for right.

Now we need to create the overunder display.
We will chop 

1202 

of 1200 horizontal lines, 70 cannot be used. remainder must be divided between the two images.
we have 1130 lines to work with.
/2 = 565

how do we get from 1200 to 565?

1200/2 = 600

(remove every other line)

still need to remove 35 lines.

so we will remove 17 from the top and 18 from the bottom.

so the pygame image that pygame will be loading will be the one produce by that program.

now, is there an easier way to do this?


can we do quad buffer stereo at what resolution?

what do we need?

how could that be programmed?

1211
 let's  spend until 1300 (at the most)
researching python, pygame, quad buffer stereo.

O.k.
then, begin with the design of the process to create the stereo pair (crop and add the appropriate amounts in the right places).



2002-10-11-1002
we're going to 1315
since we had an extra .5hr yesterday.

The goal for the day is:

Automate the creation of two images which are a stereo pair from 3dstudio.

If we get done with that, then
automate the creation of the over-under display.

That's all.

1017
For every image we rendered before, we need to up the resolution.
o we need to create a right and a left eye view.
o we need to properly align the images.

Changes from previous script:
    o all rotation done about a helper point set at 150,150,0, not _target01_
    o camera has been moved back (and target) (how much?)

o we cannot use the rotate camera method.

    o the aperture has been moved to be even with the target. target is currently at 162, -50, 150.
    o and radius of aperture changed accordingly.

1037
if we can get the conventions of the utility scripts to match our conventions, we can use those methods to create our displays.

that is something that should be done, anyways.

leave camera oriented as it is and then move it left and right of center.

1146
(1) let's work on fixing utility script so follows conventions.

(a) first, we must spin the panel. The amount we spin it is dependent upon what the tilt will be.

1305
we should use two cameras, permanent, so to not have to keep moving one back and forth.

1325
we appear to have got it working.

To test it, though, we should run the utility (need to add helper point) on the old _1000pents scene file. and compare the result with the renderings used in the experiment.

1411
o.k.
we've got it, 
and I've tested enough to be all but sure (of course one approach is to think it through, but for some of us...)

So let's backup utilitiesstereo.ms

    o make note that the orientation of the tiling has been changed from how it was in previous scene files. (90 degrees)

    

o we should also write up a report of what we've done for the past month

o.k. let's go.

1422
just about done backing up files (had to make more room) 

2002-10-15-0955
so, till 1340 or so

Today we're going to implement the rendering of the displays in the script since we have a method that meets the standards (we've demonstrated to our satisfaction. So we need two cameras... will there be other changes?

o we need a way to align the scripts.

1006
we need to alter the spin and perhaps other functions based on the utilities we made-

1123 potential problem:
270t_-50sp_045sl is not matching perfectly.

My current guess is that it has to do with a change in the tiling- We can compare old and new frontal renderings.

1213
in coordsys world about $target01 rotate $RotPanel (-50) y_axis
in coordsys world about $target01 rotate $RotPanel (45) [1,0,0]

The above is giving me something slightly different than:

in coordsys world about $point01 rotate $RotPanel (-50) y_axis
select $RotPanel
in coordsys world about $point01 rotate selection (45/2) [1,0,0]


1219
not exactly a surprise there.

take out the select and /2 code and see if it still works.

1233
Ok. that was the problem. The bug is squashed.

1234
now to generate stereo pairs (add second render for second camera.

1332
we have a problem with the lines passing in front of the aperture when the surface is slanted 45 degrees or more.

But, basically, we have our script in place for generating stereo pairs

The cropping still needs to be done.

Let's back up our work and-

2002-10-16-1002
till 1345!!
first issue was:
45degree slants, lines protruding through aperture.

1016
that problem was fixed by moving the cameras, targets and aperture +10 x

now we need to crop an edge off one image to get the circle centered.

1020
we'll have to render two 1600 x 1200 images.

1027
aperture diameter needs to be narrower so lines (35 total) can be removed.

1038
so, we have our image. how should we crop it?

if we know the center of the aperture, we can center the image about that.

1046
the bms is (bit map stereo) is 2666 by 1200

This using 3DPIX-NP to align the images.

This suggest that if I take the first 1333 columns of the R image
and the last 1333 columns of the L image I should be set.

let's try it with PIL.

1600 - 1333 = 267

133

1339 there was as bug in the PIL's example roll function-

now fixed. should tell them!

2002-10-17-1007
til 1345 again... or so-

today we're going to go from the two aligned displays to one over-under display.

first let's finalize the alignment script.

1254
interestingly we got the netrender maxscript plugin to work, which means we can submit net jobs from script.

one problem with it is that we need to specify the name of the file that is rendered.

currently submit netrender uses the settings of the 3dsmax file, one of the settings contains the file name.

Can the file name be set from script without actually rendering an object?

1306
could do:
Have a bitmapimage which contains desired image settings...

let's forget about it right now, especially since we need to do something after.. That problem is surmountable as well.

hmm.

1329
o.k. well difinitively its a no go.

We're stuck with one computer for rendering--
one last thing to try.

1333
no. thinking abou doing something with the output.

so, about 45min on this now known to be lost cause.

Interesting, though.

1352
looks like we got the script integrated, 
so, tomorrow, we'll buy keyboard and do overunder.

great!

need to backup files!


1355
python script will need error log?

2002-10-18-1418
we're back. and with a nice new keyboard.

feels good.

smooth.

it is a beautiful day.

so, we're looking at till 1800, but -30min for keyboard buying.

so more like 1730.

1421
by the end of the day I'd like to have the over under format images being created by the python script.


1737
argh-- delayd stuff in PIL is getting me.
use myimage.copy not im1=im2!!!

1742
we got something that sort of works. (not as good as the set prepared by the other program.)

backing up files, and leaving.


2002-10-21-1105
I think we're on.
so- to 1505-15 = 1450

we need to figure out why the image we're generating isn't quite working.


2002-10-22-0817
left early yesterday (really did almost nothing, except get some Idea why the image isn't working)

The image gets distorted because more lines are taken from the top and bottom than from the middle compared to the image produced by 3dspix np program.

perhaps if we adjust the display so that it appears circular, the stereo effect will be better.

to do today also:
tape drive clean and try using new cartridge.

0847
attempting another backup.
not sure if the tape cleaning did anything.


now we can streamline the image generation script.

I'm not happy with the stereo effect.

we should also make a test image like hal set up for us.

let's review our script.

0921
unneeded cruft from script:
was roll function (a lesson was learned from the mistake-- a one line statement was all that was needed, already coded, if I'd read the documentation)
#xsize, ysize = image.size
    #delta = delta % xsize
    #print delta
    #print xsize
    #if delta == 0: return image
    #mycopy = image.copy()
    #part1 = mycopy.crop((0, 0, delta, ysize))
    #part2 = mycopy.crop((delta, 0, xsize, ysize))
    ##unfortunately, the order of the following is significant! apparently part2 pasting affects part1 (lines previously were reversed). to get around this bug perhaps make copies of the image prior to making the assignments to crops of the image.
    ##2002-10-17-1010 now, a copy is made see above.
    ##finally reading doc found the story on crop: (but probably could have used the offset function instead of this roll.
    ##im.crop(box)
    ##=> image
    ##Returns a rectangular region from the current image. The box is a
    ##4-tuple defining the left, upper, right, and lower pixel coordinate.
    ##This is a lazy operation. Changes to the source image may or may
    ##not be reflected in the cropped image. To break the connection, call
    ##the
    ##load
    ##method on the cropped copy.
    ##
    ##    
    #image.paste(part1, (xsize-delta, 0, xsize, ysize))
    #image.paste(part2, (0, 0, xsize-delta, ysize))
    #return image

1231
we created a demo image containing a disparity and calculated the disparity to be 14.3mm
The measured disparity ranged from 14.6mm to 14.8mm (two pixel variability due to antialiasing.)

now, we should create a display with a box in it.

and one that is black and white.

1314
we're out of here.

2002-10-23-0950
1335
to do:

(1) I should, ideally write the to do list before I leave.

a: practice on that display we generated yesterday (cube) hal explained the difference between crosstalk and double images.

b: deal with tape drive problem. why is it failing.

c: get pointer working / sessionman

1009
was able to view the cube display as three dimensional.
It helps to have my head in the right place. (in the location where the cameras are approximately)

1109
working on the travan tape drive problem.
NT thinks it is a Conner CTT 8000-S
Conner, apparently merged with seagate.



1234
unfortunately, I turned off the aic78xx driver, 
now g6-200-2 will not boot.
emergency repair disk.

the seagate tech support guy at 405 936 1400

said the driver was not the issue (I had attempted to install a new driver from the seagate site)

He sent me in email a firmware upgrade from 1.17 to 1.22
which I should be able to install from dos.

the case # is 481713
the warranty is 2 yrs on the drive.

1239
in the meantime, lets consider how to run our python program in stereo mode.

o : we'll probably have to make certain displays into over-under format-- all static displays. Text, such as username can be entered in the top half of the screen.

lets copy the old session program and call it stereosession.py


What screens should be created as image files and then made into over-under displays?


Perhaps we can just make sure the program draws and inputs text on the top half of the screen. It will look fat, and be visible to only one eye, but should work, & with less modification.

1335
we've made initial steps on new script--

unfortunately our xdrive is out of commission and we need to work around that. not difficult.

for tomorrow:

we really need to see what these displays look like with stereomode turned on.

2002-10-24-0901
cool- till 1245 or 1300 because of monday.

today, continue working on making StereoSession work.

and get g6-200-2 back on it's feet.

0905
first we'll do the rom update of the CTT drive.

0920
that is in process. a bit of a stupid thing to be doing since hal did ask to wait until the system was restored, 
why do I do such things?

0936
well, the nt is ready for kerin. unfortunately the help says reg entries will be restored to way nt was when nt40 was first installed. I believe this should be incorrect.

0953
so what to do to make stereo session ready?

lets make sure all text and messages display in top part of screen above the 70 line part that is removed.

let's factor out the displaying of text--

1054 was talking to hal about cybernot-
was dealing with a problem in python where I forgot:

def _displayMessage(self,width,height,yPos,displayString,textColor):

I forgot the self argument.

the error message said six were being given--
i guess that self is automatically passed in.

1057
new calibration image, what should it look like?

1104
answer: we're not yet sure.
stereo calibration image? (two circles at different depths centered over eachother)

1114
we can also move the virtual aperture to be out where the lcd display is instead of where the monitor phosphor is, or even a bit more in front of the lcd.

1131
we think we've factored out the code for displaying messages. into a separate function
Currently the old code is commented out, but will delete after successful runs.

need to move the input box code to the top half of the screen.

1218
unfortunately restoring the system registry using the repair disk messed some things up- horrible.

probably should not have chosen that option and instead looked at what the simple repair startup environment options would have done...

that quite possibly would have been all we needed.

in any event, with the script, the main remaining issue is probably the pointer.

2002-10-25-1000
 to 1345

today: we have a working computer. although it doesn't do network and 
so we'll be working on the stereosession script.

1150
we showed hal a demo of the program working in stereo.

The remaining tasks are to do something about the pointer. Maybe use 3d studio to render 360 pointers, one for each degree? Or?

And to render more images.

We'll get images started rendering while we work on the pointer.

Computers are still not networked.

should make script so that it deletes unneeded images, and renders to appropriate directory.

1211
ready to start rendering.
made script deletefiles from which it makes the over-under image.

1223
changed scene file to use local map since network is down.

1247
interestingly (though we knew this)
when rendering .pngs with the script, 3dsmax uses the settings from how the last png was saved using the gui. It's possible since were not using the network we could speed things up by rendering as .bmps and then saving as a .png in the 256 grayscale mode.

currently things are working, but I think I'll try that.

1252
it's set to : using the 3ds gui: grayscale 8 bit.

1304
our testing is complete.

It appears it is better (final size wise & no obvious speed penalty (though I did not measure)) to use the grayscale 8 bit setting and output from 3dsmax .png files.

this means that all of our existing images could have been much smaller! (rendered as 8 bit grayscale as opposed to whatever they were rendered in!)

1314
amazing.
so we're down to 59k per image.

let's start rendering the whole set of 480 then.

first let's update the backup disk.

1335
backup completed.
start the rendering.

2002-10-28-0955
to 1340
argh!
we were messing with setting up a USB mouse.

1009

Most of the files rendered alright, but
appears that the python scripts errored in some way.

1019
updating .vimrc.

1022 completed.

so the script making the over-under images errored in some way.

In addition to us not getting zero spin  & - zero spin

1026
btw, unplugging /plugging in both the mouse and KB to g6-200 worked fine-

no need to reboot.

1041

C:\WINNT351\system32\cmd.exe /c CropImagesForStereo.py
Traceback (most recent call last):
  File "C:\_research_cleath\Documents-By-Date-and-Study\2002-10-01-Stereo-Study\
PythonScripts\CropImagesForStereo.py", line 53, in ?
    myImage = offset(myImage, 133,0)
  File "C:\PYTHON22\PIL\ImageChops.py", line 134, in offset
    image.load()
  File "C:\PYTHON22\PIL\ImageFile.py", line 166, in load
    raise IOError, "decoder error %d when reading image file" % e
IOError: decoder error -3 when reading image file
shell returned 1
Hit any key to close this window...

file://localhost/C:/_research_cleath/Documents-By-Date-and-Study/2002-10-01-Stereo-Study/Images/stAL_0000120t_-90sp_045sl_li_L0000.png


For all of those 

?

1202
we corrected all the ones that the script  errored on.

we're left with 456 images--

hmm.

we thought we expected 960.

since none of the - zeros are there is the number right?

1209
12 tilts
2 slants
19 spins (since no -0)
=456

good.
with -0 spins we should have:
24 more
=
480

which is the correct number.

why doesn't neg spin rendering work?

1226
seems like it was a leftover code mod issue-
we ended up making myoutputfile
global..

things should work from now on.

1237
o.k. script set up to render the last 24 images. We'll

set it up before we leave- in about 1hr.

now, look into network issue?'

2002-10-29-0957
1000-1345

1005
on our list to figure out:
how to properly back up NT SYStem registry

1143
rdisk /s 

to get the files in the /winnt(?)/repair directory updated

1349
looks like we got it working.
by copying bits of net related registry from g6-200 to g6-200-2
uninstalling networking and then re-installing.

that's it.

2002-10-30-1003
to 1345

today I believe we need to cleanup from yesterday.
make a new emergency repair disk and go over backup procedures


today I believe we need to cleanup from yesterday.
make a new emergency repair disk and go over backup procedures

and then work on the pointer issue, and on viewing rendered images.

1100
talking with hal about systems.

and that we need to make new emergency repair disks by typing 

rdisk /s

seems before the /s was not being used and so the files in winnt(?)/repair were not getting updated, so old registry entries were being put on the repair disk.

1105
The commands I've been using to remap the network shares are as follows:

net use x: \\g6-200-2\images * /USER:g6-200\leath

then it asks for password.

that approach, however is not satisfactory.

net use x: /delete  to delete the mapping

net use x: \\g6-200-2\images /persistent:yes

works fine.

persistent (needs to be restored at next logon)

I think the passthrough feature is taking effect (same user id on this system, same password)?

1114
we also previously had a share for the directory:

\\g6-200-2\_temp\cleath

that is where the program code is stored (session.py, sessionman.py)

and a share to the 3dsmax 2.5 directory on that computer.


net use y: \\g6-200-2\3dsmax25 /persistent:yes

net use z: \\g6-200-2\cleath /persistent:yes

1130
finished remapping

1130
lets do the erds (emergency repair disks)

1224
done with emergency repair disks.
talked with hal about the difference between updating repair info and creating repair disk

1225 now, let's get back to working on the script.


o start backup of main g6-200-2 disk before leaving today

1329
talking with hal about ports and internet diff bet newsgroups access, email access, web access.

1331
our images have problems, with bars poking through edges.
this could be handled with PIL, could it be handled in the scene? Handling it in PIL might be best.

1344
will work on this more tomorrow. backup of c drive of g6-200 has been started.

2002-10-31-0946
to 1330

0948
back up of g6-200-2\c: was successful.


0949
I think I had an idea for processing the images, to remove the part where the stripes go thorough the aperture.

0955
no, .

I don't know of an easy way yet.

1022
by extruding the aperture 150 units toward the camera,  the problem appears to be eliminated.

Need to re-render the images.


1025
think about how to explain image processing for hal.

then, pointer, work on that.

1230 we have a plan for the pointer
take rotated pygame image & remove everyother line on the fly before displaying it. maintaincenter?

1306
conversion from pygame image to pil image occurring reasonably smoothly.

1348
due to some typos, took longer (cut and paste errors)

but got a programatically squashed pointer!

2002-11-01-0937
1202
spent the past 1.5 hrs realizing that the display on g6-200-2 needed to be set to 65,xxx colors from 256.

After restoring, it had been set to 256 and this coloring had never been changed.

although the resolution was changed.

the error python gave was:
pygame.error
alpha blits to 8 bit surfaces currently unimplemented. 

I had no clue where the problem was.. 
thank goodness that is over.

Now, 
managed to run the pointer program on the stereo machine.

(1) the pointer needs to be fatter.
(2) I should use the newly rendered images, though they need to be re-rendered.


1320
starting rendering

2002-11-04-1000
-1345
we're on!

today what should be done?

(1) we need to make pointer constant

(2) problems in image rendering: There are still .png s that PIL is not handling.

(3) only 460 images rendered. none of the 0 spins rendered. only the -0s rendered. actually.

images look good. new scene file o.k.

1038
let's focus on 

1210
talking with hal re jury duty.
setting fps to 30 gets things slow enough that pointer movement is fairly constant.

how can we make the code faster?

1212 files to back up. all.
.vimrc.

1225
let's see how fast it can load bmp files.

we already have a means for genning 360 images. so, we'll save them and see how fast they can be loaded. or preload them all.

1251
talking to hal re calibration image.
plan is..


1348
problem: 3dsmax script is rendering wrong camera to left image.

2002-11-05-0957
1009
FYI, camera01 is left eye
camera02 is right eye.

could label them so.

turns out I was wrong, so.

will be labeling cameras so no more confusion. seems I am easily confused.

left image goes on bottom,
right image on top

1114
argh, I switched the left/right in the crop script also.

it appears that yes, right is supposed to go on top, so make it clear in script.

1145
now, do the pointer spinning, saving of images, and preloading.

2002-11-06-1012
The pointer now spins nicely.

the remaining thing to do is work on making the thing of cardboard at the correct size of the stereo image.

first we should determine the real world placement and diameter of the thing.

first we need virtual units:

1356
We now have an aperture, with nice cross-hair lines on it.
and adjusting it to depth of virtual calibration object put it in the range of my calculations.

what's next?

perhaps should write up report on what has occurred in past month.

2002-11-07-0952
0950 - 1335

0956
what should we be doing today?


2002-11-08-1035
1420
yesterday I worked with hal on making a square which would take up the maximum space possible on the display

note that I just uninstalled the logitech mouse driver because if it is installed, one cannot unplug and replugin the mouse without rebooting. downside is: middle scroll is useless.


1049
we finally got our square in approximately the right place, after having the python program start at the 18th even numbered line instead of the 17th.

The numbers we finally used are:
a square in the plane of the display with l=w=101.5 units.
centered about the point between the targets of the left and right eye cameras.

1112
currently looking into tape drive. Backup appeared to succeed o.k. And should try --

I hate that stupid tape drive. It is a big waste of time.

1117
for the time being we'll attempt to re-find all the documents about the physical lay out of monitor and so on.


1130
what documentation could we be working on right now?

1201
have been working on networking :)

editing c:\winnt351\system32\drivers\etc\hosts
to allow use of aliases instead of ip addresses to specify devices on the network.

for fs - it is /etc/hosts.

on g62 it is \winnt\system32\drivers\etc\hosts

1219
hal's here

here's what we have:


127.0.0.1       localhost
192.168.1.50    g6
192.168.1.51    g62
192.168.1.11    fs
192.168.1.10    ea

1225
documentation-
we will be looking at monitor settings.

what have we done in the past month?
much of the work has consisted of setting up the stereo equipment and coinverting the old session program into something that can be used with stereo.

The main issues were:

at the beginning of october, we were still finishing up the monocular stuff, looking at animations, and python's ability to make animations/display different images quickly.

1237
Then, much of the time was spent making scripts/3ds scenes useful for rendering stereo. 

1243
intermission- manually altering calibration screen image to have only one column of pixels left and right-- seems our screen is a bit askew and this will help determine.

1334
seems like we might fix it. appears the screen was slanting down and to the right.

1338
continuing..
to have things

phosphor decay- causing ghosting.
red, red/blue, less crosstalk than white.

1345
to have things usable for stereo, the means of tilting the panel had to be modified. Previously the camera was rotated, but now the panel had to be tilted.

The script needed to be modified to work in stereo mode: currently all text input/display occurs in the right eye only.

I think that's about it.

1418
made hal some images with no green

2002-11-12-1033
on till 1415 :(

calibration routine.

1053
working on set of images with no green combined with images with green.

am reminded that the lab does not need the hub.

1332
looking at ghosting: seems that red is best.

now to reduce brightness of pointer

improve pointer handling code, so if no pointercloset directory, will create it.

1429
pointer at r192


2002-11-13-1000
to 1345
so we've got a red 192 pointer and we're working on calibrating the display today: 
getting things so the circular aperture is actually a circle.


1014
oh, yesterday, I redid the code that lets directories be in a directory from which the image files are drawn (the directories are removed from the imageFileList)


1055
1057
so, 
all images will have green and blue removed.

with pil.

1254
gimp notes:
to be able to stroke a path, the path must have two points.

to get the stroked path to be black, using a pencil, I had to stroke the damn thing twice.

free software, ahh.

1256
now, hal wants us adjusting the image.

1341
started backup.

restored all monitor values.. left hal note..


start new backup of c drive on g6-200-2.

2002-11-14-0943
to 1330
better.


so, today we're working on our channel issues.

we need to convert our pngs to a different mode then call imagemagick channel ops on them?

let's check.

1141
bailed on image magick, so--

thankfully PIL can do it.

1213
documentation.

Let's convert some more images.

2002-11-15-0946
1330

continue converting images. (python script)

did backup succeed.

0955
yes.

1357
took care of hood making.. reasonably close, I think.


2002-11-20-1016
back after jury duty.

The initial aperture is set up.

2002-11-21-1037
working on graphs- histograms by spin- 10 histograms.

1042
line data

1156
imported data from msaccess to statistica using an ms jet connection

using the statistica query option.

2002-11-22-0928
1315

today will go the excel route?

2002-11-25-0945
1330
today we can work on our ethics course and 
keep working with statistica to create our graphs?

eyes worn out.. already.

I'm sick of statistica and would like to find a better alternative.
don't like it's scripting.

see what graphing I can do with python.

or
r
or
s
.

should be able to query the access db and then create a graph.

1122
r-project.org
kitware.com visualization toolkit vtk

levelplot
panel.barchart
levelplot

3-d histograms in not obvious clear way of how to handle them.
sigmaplot.


1125
what do I want?

I want to script the whole process, using one language, no vb.

sigmaplot

did I look at it before?

need to query-db-
our data set of 9 participants,
want 10 graphs times 2

2 slants,
1 graph per spin

within each graph, a histogram (barchart) for each direction of slant.

let's just plug through with vb and..

would be good to manage my queries some other ways as well.

continue lookinfor ways to script graph config.

1310
is arrow more sluggish in stereo than in mono?

according to statistica docs configuring graphs should be doable.

2002-11-26-0945
1330
ask question on r and then?

1054
found what I was looking for.

could use R- might be hard to figure out everything?

1135
working on letting barbara/hal switch between stereo and 2d mode when they want to.

missing lattice.html in r help (html-- will use chm?)

1306
installed R.

in process I had to make diskspace available.

I've installed gimp and then statistica,

so I copied some things to 
X:\Storage-N-Backups-for-g6-200\misc\c

want to defrag drive, 
but
there is no defragging tool installed

we now have 200mb free.

r looks nice. (?)

2002-12-02-0945
1330
Will make a new display for hal
and
learn how to work in r?


2002-12-03-1003 
1345
today:
building displays for hal/barbara. more in a bit.

1315
we now have two probes.
basically,
we're done with the default scene except for two cameras.
$CameraLeft
$CameraRight

1328
that is done.
so, we can now write the rendering script:
11 diff probe separation distances.
two images/per sep distance -> 1 stereo image.

Need to go over with hal what images he wants rendered.
now: backup and leave.

hal: desired IPD? cur: 65mm

2002-12-04-1000
1345
will use 64mm IPD.
neeed to get fov set correctly.

using width of stereo display=370mm
because the height was ~278mm
and it is a 1600 x 1200 display.

1027
using 20.96 as the FOV of stereo display at 1m

1032 now for writing the script to render.

1125 
we also need a way to do 11 offsets no background, each offset 20 times.
in that case, I would gen one offset image and copy it 20 times incrementing the trial label each time.

1209
pos offsets toward camera

1234
need to use filein, not include for function defs to be executed

2002-12-05-1030
1415
a bit late this am
messing with server in va

rendering failed:
ran out of memory, so put gc() in every loop.

and need to move background back:
probes at -100 sometimes disappear.


2002-12-06-1007
1000-1345

problem: we changed the IPD and did not modify the python scripts that generates the over-under image. The result is that the images are not aligned.

also, barbara ran through some of the stereo images and is interested in her data.

work on IPD first. gen some images.

1203
changed offset from 133 to 138

turning off antialiasing in script

switching colors of checker board to 128 and 96 from 192  and 64

probe to 255 red from 192

max offset now +/- 50mm and all extremes are fusable. Even 100mm in front.

to do:
there are still some bugs in script. work on those.

and render a sequence of images.

also hal was interested in having the probe be a pygame sprite. so positions could be specified in pixels.

barbara wants blanking between subsequent probe displays.

1340
got blanking done.
got bug fixed.

render imgs
pygamesprite.
backup.

1341
remember to check if there is a n offset of one line in images.overunder vertically

2002-12-09-0955
0945-1330

1040
The story is:
hal is going to San Antonio Tejas from 12/10 to 12/17


2002-12-10-1013
1000 - 1345
still working on getting images rendered for stereo spin study.
looks like rendering now working, but was very slow.
still need to figure out offset for 64mm ipd in that study.

render prac images two sets,
and whole. 480

in that study how many pixels/mm and how many units/mm or pixel?

from a paper:
looks like we have 266.6666 pix as the sep bet eyes/ipd

with 11.1111 pix/unit.

we we offsetting. each image 133 pixels.

so, the sep we were using worked out to 6.38cm

which is not far from the 6.4 we want

he was dividing
266.67 pix by (41.775 pix/cm)

how many units per 6.4 cm?

24.06 units.

suggesting to me we won't alter the scene (sep at 24 units) or offset, 133 pixels.

so,
we can start the thing rendering.

need to turn on antialiasing.

1115
very top line of antialiased oval top is at 4
"  "  ""                          bottom is at 639.

What should they be?

that works out fine.

600-35 rows /image
bot im starts at 635 (70 blanking lines.)

assuming 70 is the one to use.

barbara said small vert discrep problems did not matter.

so, render 12 prac iso.

render all 480 lines.
take 12 from there for secnd prac.

1134
have to do prac images one at a time.
so will all have same pentagon position.

1144
I forgot.
with the iso, spin doesn't/shouldn't matter.

will do 9 more at diff tilts at 30 slant

1230
a reason for the slowness was we were genning images at 

2002-12-12-1131

 Your USERNAME = SUNYOPT-0081

  Your PASSWORD = leath

  Your training number =  SUNYOPT-0081

**YOU SHOULD PRINT THIS MESSAGE NOW. RETAIN THE USERNAME AND
PASSWORD FOR FUTURE REFERENCE**

Follow the step by step directions after logging on to the
training site.**

STEP BY STEP INSTRUCTIONS TO BEGIN YOUR TRAINING
1.  Go to the training site at
http://www.courses.miami.edu/bin/common/courses.pl

modules 1-5 7,9,10,12



backup scripts.

the things I have to work on are:
(1)Ethics course
(2)Spin study
(3)sprite approach
(4)R Prob. density function.
(5) New drive for this pc. does kerin have a new one?

1048
let's start with the spin study.
make it just like the old one was.

Practice sessions. breaks.
The repeat delay on script should be set.

1144
genfunctions need to handle offset changes and redchannel only preference.

Need to get right IPD for stereo spin study.
previously using something more than 60.

so now we're using
62 IPD as our IPD for both stereo spin and stereo probe studies.
so
we need to adjust cameras and re-render in both.


offsets for both need to be adjusted.

1242

1332
tried installing the ide harddrive and the scsi
that kerin gave me.

scsi probably needs correct dipswitch settings/termination.
in addition, need longer cable.

ide, seemed buggy but was recognized.
however no means of selecting scsi to boot. would fdisk work? Need to ask.

For tomorrow, would like to have probe study for barbara to look at.


1354
looks like we already have the full set rendered.
The only difference is that the ipd was 64 instead of 62

for barbara's purposes probably fine.

should set up display for stereo and run through it ourself to make sure it works.

1405






2002-12-13-1003
1015 
1053 
ran thru some blocks of the stereo probe study.

three left.

180 tot.


we still need to fix some renderings from the stereolines, and run through that.

1305
zf createfold

1356
finished making (not quite finished)
script more resistant to PIL import errors.
CropImages for Stereo script...

perhaps not ideal use of time?

learning more about error handing, how python can be messed up by external modules.

1358
monday we need to get more probe possibilities rendered.

Try a white probe w/bg and w/out bg

try a black probe against bg.

try a darker bg.

render samples for b. g.




work on sprite approach.


2002-12-16-1046 
1030-1415
see above

1148 
two white probes done

1228 
using bg values of 64 and 96 for one of the variants.

1429 --

2002-12-17-1402 
1400-1745

today, we could look at Barbara's data.
finish our trials

sprite approach
run through stereo spin

(1) finish probefc
(2) begin stereo spin
(3) sprite approach

2002-12-18-0955

0930-1315 today

1308 
forgot to include practice blocks and to
have two runs of the final directory

480
480
120 (practice)


1400 

2002-12-19-0958 
1345

continue w stereo spin trials


then, begin sprite approach

1032 
making L=0 and R=1
in ProbeFC data

2002-12-20-0951 
1335
.
1158 

120 more images to view


two issues:

(1) the data loss error with stereoprobe script
        --> so far, not able to reproduce it.


(2) the sprite approach to probes

the bug was due to number of trials not evenly fitting into a whole multiple of trialblocksize 

2002-12-23-1042 
1030-1415
today:
    (1) finish stereo lines

    (2) data analysis

    (3) sprite approach

1157 
redoing first 120
3 data sets:
colin1
colin2
colin3

colin3 = colin1 with first 120 redone at the end
to analyze data,
drop 1st 120 of trials w/ participant name colin1
replace w/ 120 that have participant name colin3

this is in reference to stereospin lines data

1240 
data an

2002-12-24-0953
0945-1330

1006
to do:
get the StereoSpinLines sessionman so it handles the 120 practice trials
and the two runthroughs of the data.

then, sprites

1118 
forgot an elif and 
debugging took a while (in set persession values)

1126 
get intermission screens to work?

1215 
hals stereo spin id is 123

1221 make circular aperture

1222
sprites

2002-12-26-1008
1345
sprites

1205 
we have something that draws rectangles on the screen,
now what?

should make diagram of the pixels in the over-under display, so we know which r.e. locations correspond to left eye locations

we did this before...

entire image:
x -> 0-1599
y -> 0-1199

x(r.e.,l.e.) = x

y(r.e.) = 0-564
y(l.e.) = 635-1199

so add 635 to r.e.  y positions


--
probes should have center positions and then offsets about those positions.

we know the offset between probes

138 pixels 

so right probe xpos (center) should be 138 from l probe


1315
center points and offsets from them

xpos,ypos is the top left corner.

1323 tomorrow am, focus on statistics


2002-12-27-0941 
1325

r

1011
RSPython package

1028
the magic incantation is:
(once you are in the right dir)
test <- read.csv("uh.csv")

now test is the data frame

1237 
using odbc in control panel

set up dsn 'msaccess' 

installed RODBC module for R using R GUI

had to load the module (used gui)

then:
 odbcConnect('msaccess')

appeared to work just fine

not sure how to modify or view the dsn 
I created, however



myChannel <- odbcConnect('msaccess', uid="", pwd="", host="localhost", case="msaccess")


sqlTables(myChannel)
to list the tables in the database


use mysql instead of access eventually?


1316
IPD for all displays is 62 mm

!!!!!!!!!need to regen base probe display to use 62mm IPD (currently 64)
!!!!!!!!!!probe separation also needs to be changed to 62


the offset we were using to align images was  138 - so 276 pixels / 64 mm

which works out closely with what was measured from the


2002-12-30-1016
1000-1345

!!!

continuing R work


2002-12-31-1021
0945-1330
continuing R work

r should rock

should I learn emacs

ess and xemacs

2003-01-02-1004 
0945 1330
same as above
would like to have a script that creates the right graphs for the fc curves

1042 removed vc++

1143
C-h b to see key bindings in emacs

1332
so, we're set up in xemacs
with a black background

and ready to work on our R file.

2003-01-03-1038 
0945 - 1335


today we'll make the graphs for the probe fc study in r/ess

C-g is quit

C-h ? for help



The lines are truncated in the narrow windows.  Thus, entering M-x
apropos RET truncate RET gives you a list with the following entry:

    truncate-partial-width-windows
      Variable: *Non-nil means truncate lines in all windows less than
      full frame wide.

Then typing C-h v truncate-partial-width-windows RET gives you:

    truncate-partial-width-windows`s value is t

    Documentation:
    *Non-nil means truncate lines in all windows less than full frame
    wide.

vsplit is:

C-x 3

1305 finally ready to R

2003-01-06-0949 
to 1330 today
we should have the script done today
we were trying to do line continuations in an r script

1056 this sucks:

Sorry. I was mistaken about the continuation character in the last message.
The "+" merely shows up to indicate the continuation of the line. You could
paste to together the pieces of the query this way (no "+" at the end of the
line).

> h3 <- sqlQuery(myConnect, paste("select * from console where",
+ "foo > 20 order by foobar"))

Perhaps someone will have a better suggestion.

-Bill

1122 
describe-bindings

 (globally bound to "M-? b", "C-h b", "f1 b")

1203 
not able to continue strings nicely

1304 
why don't we make a function that takes the x and y and part name and bg/no bg label and plots it


?

1412 log back in to check ethics test

coplot may help us, lets continue tomorrow
1429 

2003-01-07-0947 
1330
coplot did help us. so now... work on using it right.

1030 and the lines

1052 it is closer that got changed from L/R to 0,1 not background in probeFCnoRC data


1256 
now we have the basic probefc plot working

we're on to doing prob density for spin study

1315 
these are the names to get data for first spin study:
like "hal" or like "summra" or like "eksupar" or like "jenny" or like "yuan" or like "elaine" or like "emily" or like "alice" or like "colin"
sessionlabel like run 1 or run 2

returning 8640 records
1337 tomorrow, can we make other queries obsolete?

2003-01-08-1207 
goal: density for ag converted spin data today
goal: all queries done from script

1244 the demo for probability density we were looking for is in:

Name:  R-intro.pdf
Progress:  623 KB
Speed:  32 KB/s
From:  http://cran.r-project.org/doc/manuals/R-intro.pdf
To:  C:\_research_cleath\Documents-By-Date-and-Study\2002-Multi-Study\R\R-intro.pdf
Size:  623 KB (637,758 bytes)
Transferred:  623 KB (637,758 bytes)
Sort by date:  01/08/03 12:46:05 PM

section 8.2
1328 spent a lot of time thinking i had wrong data/ otherwise messed up because did not examine stem diagram correctly.
1357 scrolling wasn't working now it is. to scroll the bottom window, c-m-v

2003-01-09-0936 
1315
1025 only so long talking to hal about Quinn's providence.

today, we can refine our r script to not require messing with access to access data from different studies.


2003-01-10-0937 
1315
continue working to get queries for different studies working from R script.

1135 we have our query working
now we need to add new vectors to the data frame to replace some of what was done in last960_3 and last960_2

using viper to make emacs more usable

problem w cspectilt calc in r... will have to fix later

2003-01-13-0952 
1330
working on that problem
?

2003-01-14-0944 
the problem has been solved.
the operation was being done once for the whole vector rather than by element.

emacs keymaps from Ess wiki


> Some key keys to get me started in emacs. My particular interest is to
> be learn to use ESS.
>
> R:
> ------
> M-x R Start R session
> M-ENTER resubmit command and place cursor at beginning
> of next command
>
>
>
> Help:
> ----
> C-h b List of key bindings. Use / to search for regexp
> C-h m Mode based help, i.e. context specific help
>
>
> File stuff:
> ---------
> C-x C-f Visit a file, including creating a new file
> C-x C-s Save buffer
> C-x C-c Save buffers, kill emacs
>
>
> Editing:
> -------
> C-_ Undo
> ESC d kill word
> ESC DEL kill word backwards
> C-y paste
> C-space start to select a region (mark)
>
>
> Buffers:
> -------
> C-x C-b list buffers (in another buffer)
> C-x b change to a specific buffer
> C-x 1 make this buffer fill the whole screen
> C-x 2 split screen into two
> C-x o select the other buffer when screen is split
> C-x k kill a buffer
>
>
> Combinations:

> -----------
> C-x C-b C-x o < select buffer > RET 
>

> This will list the buffers, take you to the buffer list, then you select
> a buffer and press RET to enter the buffer.


Loading Viper
=============

   The most common way to load it automatically is to include the
following lines (in the given order!):

     (setq viper-mode t)
     (require 'viper)
in your `~/.emacs' file


     M-x viper-mode

   When Emacs first comes up, if you have not specified a file on the
command line, it will show the `*scratch*' buffer, in the `Lisp
Interaction' mode.  After you invoke Viper, you can start editing files
by using `:e', `:vi', or `v' commands.  (*Note File and Buffer
Handling::, for more information on `v' and other new commands that, in
many cases, are more convenient than `:e', `:vi', and similar old-style
Vi commands.)

   Finally, if at some point you would want to de-Viperize your running
copy of Emacs after Viper has been loaded, the command `M-x
viper-go-away' will do it for you.  The function `toggle-viper-mode'
toggles Viperization of Emacs on and off.

1159 

Manipulating Comments
=====================

   The comment commands insert, kill and align comments.

`M-;'
     Insert or align comment (`indent-for-comment').

`C-x ;'
     Set comment column (`set-comment-column').

`C-u - C-x ;'
     Kill comment on current line (`kill-comment').

`M-<LFD>'
     Like <RET> followed by inserting and aligning a comment
     (`indent-new-comment-line').

   The command that creates a comment is `Meta-;'
(`indent-for-comment').  If there is no comment already on the line, a
new comment is created and aligned at a specific column called the
"comment column".  Emacs creates the comment by inserting the string at
the value of `comment-start'; see below.  Point is left after that
string.  If the text of the line extends past the comment column,
indentation is done to a suitable boundary (usually, at least one space
is inserted).  If the major mode has specified a string to terminate
comments, that string is inserted after point, to keep the syntax valid.

   You can also use `Meta-;' to align an existing comment.  If a line
already contains the string that starts comments, `M-;' just moves
point after it and re-indents it to the conventional place.  Exception:
comments starting in column 0 are not moved.

   Some major modes have special rules for indenting certain kinds of
comments in certain contexts.  For example, in Lisp code, comments which
start with two semicolons are indented as if they were lines of code,
instead of at the comment column.  Comments which start with three
semicolons are supposed to start at the left margin.  Emacs understands
these conventions by indenting a double-semicolon comment using <TAB>
and by not changing the indentation of a triple-semicolon comment at
all.

     ;; This function is just an example.
     ;;; Here either two or three semicolons are appropriate.
     (defun foo (x)
     ;;; And now, the first part of the function:
       ;; The following line adds one.
       (1+ x))           ; This line adds one.

   In C code, a comment preceded on its line by nothing but whitespace
is indented like a line of code.

   Even when an existing comment is properly aligned, `M-;' is still
useful for moving directly to the start of the comment.

   `C-u - C-x ;' (`kill-comment') kills the comment on the current
line, if there is one.  The indentation before the start of the comment
is killed as well.  If there does not appear to be a comment in the
line, nothing happens.  To reinsert the comment on another line, move
to the end of that line, type first `C-y', and then `M-;' to realign
the comment.  Note that `C-u - C-x ;' is not a distinct key; it is `C-x
;' (`set-comment-column') with a negative argument.  That command is
programmed to call `kill-comment' when called with a negative argument.
However, `kill-comment' is a valid command which you could bind
directly to a key if you wanted to.

Multiple Lines of Comments
--------------------------

   If you are typing a comment and want to continue it on another line,
use the command `Meta-<LFD>' (`indent-new-comment-line'), which
terminates the comment you are typing, creates a new blank line
afterward, and begins a new comment indented under the old one.  If
Auto Fill mode is on and you go past the fill column while typing, the
comment is continued in just this fashion.  If point is not at the end
of the line when you type `M-<LFD>', the text on the rest of the line
becomes part of the new comment line.

Options Controlling Comments
----------------------------

   The comment column is stored in the variable `comment-column'.  You
can explicitly set it to a number.  Alternatively, the command `C-x ;'
(`set-comment-column') sets the comment column to the column point is
at.  `C-u C-x ;' sets the comment column to match the last comment
before point in the buffer, and then calls `Meta-;' to align the
current line's comment under the previous one.  Note that `C-u - C-x ;'
runs the function `kill-comment' as described above.

1240 
comment block issues in emacs:
to comment region:
m-x comment-region

to uncomment
c-x r d

or c-u -1 m-x comment-region

1249 
finally we have duped the query for last960

!

in R


2003-01-15-0931 
1315
now learning circular statistics
what should we look at with them?


C-c C-c in R window to interrupt subjob

1114 
= appears to still be an assignment operator in R
== for logical comparison


1229 

Hi Collin,

you can also try overlaying plots using par(new=...)

plot(x,y1)
par(new=TRUE)
plot(x,y2)

this plots in the same device, but take care with the annotations by using

par(ann=F)

to suppress them

2003-01-16-0945 
1330

ah!
0957 
today:
hals data and my data from stereo

1309 
Focus on the probe again

tomorrow we're working on the new stereo setup.

for now, back to r
2003-01-17-0853 
1230
today...

0946 
continuing with conversion of queries to r: last 960_2

new parts of query are cspin_p

2003-01-22-1023 
we're working on a graph-

how to get it from ranging wide to fitting in 0-180?

radians

no

write function that normalises the values outside of the range--
you've done this elsewhere.

if < 0 then add it to 

mod everything by 180?
i think so!

doc found in package base.
it is %%


took a while

1234 double checked proj line calc--looks good


2003-01-23-0932 
we're back to working on the python probe project...

which meanz off the net.

1107
the things we need to do are:

1 gen a bg and non bg image either on the fly or to be saved and reloaded.
2 run the session without a directory of images, since there's no need for images.
3 be able to specify 4 probe positions separately.

so, we need to start with a sequence that tells us bg/no bg, & probe offsets.

for a number of trials.

we should be able to do this by:
changing the load image func so it simply gets the new parameters off the list.

any point in using old code?

intermission screens and such.

let's try stuffing the imagelist with values and run with that?

we need a function that draws our screen given the parameters.

we'll subclass _init imagelist.
and create a list that contains rand gen params: offsets and bg/no bg

then instead of calling load image, we'll
call drawscreen, and pass in the parameters.

sounds reasonable.

2003-01-24-0930
continuing with python probe script.

1013 
so, it basically works.

now we need to draw background.


1058 
so,
plain background bgs have value of 112
I think

bg checks are 96 and 128

1124 
forgot that bg must be overunder.

1149 
forgot that we need 70 lines of dead space

1252 
so we have a good example

meaning we have something that works

still to do?

1303 
tomorrow:
o double-check bg creation process
o get offsets correct

get it ready to run for pilot
recording data and so on.
organizing trials

2003-01-27-1001 

so we're on.
today,
we're getting our script ready for running the pilot
see above.

I think the bg creation process is fine.
the bottom edge of squares is cut off though.

(in the stereo display)


1030 
only five pixels of the last square.

actually 
1200/2-35=
565
565/20.0=
28.25

so 28.25 squares vertically.

---

how /what do we need to do to run pilots?

a practice session?

recording the data, of course.


(1)we need the start position of the left probe set to be in front of the bg

1105
let's have something called initialDisparity

1115 
will have to work over in black room

1149 
so, we got the guess right-
the probes were in front of the bg with the addition of a default disparity.

which means that positive disparities move the probe toward viewer.


1156
how will we set up practice sessions?

and handle recording of data.?

1220 
handle dups by checking for duplicate trialId (used to use imagename)
no! we used N!

which is the trial's order in the list.

1224
think done with setting up practice.

now need to check data recording.


that's it!

1232 
seems to be working nicely

1233 
one problem is,
both probes will be offset.

?


---

intermission screen

1252 
when we've decided on the setup we want,then we'll worry about the intermission screen.

now is probably the time to work on making sure the data analysis script is ready.


and: backup data
and: sort some stuff out, like how the stereo lines stuff is in with probefc.


2003-01-28-0930
we're on...

(1) make sure the r script will handle the data
and organize stuff.

we need an r script for the probe study separate from the stereo lines, and w/o a lot of extra junk.

#1 we should have some data in the db to work with.

2003-01-29-0932 
today we're running through the probe data.

1011
http://www.theaustralian.news.com.au/common/story_page/0,5744,5907075%255E1702,00.html
Long hours at computer 'deadly'

January 29, 2003

THE next time your boss asks you to put in a few extra hours at your desk - remind him it could be deadly.

New Zealand researchers have found that sitting at a computer for hours on end can cause fatal blood clots, just as long flights can lead to deep vein thrombosis (DVT), known as economy-class syndrome. 

They discovered the link when a 32-year-old man who sat at his computer terminal for up to 18 hours a day nearly died after he developed a blood clot in his leg which travelled to his lungs. 

"This is the first reported case of an association between repeated prolonged immobility sitting at a computer and life-threatening (lung embolism)," wrote the researchers led by Richard Beasley from the Wellington-based Medical Research Institute of New Zealand. 

They suggest the condition be called "e-thrombosis". 


DVT is caused by blood thickening in a vein that forms a clot and causes the leg to swell. 

The most serious complication is when part of the clot breaks off and travels to the heart or other vital organs, which can sometimes be fatal. 

Dr Beasley told AAP it was important the community was made aware of this new risk factor for developing fatally potential blood clots. 

"It's unusual for a fit person in their 30s to get such a massive blood clot so we looked hard to find any risk factors," he said. 

The penny dropped when they realised the man worked for extraordinarily long hours at his computer. 

"It also turned out he worked for many hours at a time without getting up," Dr Beasley said. 

"It became apparent that this clearly was the reason why he got the blood clot and it's very similar to the traveller thrombosis or economy-class syndrome." 

Dr Beasley warned e-thrombosis was an outcome of a modern sedentary lifestyle. 

"This appears to be the first report of its nature ... (and) we need to raise awareness of its possibility," he said. 

"In view of the very dominant way in which the computer has influenced our lifestyle, it really was something that we needed to look at in more detail." 

Dr Beasley recommends people working with computers ensure they get up from their desk regularly and do leg exercises while they sit at their terminals. 

DVT as a result of prolonged sitting was first recognised during the Blitz in World War II, when cases of fatal embolisms emerged among Londoners who sat for long periods in deckchairs in air-raid shelters. 

More recently, DVT has emerged as a potential, though very remote, risk for travellers on long, intercontinental flights. 

Pregnant women, people who are overweight, the elderly, smokers and people with coronary heart disease and certain blood conditions are considered to be most at risk. 

The British high court last month blocked a bid by 55 victims of deep-vein thrombosis who had filed suit against 27 airlines, alleging that the carriers had breached their duty of care because of their cramped seating. 

It ruled that the plaintiffs had no case under the 1929 Warsaw Convention on air travel as DVT was unexpected and could not be considered an accident in the normal operating of an aircraft. 

To prevent DVT, doctors suggest flexing one's toes and ankles, drinking water and avoiding alcohol, and getting up to stretch one's legs at least once an hour. An aspirin, which helps to thin the blood, can also help.

back
1204 
need to have script record zero as left, 1 as right
Closer closer

1233
updated inputbox

and stereo session to have larger font sizez


1243 
yee haw!
our query worked.

1302
things are going nicely.

just factor down the probeFC query more,
and learn more about printing from R

1308
very easy to change kb locales... alt shift, once you set them up.

1319 
only thing still in access is the find and remove dups query.

2003-01-30-0926 
today- hals data- 
and--

0955 
well it's broken!!

1036 
there was a bug --
making the font go from 20 to 40 px,

2003-01-31-0931 
continue,

working through budworm example

1008 
worked on getting address changed for RF with Carolynn.

1050 
beginning trying to do an analysis--


offset is like ldose
bg is like sex
probeFC is like numdead

1305 
working on doing analysis without involving the bg factor.

should be easy.

2003-02-03-0934 
we're on!

still working on understanding 

1013 
1024 
talk talk talk

when-

1026 
doing a probit with half of the data.


1129 
now we're studying regression

2003-02-04-0932
today,
we're going through the regression analysis, explaining the steps that we're taking.


2003-02-05-0915 
Yesterday was reading-

today we'll explain the analysis.

The basic procedure:
develop a model,

see how much variance it accounts for,
compared to other models.

given what we're dealing with- we expect the probit model to fit well,
and we have a factor design-

since in the experiment we expect the slopes to be diff,

if intercept corresponds to vert position, then that may be diff as well.

so, how do we write that model?

1123 
yep, we're working with one model and looking for a significant effect of the bg factor.

1129 
let's 
work through it with all the data for the following models:

(with colin's data)

(a) 1 line
(b) 2 parallel lines
(c) 2 lines

(a)
glm(formula = probeFCMatrix ~ offset, family = binomial(link = probit))

Deviance Residuals: 
     Min        1Q    Median        3Q       Max  
-3.15327  -0.77773  -0.09148   0.91510   3.03154  

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept) -0.07368    0.08563  -0.861    0.390    
offset       0.52405    0.04165  12.582   <2e-16 ***
---
Signif. codes:  0 `***' 0.001 `**' 0.01 `*' 0.05 `.' 0.1 ` ' 1 

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 379.014  on 21  degrees of freedom
Residual deviance:  46.681  on 20  degrees of freedom
AIC: 84.178

Number of Fisher Scoring iterations: 4

(b)
Call:
glm(formula = probeFCMatrix ~ bg + offset, family = binomial(link = probit))

Deviance Residuals: 
    Min       1Q   Median       3Q      Max  
-2.2314  -0.5995   0.1917   0.7272   1.4811  

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept)  0.38266    0.12988   2.946  0.00322 ** 
bg1         -0.89972    0.19242  -4.676 2.93e-06 ***
offset       0.57340    0.04734  12.112  < 2e-16 ***
---
Signif. codes:  0 `***' 0.001 `**' 0.01 `*' 0.05 `.' 0.1 ` ' 1 

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 379.014  on 21  degrees of freedom
Residual deviance:  22.383  on 19  degrees of freedom
AIC: 61.879

Number of Fisher Scoring iterations: 4

(c)
Call:
glm(formula = probeFCMatrix ~ bg + offset + bg:offset, family = binomial(link = probit))

Deviance Residuals: 
     Min        1Q    Median        3Q       Max  
-1.75237  -0.54306   0.09956   0.45905   1.60098  

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept)  0.45256    0.14955   3.026  0.00248 ** 
bg1         -0.90492    0.19631  -4.610 4.03e-06 ***
offset       0.69433    0.08694   7.986 1.39e-15 ***
bg1:offset  -0.19683    0.10357  -1.900  0.05737 .  
---
Signif. codes:  0 `***' 0.001 `**' 0.01 `*' 0.05 `.' 0.1 ` ' 1 

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 379.014  on 21  degrees of freedom
Residual deviance:  18.565  on 18  degrees of freedom
AIC: 60.062

Number of Fisher Scoring iterations: 4

anova:

> anova(myModel.OneLine,myModel.ParallelLines,myModel.TwoLines, test="Chisq")
Analysis of Deviance Table

Model 1: probeFCMatrix ~ offset
Model 2: probeFCMatrix ~ bg + offset
Model 3: probeFCMatrix ~ bg + offset + bg:offset
  Resid. Df Resid. Dev Df Deviance P(>|Chi|)
1        20     46.681                      
2        19     22.383  1   24.299  8.25e-07
3        18     18.565  1    3.817     0.051


1202 
now to be clear on what the parameters mean.
let's do a plot.

2003-02-06-0915 
analyze hal's data like with mine.

0943
hal single line

Call:
glm(formula = probeFCMatrix ~ offset, family = binomial(link = probit))

Deviance Residuals: 
    Min       1Q   Median       3Q      Max  
-3.8391  -1.4007  -0.5491   1.5753   4.7877  

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept) -0.27147    0.08032   -3.38 0.000726 ***
offset       0.21605    0.01673   12.91  < 2e-16 ***
---
Signif. codes:  0 `***' 0.001 `**' 0.01 `*' 0.05 `.' 0.1 ` ' 1 

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 397.66  on 21  degrees of freedom
Residual deviance: 119.98  on 20  degrees of freedom
AIC: 157.15

Number of Fisher Scoring iterations: 3

hal 2 parallel lines

Call:
glm(formula = probeFCMatrix ~ bg + offset, family = binomial(link = probit))

Deviance Residuals: 
     Min        1Q    Median        3Q       Max  
-1.75047  -0.90612   0.02924   0.70074   2.43076  

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept) -1.29906    0.16791  -7.737 1.02e-14 ***
bg1          1.92879    0.24235   7.959 1.74e-15 ***
offset       0.29842    0.02597  11.493  < 2e-16 ***
---
Signif. codes:  0 `***' 0.001 `**' 0.01 `*' 0.05 `.' 0.1 ` ' 1 

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 397.655  on 21  degrees of freedom
Residual deviance:  27.403  on 19  degrees of freedom
AIC: 66.565

Number of Fisher Scoring iterations: 4


2 separate lines

Call:
glm(formula = probeFCMatrix ~ bg + offset + bg:offset, family = binomial(link = probit))

Deviance Residuals: 
      Min         1Q     Median         3Q        Max  
-1.390077  -0.325369   0.003363   0.359663   1.763431  

Coefficients:
            Estimate Std. Error z value Pr(>|z|)    
(Intercept) -1.04202    0.15943  -6.536 6.32e-11 ***
bg1          2.03439    0.26922   7.557 4.13e-14 ***
offset       0.23152    0.02897   7.992 1.32e-15 ***
bg1:offset   0.23931    0.07462   3.207  0.00134 ** 
---
Signif. codes:  0 `***' 0.001 `**' 0.01 `*' 0.05 `.' 0.1 ` ' 1 

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 397.655  on 21  degrees of freedom
Residual deviance:  13.503  on 18  degrees of freedom
AIC: 54.665

Number of Fisher Scoring iterations: 6


 anova(myModel.OneLine,myModel.ParallelLines,myModel.TwoLines, test="Chisq")
Analysis of Deviance Table

Model 1: probeFCMatrix ~ offset
Model 2: probeFCMatrix ~ bg + offset
Model 3: probeFCMatrix ~ bg + offset + bg:offset
  Resid. Df Resid. Dev Df Deviance P(>|Chi|)
1        20    119.985                      
2        19     27.403  1   92.582 6.461e-22
3        18     13.503  1   13.900 1.928e-04


1030 
now...
the aperture.

1311 
talking with hal re what the stats mean- 
more work on that needed

and discussion of the aperture.


2003-02-07-0920
today, need better understanding of the numbers in the regression summary, and so on

1002
specifically,
how the p vals are calculated on the glm--
and what 
AIC is 
and fisher scoring iterations.

1109 
talking with hal-
re kurzweil-
re hermit
re homogenization of space.

1135 
AIC is:
Computes the (generalized) Akaike Information Criterion for a fitted parametric model.

make notes of where read about Fisher Scoring iterations-

2003-02-10-0920
continuing reading about regression to better understand the operations.

1222 
p 21 are errors correlated or do they have unequal variance.? if so then no least squares.

1226 
should be able to write null hypothesis for every significance test.

(1) in the summary for a glm model, the significance codes for each term appear to be whether the variance (actually, the residual sums of squares) of the model without the term is significantly different than the RSS of the model with the term.

(2) what is happening in the anova?

what is the AIC?

1323 

2003-02-11-0932 
today, buy foam core board,
and continue regression research.

1142 
I'm not figuring out the AIC.

here's an anova for hal:
          Df Deviance Resid. Df Resid. Dev P(>|Chi|)
NULL                         21     397.66          
bg         1    39.45        20     358.20 3.358e-10
offset     1   330.80        19      27.40 6.441e-74
bg:offset  1    13.90        18      13.50 1.928e-04


1201 
sort of at my limit with this-
but-
the anova null hypothesis is: ?
 
we need to study the anova more,
and compare link= logit with
probit
and see if there's a difference.

1203 
now 
let's start pondering the aperture.

2003-02-12-0929
today:
aperture.



2003-02-20-0915
making a calibration screen.

banded

red in middle, blue border.

1151 
getting a linksys for hal.

1313 
tomorrow- the calibration screen.

2003-02-21-0915
today- calibration screen.

anything else??
no.

let's do it in python.

2003-02-24-0915
now we're continuing with calibration efforts.

get mon, aperture aligned..
1234 
more bands.

for calib screen.

2003-02-25-0917
same as yesterday-

1053 
narrowing aperture to make the proportions fit with screen.

2003-02-26-0914
today- remeasuring display to ensure pixels are square.

1105 
draw crosshairs

2003-02-27-0915 
fixing the script to make the rects proportional

1257 
tomorrow,
write up procedure for getting into position with display

get aperture aligned right way

think about how to run hal

2003-02-28-0918
see above.

Procedure for positioning participant correctly:

1) have calibration screen up

2) have chinrest all the way forward (the clamp at the base)

3) have participant position chair so s/he is comfortable in the chin rest.

4) have participant look thr

1253
so it's aligned

monday, run hal-
40 trials per offset.


on the larger offsets

that's all!

2003-03-03-0917

1147 
well,
hal is running on it right now.

we made the r.e. aperture somewhat smaller on the top, with another piece of tape.

need to add .5 sec blank.
another 110 practice.
1230 
added block of 110

but think I shall not bother-

to make the intermission screen nice.

1251 
tomorrow- questions- r- understanding regression.

2003-03-04-0916
working on data analysis for hal's data.


1045 
connecting all to router.

changed router ip to 192.168.1.1

wan ip:192.195.177.25 
dns: 141.254.1.11
192.195.177.60

1129 
so, we're on.

1150 
turn off/set repeat rate to nothing-
if hold down key during screen transitions- will continue to record-

1217 
http://pythonology.org/success&story=natsworld

class ImgShortcut:
    def __init__(self, fmt):
        self.fmt = fmt

    def __call__(self, arg):
        return self.fmt % (arg)

nov4 =  ImgShortcut(r'C:\img\vol3\20011104\dscf%04d.jpg')
nov10 = ImgShortcut(r'C:\img\vol3\20011110\dscf%04d.jpg')

>>> print nov4(17)
c:\img\vol3\20011104\dscf0017.jpg

1224 
what now?
r focus.

1233 
where was I

1237 
what will be the analysis process,
and what will it mean?



write a procedure section.

(1) do a regression on the full model and see which coefficients are significant.

the procedure in that pdf file?

2003-03-06-0959 

2003-03-07-1120 

today, a list, of software needed to do what I've been doing.

3dStudio Max r 2.5

http://python.org/2.2.2/
Python 2.2 http://python.org/ftp/python/2.2.2/Python-2.2.2.exe
Python documentation: http://python.org/doc/2.2.2

http://pygame.org/
Python 2.2 Numeric-20.3
Python 2.2 pygame-1.4
Python Imaging Library: http://www.pythonware.com/products/pil/

R for Windows 1.6.1
As well as MS Access, and creating an ODBC connection 'msaccess'.
What are the modules needed?


The GIMP 1.2.3-20020101
Vim 6.0
XEmacs

The X:Drive is mapped to g6-200-2/images
Status       Local     Remote                    Network

-------------------------------------------------------------------------------
Disconnected H:        \\home\user0292$          Microsoft Windows Network
Unavailable  Q:        \\g6-200-2\g6-200-2       Microsoft Windows Network
OK           X:        \\g6-200-2\images         Microsoft Windows Network
Unavailable  Y:        \\g6-200-2\3dsmax25       Microsoft Windows Network
OK           Z:        \\g6-200-2\cleath         Microsoft Windows Network
OK                     \\g6-200-2\IPC$           Microsoft Windows Network
The command completed successfully.


1133 
now, for the website.

1150 
copy all that is needed onto the x-drive.

what modules?



2003-03-10-1253 
till 1645 today

we  need to figure out what hal needs to run things.

1311 
on friday,
we installed
python,
pygame,
numeric,
but not pil.

one desired thing is printing out colorized listings.

1322 
:help convert-to-HTML



	:runtime! syntax/2html.vim
<
	Warning: This is slow!

After you save the resulting file, you can view it with any HTML viewer, such
as Netscape.  The colors should be exactly the same as you see them in Vim.

The lines are numbered according to 'number' option and the Number
highlighting.  You can force lines to be numbered in the HTML output by
setting "html_number_lines" to nonzero value: >
   :let html_number_lines = 1
By default, HTML optimized for old browsers is generated.  If you prefer using
cascading style sheets (CSS1) for the attributes (resulting in considerably
shorter and valid HTML 4 file), use: >
   :let html_use_css = 1



1329 
so,
syntax coloring looks great-

we can ask hal what color scheme he likes.

1353 
tasks:
print out listings in b&w for hal
make map of where the storage is.

1556 
so,
now a map of where things are.

2003-03-11-0936 

0938 
today: data analysis.

1202 

Thinking about organization.
what more needs to be done to make things easier?

 (1) network specific code (shared drives etc.)
 (2) What better organization.?



1252 
make refs to bdata a var at top?

2003-03-12-0929 
1315

2003-03-26-1157 
we have two tasks:
(1) a more complete system configuration list for hal,
and fixing the access find duplicates issue.

1240
fixed dup check and removed one 775?


1242 
hal needs a list of-

1247 
list for hal of 
what to install to get system working:
http://www.socsci.mcmaster.ca/jfox/Books/Companion/ESS/

1151
printed doc-
need similar doc for g6-200-2
need to mention drives that are shared.

2003-03-28-1002
now:
ms kb acces 97 & 2k
abstract refs to g6-200-2

& x drive.

1040 
access 97 2000 same
(google search)

now, abstraction.



2003-03-27-0929 
how are you doing?

0932 
the list for hal.

2003-03-31-1012
1345
going over scripts with hal

2003-04-02-1303 
what things do I need on my computer to be able to do all work for hal?

software wise-- we made the list 
ms$ wise:
access, maybe excel-- yeech!




eof.
ongoing:
save copy of script used to runstudy/record data for all non-pilot data.

Monthly report for october, half of november:
what have we done in the past month?
much of the work has consisted of setting up the stereo equipment and coinverting the old session program into something that can be used with stereo.

The main issues were:

at the beginning of october, we were still finishing up the monocular stuff, looking at animations, and python's ability to make animations/display different images quickly.

Then, much of the time was spent making scripts/3ds scenes useful for rendering stereo. 

To have things usable for stereo, the means of tilting the panel had to be modified. Previously the camera was rotated, but now the panel had to be tilted.

The script (session needed to be modified to work in stereo mode: currently all text input/display occurs in the right eye only).

I think that's about it.

recently, hal calibrated the display (made sure the image of the square was square), we selected a pointer color (red 192) and a display color to minimize crosstalk (red channel only).

I just wrote a script in python using PIL to extract the red channel from an image.


o when you leave: start new backup of C drive.



o adjust png saving options for scene file with hope that pil png decoder won't error on any images.
o start backup of main g6-200-2 disk before leaving today

(-3) need to get hal to think about backing up images.

(-2) From now on, periodically, at least once per month, I need to stop and archive, charts, rawdata, images, and _write a report_ or any other needed documentation about what is contained in that archive. Got it? got it.

new site for proxyblock:
www.rsf.fr
