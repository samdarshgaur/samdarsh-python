dict1 = {1 : "Python" , 2 : "Java" , 3 : "C" , 4 : "SQL"}
List1 = list(dict1.values())
List1.sort()

ele = List1[-2]
print("The second maximum element in the dictionary is :",ele)
