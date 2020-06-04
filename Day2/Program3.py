num= int(input("Enter the number of line required in the pattern : "))

for x in range(0,num):
    print(" "*x + "*" + "  "*(num-1-x) + "*")

for x in range(0,num):
    print(" "*(num-1-x) + "*" + "  "*x + "*")
