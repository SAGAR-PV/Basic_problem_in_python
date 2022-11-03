n=int(input("enter the number"))
i=1
j=0
while(i<=n):
    while(j<=i-1):
        print("*",end=" ")
        j=j+1
    print("\r")
    j=0 
    i=i+1    

