List1 = []
num = int(input("Enter the size of the List : "))
print("Enter the list elements : ")
for x in range(0,num):
    List1.append(input())

print("The list entered is :",List1)

i = 1
while i > 0:
    if str(i) in List1:
        i += 1
    else:
        print("The smallest positive number missing from the unsorted list is :",i)
        break
