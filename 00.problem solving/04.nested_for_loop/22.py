s = input("Enter a string: ")

for i in range(len(s)):
    for j in range(len(s)):

        if s[i] == s[j]:
            print(f"{s[i]}/{s[j]} is Same")
        else:
            print(f"{s[i]}/{s[j]} is Different")