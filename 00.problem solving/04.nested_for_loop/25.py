str1=input("Enter the string 1: ")
str2=input("Enter the string 2: ")

total=0

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
           total +=1
print(total)           