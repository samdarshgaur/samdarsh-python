dict1 = {1 : "Python" , 2 : "Java" , 3 : "C" , 4 : "SQL" , 5 : "Java" , 6 : "C"}
dict2 = {}

for key,value in dict1.items():
    if value not in dict2.values():
        dict2[key] = value

print("Original Dictionary : ",dict1)
print("Dictionary after removal of duplicates : ",dict2)
