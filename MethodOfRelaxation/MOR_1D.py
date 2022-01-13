# 1D method of relaxation solver for Laplace’s equation, visualized
import numpy as np
import matplotlib.pyplot as plt

#Using V(x = a = 0) = Va = 0 and V(x = b = 10) = Vb = 10 

mesh=11
a=0
Va=0
b=10
Vb=10

h=(b-a)/(mesh-1)
V_old=np.zeros(mesh)
V_old[0]=Va
V_old[mesh-1]=Vb
V_new=V_old+np.zeros(mesh)

tolerance=0.001
difference=0.01
iterations=1000
count=0

while(difference>tolerance) and (count<iterations):
    for i in range(1,mesh-1):
        V_new[i]=0.5*(V_old[i-1]+V_old[i+1])
        difference=max(abs(V_new-V_old))
    count=count+1
    V_old=V_new+np.zeros(mesh)
    plt.plot(V_old)
print(V_old,count)

#With better accuracy 

mesh=101
a=0
Va=0
b=10
Vb=10
h=(b-a)/(mesh-1)

V_old=np.zeros(mesh)
V_old[0]=Va
V_old[mesh-1]=Vb
V_new=V_old+np.zeros(mesh)

tolerance=0.001
difference=0.01
iterations=1000
count=0

while(difference>tolerance) and (count<iterations):
    for i in range(1,mesh-1):
        V_new[i]=0.5*(V_old[i-1]+V_old[i+1])
        difference=max(abs(V_new-V_old))
    count=count+1
    V_old=V_new+np.zeros(mesh)
    plt.plot(V_old)
print(V_old,count)
