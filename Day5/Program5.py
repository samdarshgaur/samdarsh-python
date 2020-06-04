def Func(List):
    if len(List) == 2:
        return max(List)
    if len(List) == 1:
        return List[0]
    if len(List) == 3:
        return max(List[1], List[0] + Func(List[2:]))
    return max(List[1] + Func(List[3:]), List[0] + Func(List[2:]))

num = int(input("Enter the number of Houses : "))
List1 = []

for x in range(0,num):
    List1.append(int(input("Enter the value in the House number " + str(x + 1) + " : ")))

print("The maximum stolen value from Houses is", Func(List1))
