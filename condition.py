# a=10
# b=20
# c=30
# print(a<b and c>a)
# print(a<b or b>c)
# print(not(a<b))


# a=10
# b=10
# print(a is not b)

# a=[1,2,3]
# if 1 in a:
# 	print("yes")

# a=10
# b=20
# if b>a:
# 	print("b is greater than a")

# a=30
# b=38
# if a==b:
# 	print("a is equal b")
# elif a!= b:
# 	print("a is not equal b")


# my_str="hello"
# if '!' in my_str:
# 	print("True")

# a=200
# b=30
# if a>b:
# 	print("a is greater than b")
# elif a<b:
# 	print("b is greater")
# else:
# 	print("a is equal b")

# x=41
# if x>10:
# 	print("Above ten")
# 	if x>20:
# 		print("and also above 20")
# 	else:
# 		print("but not above 20")

# num1=10
# num2=20
# num3=30
# #if num1 is num2:
# 	#print("num1 is num2")
# #else:
# 	#print("num1 is not num2")

# if num2<num1:
# 	print("do something")
# else:
# 	if num3>num2:
# 		print("ok")

# a=int(input())
# b=int(input())
# if a==b:
# 	print("a is equal b")
# elif a>b:
# 	print("a is greater than b")
# else:
# 	print("b is greater than a")

# num=int(input())
# if num%5==0 and num%7==0:
# 	print("fizzbizz")
# elif num%5==0:
# 	print("fizz")
# elif num%7==0:
# 	print("bizz")

# str=input()
# if len(str)>20:
# 	print("too long word")
# elif len(str)<10:
# 	print("short word")
# elif len(str)>10:
# 	print("long word")



# for x in "banana":
# 	print(x)

# fruits=["apple","banana","cherry"]
# fruits=("apple","banana","cherry")
# for x in fruits:
# 	print(x)

# string=input()
# i=0
# for x in string:
#     if x == 'a':
# 	    i+=1
# print(i)

# list=[1,2,3,4,5]
# sum=0
# for x in list:
# 	sum+=x
# print(sum)

# string1=input()
# string2=input()
# string3=input()
# if len(string1)>len(string2) and len(string1)>len(string3):
# 	print("The long word is",string1)
# elif len(string2)>len(string1) and len(string2)>len(string3):
# 	print("The long word is", string2)
# else:
# 	print("The long word is", string3)

# my_str = input()
# if 'a' in my_str or 'b' in my_str:
# 	print("True")
# else:
# 	print("False")

# word = input()
# for x in word:
# 	print(x)

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
if num_1 >= num_2 and num_1 >= num_3:
	largest = num_1
elif num_2 >= num_1 and num_2 >= num_3:
	largest = num_2
else:
	largest = num_3
print("the largest number is",largest)
