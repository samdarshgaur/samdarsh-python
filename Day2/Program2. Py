def Odd_Even(num):
    if num%2==0:
        print("The number",num,"is an even number.")
    else:
        print("The number",num,"is an odd number.")

def Prime(num):
    flag=0
    for x in range(2,num//2):
        if num%x==0:
            flag+=1
            break
        else:
            pass
    if flag==0:
        print("The number",num,"is a prime number.")
    else:
        print("The number",num,"is not a prime number.")        

def Palindrome(num):
    n=str(num)
    L = len(n)
    flag=0
    for x in range(0,L//2):
        if(n[x]==n[L-1-x]):
            pass
        else:
            flag += 1
    if flag == 0:
        print("The number",num,"is a palindrome.")
    else:
        print("The number",num,"is not a palindrome.")

def Armstrong_Number(num):
    sum=0
    temp=num
    while temp>0:
        dig=temp%10
        sum = sum+(dig**3)
        temp=temp//10

    if sum==num:
        print("The number",num,"is an armstrong number.")
    else:
        print("The number",num,"is not an armstrong number.")



num = int(input("Enter a number : "))
Odd_Even(num)
Prime(num)
Palindrome(num)
Armstrong_Number(num)
