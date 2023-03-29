a=43
b=65

"""def production():
    #local
    a=43
    b=65
    print("Mul:",a*b)

print("Sum:",a+b)
production()"""

print("A:",a)

def getval():
    global a
    a=45
    print("A:",a)

getval()