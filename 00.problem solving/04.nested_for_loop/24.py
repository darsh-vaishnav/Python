str1=input("Enter the string 1: ")
str2=input("Enter the string 2: ")
for i in str1:
    for j in str2:
        if i==j:
            print(f"{i} {j}")

str1=input("Enter the string 1: ")
str2=input("Enter the string 2: ")
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            print(f"{str1[i]} {str2[j]}")            