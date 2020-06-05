num = int(input("Enter the number till which the fibonacci is required : "))
a=0
b=1
c=0
sum = 0
if num>0:
    print("The fibonacci series is : ")
    while a < num:
        sum += a
        print(a)
        c=a+b
        a=b
        b=c
else:
    print(0)

if sum == num:
    print("The sum of the elements of the fibonacci series is equal to the fibonacci number.")
else:
    print("The sum of the elements of the fibonacci series is not equal to the fibonacci number.")
