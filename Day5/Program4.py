def Replace_Right(List1,num):
    i = 0
    while i < num:
        max = list1[i]
        for x in range(i+1,num):
            if list1[x]>max:
                max = list1[x]
            
        list1[i] = max
        i += 1
    return List1



list1 = []
num = int(input("Enter the size of the list : "))
print("Enter the list elements : ")
for i in range(0,num):
    list1.append(input())

print("The list entered is :",list1)


print("The list now is :",Replace_Right(list1,num))
