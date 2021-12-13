#write a python program to find number is armstrong or not:

num=int(input("Enter the number to check:"))
s=0
temp=num
while(temp>0):
    d=temp%10
    s+=d*d*d
    temp//=10
if(num==s):
    print("the number you enter is armstrong:")
else:
    print("the number you enter is not armstrong:")
