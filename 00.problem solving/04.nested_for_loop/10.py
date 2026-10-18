n=int(input("Enter the number:"))

i=0
while i<n:
    j=0
    while j<n:
        print(j%2,end=" ")
        j+=1
    print()
    i+=1 

# for

n = int(input("Enter the number:"))
for i in range (1,1+n):
    for j in range(1,1+n):
        