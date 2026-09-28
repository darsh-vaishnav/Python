text = input("Enter a string: ")
uppercase_count = 0
index = 0
while index < len(text):
    character = text[index]
    if character >= "A" and character <= "Z":
        uppercase_count += 1
    index += 1
print("Number of uppercase letters:", uppercase_count)