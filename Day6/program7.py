def Ackermann(a,b,str="% s"):
    print(str % ("Ackermann(%d , %d)" % (a,b)))
    if a == 0:
        return b+1
    if b == 0:
        return Ackermann(a-1,1,str)
    b2 = Ackermann(a,b-1,str % ("Ackermann(%d,%%s)" % (a-1)))
    return Ackermann(a-1,b2,str)


x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd number : "))
print(Ackermann(x,y))
