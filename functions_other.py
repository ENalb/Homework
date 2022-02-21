#1)Ask the user for a number and determine whether the number is prime or not.
# def prime_function():
# 	number = int(input())
# 	k = True
# 	for i in range(2,number):
# 		if number%i==0:
# 			k = False
# 	if k:
# 		print("The number is  prime")
# 	else:
# 		print("The number is not prime")
# prime_function()

#2)Create a program that will play the “cows and bulls” game with the user.
computer_number=3768
user_input=input()
cow=0 
bull=0
if user_input==computer_number:
	print("You guessed right")
else:
	for i in str(user_input):
		for j in str(computer_number):
			if i==j:
				if str(user_input).index(i)!=str(computer_number).index(j):
					cow+=1
				else:
					bull+=1
print("cows:",cow,",bulls:",bull)

#3)Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
# def backwords(myString):
# 	list_string = myString.split()
# 	for i in list_string:
# 		x =" ".join(list_string[::-1]) 
# 		return x
# print(backwords("My name is Michele"))

#4)The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# import random
# def guess_function():
#     string1="too high"
#     string2="too low"
#     string3="You win"
#     TRY=0
#     guess=random.randint(0,100)
#     while True:
#     	print("Is the number",guess,"?")
#     	answer=input()
#     	TRY+=1
#     	if answer==string1:
#     		guess-=random.randint(1,10)
#     	elif answer==string2:
#     		guess+=random.randint(1,10)
#     	else:
# 	    	print("You guess number after",TRY,"tries")
# 	    	break
# print("Write your guessed number")
# guess_function()


#5)Write a Python program to check if it is possible to rearrange given string elements to get a palindrome
# def rearrange(myString):
# 	count={}
# 	for i in myString:
# 		count[i]=myString.count(i)
# 	odd_count=0
# 	for i in count.values():
# 		if i%2==1:
# 			odd_count+=1
# 		if odd_count>1:
# 			return False
# 	return True
# print(rearrange("raaecrc"))
# print(rearrange("raaecrck"))
# print(rearrange("1212"))
