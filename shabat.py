# myList=[0,14,69,47,-5,4,7]
# minimum=myList[0]
# maximum=myList[0]
# for i in myList:
# 	if i<minimum:
# 		minimum=i
# print("The min element in list is",minimum)
# for j in myList:
# 	if j>maximum:
# 		maximum=j
# print("The max element in list is",maximum)


# import random
# x=random.randint(1,10)
# i=1
# while True:
# 	number=int(input())
# 	if number==x:
# 		print("You win")
# 		break
# 	elif number<x:
# 		print("Go higher")
# 	elif number>x:
# 		print("Go lower")
# 	i+=1

# myString=input()
# if myString[0::]==myString[-1::-1]:
# 	print("The myString is palindrom")
# else:
# 	print("The myString is not palindrom")

# myString=input()
# myList=myString.split()
# x=" ".join(myList[::-1])
# print(x)


# for i in range(0,6):
# 	for j in range(i):
# 		print("*",end=" ")
# 	print(" ")

# for i in range(0,6):
# 	for j in range(i):
# 		print("*",end=" ")
# 	print(" ")
# for i in range(6,0,-1):
# 	for j in range(i):
# 		print("*",end=" ")
# 	print(" ")

# password=input()
# if len(password)<6: #and len(password)<=17 and password[j].isupper() and password[j].isnumeric() and password[j].isalnum():
# 	print("The password is short")
# elif len(password)>17:
# 	print("The password is long")
# elif password.isalnum():
# 	for i in password:
# 		if password[i].isupper():
# 			print("The password is right")
# 		else:
# 			print("Try again")

# l, u, ch, d = 0, 0, 0, 0
# password = input()
# characters = ["[","{","}","(",")",".",":",";","+","-","*","/","&","|","<",">","=","~","]"]
# if (len(password) >= 6 and len(password) <= 16):
#     for i in password:
#         if i.islower():
#             l += 1            
#         if i.isupper():
#             u += 1            
#         if i.isdigit():
#             d += 1 
#         for j in characters:
#         	if(i == j):
#         		ch += 1           
# if (l >= 1 and u >= 1 and ch >= 1 and d >= 1): 
#     print("Valid Password")
# else:
#     print("Invalid Password")

import random
player = random.choice(["rock","paper","scissor"])
my_choice = input()
print(player)
if player == my_choice:
	print("No one")
elif my_choice == "rock" and player == "paper" or my_choice == "paper" and player == "rock":
	print("Paper wins")
elif my_choice == "rock" and player == "scissor" or my_choice == "scissor" and player == "rock":
	print("Rock wins")
else:
	print("scissor wins")
