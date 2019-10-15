def fact(x):
    fac=1
    if (x>0):
        for i in range(1,x+1,1):
            fac=fac*i
        return fac
    elif(x==0):
        return 1
    else:
        return None
        