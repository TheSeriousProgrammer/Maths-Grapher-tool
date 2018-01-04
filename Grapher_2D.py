n=True
try:
    import numpy
    import pylab
except ImportError :
    print('\n  We have detected that your pc is lack of some essential packages .. \n please connect to internet and press enter')
    input('')
    import os
    try:
        os.system("py -m pip install matplotlib")
        print("\n Installing additional packs .. please dont quit!!")
        import numpy
        import pylab
    except:
        try:
            os.system("python -m pip install matplotlib")
            import numpy
            import pylab
        except:
            print("Please install python3 in your pc from python website or connect to the internet and try again")
            n=False
if n :
    from math import *

    range=eval(input("Please enter the range within which i should plot [eg:(start,stop)] :"))

    def x_axis():
        global x
        x=numpy.linspace(range[0],range[1],1000000)
        x=list(x)

    def function_obtain():
        global func
        func=str(input('f(x) = '))

    def y_axis():
        global func
        global x
        global y
        y=[]
        hi=len(x)
        if '^' in func :
            for i in range(len(func)):
                if func[i]=="^" :
                    func=func[:i]+'**'+func[i+1:]
        if 'e' in func:
            for i in range(len(func)):
                if func[i] == 'e':
                    o, m = func[i - 1], func[i + 1]
                    if o in ('1','2','3','4','5','6','7','8','9','0') and m in ('1','2','3','4','5','6','7','8','9','0'):
                        func = func[:i] + ' * 10 ** ' + func[i + 1:]
                    else:
                        func = func[:i] + ' 2.71828 ' + func[i + 1:]
        l=func.split('x')
        h=0
        while h<len(x) :
            y.append(eval(str(x[h]).join(l)))
            h+=1

    def graphline():
        pylab.plot(x,y)

    while True :
        while True :
            print('\n')
            function_obtain()
            x_axis()
            y_axis()
            graphline()
            choice=str(input("Do you wanna plot one more function simultaneously ? (y/n) :"))
            print('\n')
            if 'n' in choice.lower():
                break
        pylab.show()
        choice1=str(input("Do you wanna plot one more graph? (Y/N) :"))
        if 'n' in choice1.lower():
            break
            print(" \n \n Hope I did good !!!!!!!!!!!")
        
    t=input("\n Hey please send your feed back to chidha1434@gmail.com !!! \n \n Press enter to quit the prog....")
