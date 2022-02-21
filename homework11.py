#1)Write a Python program of recursion list sum.
def list_sum(lst):
	s=0
	for i in lst:
		if type(i)==list:
			s += list_sum(i)
		else:
			s += i
	return s
print(list_sum([1,2,[3,4],[5,6]]))

#2)Write a Python program to solve the Fibonacci sequence using recursion.
def Fibonacci_sequence(num):
	if num<=1: 
		return num
	else:
		return Fibonacci_sequence(num-1)+Fibonacci_sequence(num-2)
print("Input number:")
number = int(input())
print("Fibonacci sequence:")
for i in range(number):
	print(Fibonacci_sequence(i))


#3)Write a Python program to find  the greatest common divisor (gcd) of two integers.
def greatest_common_divisor(x,y):
	if y==0:
		return x 
	else:
		return greatest_common_divisor(y,x%y)
print(greatest_common_divisor(49,14))

