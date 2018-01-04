

func=str(input("f(x,y)="))


#+++++++++++++++++++++++++++Human understandable to python understandable convertion part+++++++++++++++++++++++++++++++++++++++

if '^' in func :#this part is to create powers
            for i in range(len(func)):
                if func[i]=="^" :
                    func=func[:i]+'**'+func[i+1:]
                    
if 'e' in func:#this part is to replace e with either 2.7128 or to the power 10
            i=0
            while i<(len(func)):
                if func[i] == 'e' :
                    if i != len(func) and i!= 0 :#just to avoid index error in case of first or last element
                        o, m = func[i - 1], func[i + 1]
                        if o in ('1','2','3','4','5','6','7','8','9','0') and m in ('1','2','3','4','5','6','7','8','9','0'):#the loop checks if e is present between 2 numbers if so replaces it with *10** 
                            func = func[:i] + '*10**' + func[i + 1:]
                        else:
                            func = func[:i] + '2.71828' + func[i + 1:]#If the elements before or after 'e' are not numbers then replaces it with 2.71828
                    else:#incase of last or first element being 'e' replaces it with 2.71828 
                        if i==0:
                            func='2.71828'+func[1:]
                        else:
                            func=func[:i]+'2.71828'
                i+=1
if 'pi' in func:
    for i in range(len(func)):
        if func[i:i+2]=='pi':#replaces pi with 3.142857
            func=func[:i]+'3.142857'+func[i+2:]
i=0
while i<(len(func)):#This part is to  eg: covert 2y to 2*y
    if i != len(func)-1 :#Just to avoid index error in case of last element being a number
        if func[i].isnumeric() and func[i+1] not in ['+','-','*','/'] and not(func[i+1].isnumeric()) and not(func[i+1]=='.'):
            func=func[:i+1]+'*'+func[i+1:]
    i+=1
print("coverted form:",func)

#+++++++++++++++++++++++++++Graph plotting part of the code+++++++++++++++++++++++++++++++
def f(x,y):
    return(eval(func))

'''
#HI There if you like this program kindly reply to me via chidha1434@gmail.com and support me by following me on stack exchange.. Thank you!!!
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
