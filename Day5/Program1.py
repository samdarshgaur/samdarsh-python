def Change0_5(number):
    temp = number
    count = 0
    new_num = 0
    while temp!=0:
        dig = temp % 10
        if dig == 0:
            dig = 5
        new_num += (10**count)*dig
        count += 1
        temp = temp//10
    return new_num


num = int(input("Enter an integer :"))
Changed_num = Change0_5(num)
print("The number after changing all the 0's with 5's is :",Changed_num)
