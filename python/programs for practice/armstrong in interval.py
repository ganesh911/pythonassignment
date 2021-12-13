#write a program to find armstrong number in an interval:

a=int(input("enter the starting inteval:"))
b=int(input("enter the ending interval:"))
for i in range(a,b):
    n=i
    s=0
    while(n>0):
        d=n%10
        n=int(n//10)
        s=s+(d*d*d)
        if(s==i):
            print(i)
        
