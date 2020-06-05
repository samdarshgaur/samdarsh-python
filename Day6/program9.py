List = []
size = int(input("Enter the size of the list : "))
print("Enter the list elements : ")
for i in range(0,size):
    List.append(input())

K = int(input("Enter the value of K, should be less than size of List: "))
print("The list entered is :",List)
List.sort()
print("The smallest element in the list at position",K,"is :",List[K-1])
