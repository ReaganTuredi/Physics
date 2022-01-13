import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

#Constants 
k = 9e9                           
Q = 0.1e-6                        

chargeOfChunk = Q/Nchunks

## Length of line
L = 0.2

## Location of the ends of the line
lineStartX = -L/2
lineEndX = +L/2

## Number of segments of the line
Nchunks = 20

## Create locations for the segments
xLocations = np.linspace(lineStartX+L/2/Nchunks,lineEndX-L/2/Nchunks,Nchunks)
print(xLocations)
yLocations = np.zeros(Nchunks)

## Stack locations
chunkLocations = np.stack((xLocations,yLocations), axis=1)

#Finding charge at distance of 0.01 from line charge
Q_est=Q/10
(k*Q_est)/(0.01**2)

