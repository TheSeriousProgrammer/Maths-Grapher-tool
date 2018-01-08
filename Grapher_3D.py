

def input_func():
    global func
    func=str(input("f(x,y)="))

#+++++++++++++++++++++++++++Human understandable to python understandable convertion part+++++++++++++++++++++++++++++++++++++++
def human_readable_to_py_readable():
    global func
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



'''
    #HI There if you like this program kindly reply to me via chidha1434@gmail.com and support me by following me on github or stack exchange.. Thank you!!!
'''
def f(x,y):
        global func
        return(eval(func))  
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import *

#+++++++++++++++++++++++++++Graph plotting part of the code+++++++++++++++++++++++++++++++
def Plot_new():
    
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1,1,1, projection='3d')
    #ax = fig.gca(projection='3d')

# Make data.
    X = arange(-5, 5, 0.025)#range of points returned as a numpy array
    Y = arange(-5, 5, 0.025)
    X, Y = meshgrid(X, Y)
#R = sqrt(X**2 + Y**2)
#Z = sin(R)
    Z=f(X,Y)
# Plot the surface.
    surf = ax.plot_surface(X, Y, Z, linewidth=0,cmap=cm.coolwarm,rstride=4,cstride=4, antialiased=False)#antialized true make the surface transparent, rstride and cstride make the surface smooth
    cset = ax.contour(X, Y, Z, zdir='z',cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x',cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y',cmap=cm.coolwarm)
# Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.set_zlabel('f(x,y) or z')
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)

# Add a color bar which maps values to colors.
def show():
    
    #plt.title("f(x,y)=",func)
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.zlabel('z')
    plt.show()

a=0

while True :
    choice=int(input("Enter 1 to plot a graph , Enter any other to quit, Your choice:"))
    if choice==1:
        input_func()
        human_readable_to_py_readable()
        Plot_new()
        show()
    else:
        print('Thanks for using me!! Farewell!!')
    
