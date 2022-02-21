def reverse_function(myString):
	return myString[::-1]
print(reverse_function("1234abcd"))

def my_function(myStr):
	for i in myStr:
		if i=="-":
			newStr = myStr.replace("-"," ")
	lst = newStr.split()
	sorted_list = sorted(lst)
	result = "-".join(sorted_list)
	return result
print(my_function("green-red-yellow-black-white"))

def float_number(number):
	txt = str(number)
	for i in txt:
		if i==".":
			print(txt[0:txt.index(i)+3])
float_number(19758.25693254)

import random
def guess_number():
	random_number = random.randint(1,10)
	i = 0 
	while True:
		num = int(input())
		if num > random_number:
			print("too high")
		elif num < random_number:
			print("too low")
		else:
			print("You win!")
			break
guess_number()

def divisors_of_number():
	number = int(input())
	for i in range(1,number+1):
		if number%i==0:
			print(i)
divisors_of_number()