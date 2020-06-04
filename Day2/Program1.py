num = int(input("enter the number till which the fibonacci is required : "))
a=0
b=1
c=0
if num>0:
    print("the fibonacci series is : ")
    for x in range(num):
        print(a)
        c=a+b
        a=b
        b=c
else:
    print(0)
