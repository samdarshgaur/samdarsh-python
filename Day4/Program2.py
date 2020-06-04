Tuple = ("Python","Java","C","CPP","Java","CPP","J Query","JS Note","C","Java")
print("The tuple is: ",Tuple)
ele = input("Enter the element whose occurence you want to check : ")

count = 0
for x in Tuple:
    if x == ele:
        count += 1

print("The element :",ele," is found",count," times in the tuple ")
