n=int(input("Enter the number:"))

i=0
while i<n:
    j=0
    while j<n:
        print(j%2,end=" ")
        j+=1
    print()
    i+=1 