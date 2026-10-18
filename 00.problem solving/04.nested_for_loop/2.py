# Que 2
n=int(input("Enter the number:"))
i=1
while i<=n:
    j=1
    while j<=n:
        print(f"{i} x {j} = {i*j}")
        j+=1
    i +=1    

# for 
n=int(input("Enter the number:"))
for i in range (1,1+n):
    for j in range (1,1+n):
        print(f"{i} x {j} = {i*j}")
        