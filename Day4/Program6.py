def Counting(Tup,ele):
    count = 0
    for x in Tup:
        if x == ele:
            count += 1
        else:
            pass
    return count

Tuple1 = ("Ram" ,"Jetha Lal","Bharat","Mahua","Ram","Mahua","Jeth Lal","Ram","Jetha Lal","Mahua","Jatha Lal","Chinkara","Jetha Lal","Sundar","Mahua","Sundar","Jetha Lal","Chinkara","Jetha Lal")
List = ["Ram","Jetha Lal","Sundar","Bharat","Mahua","Chinkara"]

print("The List of Candidates is :",List)

max = 0
winner = ""

print("The voting results are : ")
for x in Tuple1:
    print(x)
    
for x in List:
    votes = Counting(Tuple1,x)
    if votes > max:
        max = votes
        winner = x
    else:
        pass

print("The winner of the electons is :",winner," by :",max," votes.")
