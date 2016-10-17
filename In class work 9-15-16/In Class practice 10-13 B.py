i = input('enter number')
def from0(i):
    if(i>0):
        for x in range(i+1):
            print(x)
    elif(i<0):
        i*=-1
        for x in range(i+1):
            print(-1*x)
    else:
        print(i)



