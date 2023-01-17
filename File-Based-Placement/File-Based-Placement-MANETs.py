import random
import math


#Grid length
GridLength=input("Enter the Grid Length in meters: ")
GridLength=int(GridLength)

#deviceName of the device
deviceName=input("Enter Device Name in character input:")
deviceName=str(deviceName)


#Number of devices
num=input("Enter number of devices:")
num=int(num)

#center coordinates(x and y) 
C_x=input("Enter X Coordinate of circle center Meters:")
C_x=int(C_x)

#print(C_x)
C_y=input("Enter Y Coordinate of circle center Meters:")
C_y=int(C_y)

#radius input
radius=input("Enter radius in meters:")
radius=int(radius)

#Calculation
radiants=360/num
def multiples(value, length):
    return [value * i for i in range(1, length + 1)]
    
points_rad=multiples(radiants, num)
print(points_rad)
df=open('placement.txt','w')

#print to file and console
for i in points_rad:
    X=C_x+radius*math.cos(i)
    Y=C_y+radius*math.sin(i)
    df.write("%s,WIRELESSNODE,%.1f,%.1f\n"%(deviceName,X,Y))
    print("%s,WIRELESSNODE,%.1f,%.1f\n"%(deviceName,X,Y))
    
df.close
