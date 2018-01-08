

func=str(input("f(x,y)="))

#+++++++++++++++++++++++++++Human understandable to python understandable convertion part+++++++++++++++++++++++++++++++++++++++

if '^' in func :#this part is to create powers
            i=0
            while i<(len(func)):
                if func[i]=="^" :
                    func=func[:i]+'**'+func[i+1:]
                i+=1

                        
i=0
while i<(len(func)):#This part is to  eg: covert 2y to 2*y
    if i != len(func)-1 :#Just to avoid index error in case of last element being a number
        if func[i].isnumeric() and func[i+1] not in ['+','-','*','/'] and not(func[i+1].isnumeric()) and not(func[i+1]=='.') and func[i+1]!=')':
            func=func[:i+1]+'*'+func[i+1:]
    i+=1
print("coverted form:",func)

#+++++++++++++++++++++++++++Graph plotting part of the code+++++++++++++++++++++++++++++++
def f(x,y):
    return(eval(func))

'''
#HI There if you like this program kindly reply to me via chidha1434@gmail.com and support me by following me on github or stack exchange.. Thank you!!!
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import *

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = arange(-5, 5, 0.025)
Y = arange(-5, 5, 0.025)
X, Y = meshgrid(X, Y)
#R = sqrt(X**2 + Y**2)
#Z = sin(R)
Z=f(X,Y)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z,linewidth=0,cmap=cm.coolwarm, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
