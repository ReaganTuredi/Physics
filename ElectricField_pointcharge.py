import numpy as np
import matplotlib.pyplot as plt

#Calculating the Electric Field of a Point Charge
#------------------------------------------------------------------#
#constants
k = 9e9                         
Q = 0.1e-6     
#defining the locations pertaining the the charge
SourceLocation = np.array([0,0])         
ObservationLocation = np.array([0.1,0])          
delta = ObservationLocation - SourceLocation               

E = k*Q*delta/(np.linalg.norm(r))**3 

print("electric field:",np.round(E[0],2)) #electric field
#------------------------------------------------------------------#


#Calculating the Electric Field at different locations around a point charge 
#------------------------------------------------------------------#
theta = np.linspace(0,2*np.pi, 40) #observation locations
radius = 0.1

SourceLocation_changing = np.array([0,0])         # charge location

fig = plt.figure(figsize=(10,10))
plt.plot(0,0,'ro')    #charge location

for t in theta:
    ObservationLocation_changing = np.array([radius*np.cos(t), radius*np.sin(t)]) 
    delta_changing = ObservationLocation_changing - SourceLocation_changing   #distance between observation and source location 
    E = k*Q*delta_changing/(np.linalg.norm(delta_changing))**3    #E field
    E_new = np.linalg.norm(delta_changing)/np.linalg.norm(E)/2    
    plt.arrow(ObservationLocation_changing[0],ObservationLocation_changing[1],E_new*E[0],E_new*E[1])   
#------------------------------------------------------------------#
    
