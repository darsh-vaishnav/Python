rows=int(input("Enter the rows: "))
i=0
while i<rows :
    j=1
    while j<=rows:
        print(j,end=" ")
        j=j+2
    print()
    i=i+1 

# for
rows=int(input("Enter the rows: "))   
for i in range(rows):
    for j in range(1,rows+1,2):
        print(j,end=" ")
    print()