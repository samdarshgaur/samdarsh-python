row = int(input("Enter the number of lists you want : "))
list = []

for i in range(0,row):
    print("Enter the size of list no.",i+1,)
    col = int(input())
    print("Enter the elements : ")
    sub_list = []
    for j in range(0,col):
        sub_list.append(int(input()))
    sub_list.sort()
    list.append(sub_list)

print("The entered lists in sorted order are : ")
for i in range(0,row):
    for j in range(0,col):
        print(list[i][j],end = " ")
    print()

single_list = []
for i in range(0,row):
    for j in range(0,col):
        single_list.append(list[i][j])
single_list.sort()
print("All lists merged together and sorted in one list :")
print(single_list)
