import numpy as np                
import matplotlib.pyplot as plt   
plt.style.use('ggplot')

x = np.arange(-10,10,1) #replace these with any values!
y = np.arange(-10,10,1) #replace these with any values!
X, Y = np.meshgrid(x,y) #create a meshgrid of these values


# Using the equation v(x,y)= (x+y)/(x^2+y^2)

vx = X/(np.sqrt(X**2+Y**2))
vy = Y/(np.sqrt(X**2+Y**2))
plt.figure(figsize=(10,10))
plt.quiver(X,Y,vx,vy)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
