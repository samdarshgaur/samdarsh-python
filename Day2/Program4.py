num = int(input("Enter the number of lines required in the pattern : "))

for x in range(1,num+1):
    print("*"*(num-x+1) + "  "*(x) + "*"*(num-x+1))
   
for x in range(1,num+1):
    print("*"*x + "  "*(num-x+1) + "*"*x)
