x = int(input("enter first variable : "))
y = int(input("enter second variable : "))

print("before swapping : x =",x," , y =",y)

x = x+y
y = x-y
x = x-y

print("after swapping : x =",x," , y =",y)
