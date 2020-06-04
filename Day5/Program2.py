def knapsack(size, List):
    if size == 0 or len(List) == 0:
        return 0
    if len(List) == 1:
        if List[0][0] > size:
            return 0 
        return List[0][1]  
    if List[0][0] > size:
        return knapsack((size , List[1:]))
    return max(List[0][1] + knapsack(size - List[0][0], List[1:]), knapsack(size , List[1:]))

num =  int(input("Enter the number of items you want to enter: "))
List1 = []

for x in range(0,num):
    weight = int(input("Enter the weight for item number " + str(x + 1) + ": "))
    value = int(input("Enter the value for item number " + str(x + 1) + ": "))
    List1.append((weight,value))

weight = int(input("Enter the value of weight capacity: "))
print("The maximum value for the given weight value pair is ", knapsack(weight, List1))
