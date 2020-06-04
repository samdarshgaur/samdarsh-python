List = [(12,14,18),(21,22,10),(45,5,3),(0,8,21)]

print("The List before sorting :",str(List))

num = 0
List.sort(key = lambda x: x[num])

print("the List after sortimg by",num,"th element is :",str(List))
