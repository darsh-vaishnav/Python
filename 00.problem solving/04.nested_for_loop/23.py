string=input("Enter the string: ")
for i in range(len(string)):
    for j in range(len(string)):
        if string[i]==string[j]:
            print("Same",end=" ")
        else:
            print("Different",end=" ")
    print()    