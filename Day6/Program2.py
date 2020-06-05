def sort_0_1(list, size) : 
    count = 0 
    for x in range(0, size) : 
        if (list[x] == 0) : 
            count = count + 1
    for x in range(0, count) : 
        list[x] = 0
    for x in range(count, size) : 
        list[x] = 1
         
def print_func(list , size) : 
    for x in range(0, size) : 
        print(list[x] , end = " ") 
          
list = [ 0, 1, 0, 1, 1, 1 ] 
size = len(list) 
print("List right now is : ")
print_func(list,size)
sort_0_1(list, size) 
print("\n List after sorting is : ")
print_func(list, size) 
