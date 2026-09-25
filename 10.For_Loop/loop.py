# str=input("Enter a string:").strip().lower()
# str2=""
# length=len(str)
# for element in range(length-1,-1,-1):
#     str2=str2+str[element]
# if str==str2:
#     print(f"String 1 {str} and String 2 {str2} are Valid palindrom")
# else:
#     print(f"String 1 {str} and String 2 {str2} are Not an Valid palindrom")        

# #*****
# for i in range(4):
# #     for j in range(4):
# #         print("*", end="")
# # print("")    
# for row in range(1,6):
#     for column in range(1,row+1,):
#         print("*",end="")
#     print()

# # #
# # for i in range(1):
# #     for
# print("    *")
# print("   **")
# print("  ***")
# print(" ****")
# print("*****")
# num=int(input("Enter row value:"))
# for i in range(1,num):
#     for j in range(1,num-i,):
#         print("*",end="")
#     for k in range(1,i+1):
#         print(" ",end="")
#     print()   

# num=int(input("Enter row value:"))
# for i in range(1,num):
#     for j in range(1,num-i,):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()    

# print("*   *")
# print("*   *")
# print("*   *")
# print("*   *")
# print("*****")
# for i in range(1,6)
#   print("")

# n=int(input("Enter the Rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j==1 or j==n or i==n:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()   
            
n=int(input("Enter the Rows:"))
for i in range(1,n+1):
    for j in range(1,n+3):
        if j==1 or j==n or i==n:
            print("* ",end="")
        elif i==n:
            print("* ")    
        else:
            print(end=" ")
    print()  


   
