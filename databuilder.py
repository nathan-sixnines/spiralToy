from PIL import Image, ImageDraw
import math
import os
import numpy as np
import StringIO
import sys

def dist(x1,y1,x2,y2):   
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)   

def offset(x, y, angle, factor):


    retX = x + (math.sin(angle))* factor
    

    
    retY = y + (math.cos(angle)) * factor
    
    return (retX,retY)
    
    
    
def spiral(x,y, img):

    param1 = dist(x,y, 540,540)
    
    param2 = math.atan2(540 - x, 540 - y)
    
    pointList = []
    
    for i in range(300):
        pointList.append(offset(540,540, i * param2, ((param1 + 50) * i / 200) ))
    
    draw = ImageDraw.Draw(img)
    
    draw.line(pointList, fill = 0, width = 4)
    
    return img
        
        
data = np.zeros((1080,1080), np.uint32)

for i in range(int(sys.argv[1]) * 135, (int(sys.argv[1]) + 1) * 135):

    print ("i = %s" % i)

    for j in range(1080):
        if(j% 108 == 0):
            print ( "  j = %s" % j)
    
        img = Image.new('L', (1080,1080), color = "white")
        img = spiral(i,j, img)
        
        

        temp = StringIO.StringIO()
        
        old_file_position = temp.tell()
        img.save(temp, format="png") #"data/measure.png")
        
        temp.seek(0,os.SEEK_END)
        
        
        #statinfo = os.stat('data/measure.png')
        #number = int(statinfo.st_size[:-1])
        data[i,j] = int(temp.tell())
        
        if(data[i,j] < 0):
            print (data[i,j])
            print ("less than 0 at %s, %s" % (i,j))
            stop = 1/0
        
        temp.seek(old_file_position, os.SEEK_SET)
        
        
        #data[i,j] = i * 1080 + j
        
        
    np.save('data_%s' % sys.argv[1], data)
        
np.save('data_%s' % sys.argv[1], data)

print data[0,0]

im  = Image.fromarray(np.uint8(data))

im.save("sanitycheck1.png")