# total=0
# flag=True
# grade="F"

# if i in range(5):
#     marks=int(input("Enter the marks:"))
#     total+=marks
#     if marks<35:
#         flag=False
# if flag:
#     percentage=total/5
#     if percentage>=90:
#         print("A+")
#     elif percentage>=80:
#         print("A")
#     elif percentage>=70:
#         print("B")
#     elif percentage>=60:
#         print("C")
#     elif percentage>=50:
#         print("D")
#     else:
#         print("F")
# else:
#     print("F")

# print("total")
# print("percentage")
# print("grade")

# if passed:
#     print("Passed")
# else:
#     print("Failed")    
# marks = []
# total = 0
# passed = True

# for i in range(1, 6):
#     mark = float(input(f"Enter marks for subject {i}: "))
#     marks.append(mark)
#     total += mark

# percentage = total / 5

# for mark in marks:
#     if mark < 35:
#         passed = False
#         break

# if passed:
#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 80:
#         grade = "A"
#     elif percentage >= 70:
#         grade = "B"
#     elif percentage >= 60:
#         grade = "C"
#     elif percentage >= 50:
#         grade = "D"
#     else:
#         grade = "F"
# else:
#     grade = "F"

# print("Total Marks:", total)
# print("Percentage:", percentage, "%")
# print("Grade:", grade)

# if passed:
#     print("Final Result: PASS")
# else:
#     print("Final Result: FAIL")
                               
total = 0
passed = True

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    total +=mark

    if mark < 35:
        passed = False

percentage = total / 5

if passed:
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
else:
    grade = "F"

print("Total:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)

if passed:
    print("Final Result: PASS")
else:
    print("Final Result: FAIL")