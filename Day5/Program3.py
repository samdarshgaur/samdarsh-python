def Sort_List(List1):
    
    List_Even = []
    List_Odd = []

    for x in List1:
        if int(x) % 2 == 0 :
            List_Even.append(x)
        else :
            List_Odd.append(x)
        
    print("Segregated Lists are : ")
    print("Even :",List_Even)
    print("Odd :",List_Odd)

    return sorted(List_Odd,reverse = True) + sorted(List_Even)


List1 = []

num = int(input("Enter the size of the list : "))
print("Enter the elements into the list : ")
for i in range(0,num):
    List1.append(input())
print("The list entered is : ",List1)

print("New list is :",Sort_List(List1))
