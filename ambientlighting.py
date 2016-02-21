import serial
from PIL import ImageGrab
import time
from PIL import Image

arduino=serial.Serial("com4",9600,timeout=1)
print "opening serial port...."
time.sleep(2)
print "port successfully opened"

while(True):
	

	im = ImageGrab.grab()
	px = im.load()

	topr,topg,topb=0,0,0
	leftr,leftg,leftb=0,0,0
	rightr,rightg,rightb=0,0,0

	newtopr,newtopg,newtopb=0,0,0
	newleftr,newleftg,newleftb=0,0,0
	newrightr,newrightg,newrightb=0,0,0

	for toptopx in range(0,im.size[0],2):
		 for toptopy in range(0,im.size[1]/3,2):
			  topr+=px[toptopx,toptopy][0]
			  topg+=px[toptopx,toptopy][1]
			  topb+=px[toptopx,toptopy][2]


	for topbottomx in range(int(im.size[0]/3),int(im.size[0]*2/3),2):
		 for topbottomy in range(im.size[1]/3,im.size[1]*2/3,2):
			  topr+=px[topbottomx,topbottomy][0]
			  topg+=px[topbottomx,topbottomy][1]
			  topb+=px[topbottomx,topbottomy][2]


	for leftx in range(0,int(im.size[0]/3),2):
		 for lefty in range(im.size[1]/3,im.size[1],2):
			  leftr+=px[leftx,lefty][0]
			  leftg+=px[leftx,lefty][1]
			  leftb+=px[leftx,lefty][2]


	for leftmidx in range(int(im.size[0]/3),int(im.size[0]*2/3),2):
		 for leftmidy in range(im.size[1]*2/3,im.size[1],2):
			  leftr+=px[leftmidx,leftmidy][0]
			  leftg+=px[leftmidx,leftmidy][1]
			  leftb+=px[leftmidx,leftmidy][2]


	for rightx in range(int(im.size[0]*2/3),im.size[0],2):
		 for righty in range(im.size[1]/3,im.size[1],2):
			  rightr+=px[rightx,righty][0]
			  rightg+=px[rightx,righty][1]
			  rightb+=px[rightx,righty][2]


	for rightmidx in range(im.size[0]/2,int(im.size[0]*2/3),2):
		 for rightmidy in range(im.size[1]*2/3,im.size[1],2):
			  rightr+=px[rightmidx,rightmidy][0]
			  rightg+=px[rightmidx,rightmidy][1]
			  rightb+=px[rightmidx,rightmidy][2]


	newtopr=int(topr*4/int(im.size[0]*im.size[1]*8/18))
	newtopg=int(topg*4/int(im.size[0]*im.size[1]*8/18))
	newtopb=int(topb*4/int(im.size[0]*im.size[1]*8/18))

	newrightr=int(rightr*4/int(im.size[0]*im.size[1]*5/18))
	newrightg=int(rightg*4/int(im.size[0]*im.size[1]*5/18))
	newrightb=int(rightb*4/int(im.size[0]*im.size[1]*5/18))

	newleftr=int(leftr*4/int(im.size[0]*im.size[1]*5/18)/1.2)
	newleftg=int(leftg*4/int(im.size[0]*im.size[1]*5/18)/1.2)
	newleftb=int(leftb*4/int(im.size[0]*im.size[1]*5/18)/1.2)

	top=[newtopr,newtopg,newtopb]
	left=[newleftr,newleftg,newleftb]
	right=[newrightr,newrightg,newrightb]
	print(str(top[0])+","+str(top[1])+","+str(top[2])+","+str(left[0])+","+str(left[2])+","+str(left[1])+","+str(right[0])+","+str(right[1])+","+str(right[2])+"Z")


	arduino.write('c'+str(top[0])+","+str(top[1])+","+str(top[2])+","+str(left[0])+","+str(left[2])+","+str(left[1])+","+str(right[0])+","+str(right[1])+","+str(right[2])+"Z")

