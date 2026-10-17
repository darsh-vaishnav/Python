rows=int(input("Enter the rows:"))
columns=int(input("Enter the columns:"))

i=1
while i<=rows:
    j=1
    while j<=columns:
        print("*",end=" ")
        j+=1
    print()
    i+=1 