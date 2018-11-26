def temperatureconvertion (C=0, F=32) :
    if C!=0 and F==32:
        F=float(F)
        C=float(C)
        F=((C*9/5)+32)
        print('Temperature',C,'Celcius equivalent with',F,'Fahrenheit')
    elif C==0 and F!=32:
        F=float(F)
        C=float(C)
        C=(F-32)*5/9
        print('Temperature',F,'Fahrenheit equivalent with',C,'Celcius')
    else :
        print('Temperature',C,'Celcius equivalent with',F,'Fahrenheit')
