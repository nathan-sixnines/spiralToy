from PIL import Image
import numpy as np
import math

def cart2pol(x, y):
    rho = np.sqrt((x-540)**2 + (y-540)**2)
    phi = np.arctan2(y-540, x-540)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


pic = np.zeros((1080,1080), dtype=np.uint32)



#with np.load('data.np') as f:
#    part0 = f
#    print part0.shape
 
part0 = np.load('data_0.npy')
part1 = np.load('data_1.npy')
part2 = np.load('data_2.npy')
part3 = np.load('data_3.npy')
part4 = np.load('data_4.npy')
part5 = np.load('data_5.npy')
part6 = np.load('data_6.npy')
part7 = np.load('data_7.npy')


print part6
    
pic[135*0:135*1,:] = part0[135*0:135*1,:]
pic[135*1:135*2,:] = part1[135*1:135*2,:]
pic[135*2:135*3,:] = part2[135*2:135*3,:]
pic[135*3:135*4,:] = part3[135*3:135*4,:]
pic[135*4:135*5,:] = part4[135*4:135*5,:]
pic[135*5:135*6,:] = part5[135*5:135*6,:]
pic[135*6:135*7,:] = part6[135*6:135*7,:]
pic[135*7:135*8,:] = part7[135*7:135*8,:]



min = 3335
max = 88443
diff = 85108

"""
for i in range(1080):
    for j in range(1080):
        if(pic[i,j] < min and pic[i,j] != 0):
            min = pic[i,j]
            print ("min = %s" % min)
            
        if(pic[i,j] > max):
            max = pic[i,j]
            print ("max = %s" % max)
         
        #print pic[i,j]
"""

pic = pic - 3334

pic = pic / 334
        
image = Image.fromarray(np.uint8(pic))

image.show() #ave('test.png')

image.save("map1.png")

# switching polar and xy co-ordinate for next image

radial = np.zeros((540,540))

for i in range(1080):
    for j in range(1080):
        rho, phi = cart2pol(i,j)
        
        rho = int(math.floor((rho / 763.675323681) * 540))
        phi = int(math.floor((phi + math.pi) * 85.9436692696))
        
        if(rho == 540 or phi == 540):
            continue
        
        radial[rho, phi] = pic[i,j]
     
image2 = Image.fromarray(np.uint8(radial))

image2.show()
