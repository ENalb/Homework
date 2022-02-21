# l=[1,2,3]
# def my_function(lst):
# 	return sorted(lst)[-1]
# print(my_function(l))

# import random
# def my_function():
# 	guessed_number=random.randint(0,15)
# 	string1="too low"
# 	string2="too high"
# 	string3="you win"
# 	count=0 
# 	while True:
# 		print(guessed_number)
# 		answer=input()
# 		count+=1
# 		if answer==string1:
# 			guessed_number+=random.randint(1,3)
# 		elif answer==string2:
# 			guessed_number-=random.randint(1,3)
# 		else:
# 			print("You guess number after",count,"tries")
# 			break
# my_function()

#print(int(7.0)==int("7.0"))

# a=[1,2,3,4,5,6]
# x=a[::-2]
# y=a[::2]
# print(sorted(x+y)==a)

# def func():
# 	x=10
# 	return func()
# print(func())

# from sys import getrecursionlimit
# print(getrecursionlimit())

# from sys import setrecursionlimit
# print(setrecursionlimit(200))


# def countdown(n):
# 	print(n)
# 	if n==0:
# 		return 
# 	else:
# 		countdown(n-1)
# countdown(5)

# def countdown(n):
# 	while n>=0:
# 		print(n)
# 		n-=1
# countdown(5)

# def factorial_recursive(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return n*factorial_recursive(n-1)
# print(factorial_recursive(5))

# def sum_recursive(current_number,accumulated_sum):
# 	if current_number==11:
# 		return accumulated_sum
# 	else:
# 		return sum_recursive(current_number+1,accumulated_sum+current_number)
# print(sum_recursive(8,10))

# def fibonacci(n):
# 	if n<0:
# 		print("Incorrect input")
# 	elif n==0:
# 		return 0
# 	elif n==1 or n==2:
# 		return 1
# 	else:
# 		return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(9))

# def sum_of_numbers(lst):
# 	if len(lst)==0:
# 		return 0 
# 	else:
# 		return lst[0]+sum_of_numbers(lst[1:])
# print(sum_of_numbers([1,6,9,4]))

def list_sum(lst):
	s=0
	for i in lst:
		if type(i)==list:
			s += list_sum(i)
		else:
			s += i
	return s
print(list_sum([1,2,[3,4],[5,6]]))