# i = 1
# while i <= 7:
# 	print(7*i)
# 	i += 1

# for i in range(1,8,1):
# 	print(7*i)

# my_list = [12,75,150,180,145,525,50]
# for i in my_list:
# 	if i == 150:
# 		continue
# 	elif i >= 500:
# 		break
# 	elif i%5 == 0:
# 		print(i)

# i = 1
# while i <= 10:
# 	print(i)
# 	i += 1

# number = 73421
# sum = 0
# for i in str(number):
# 	sum += int(i)
# print(sum)

# sum = 0
# list = [73421]
# for i in list:
# 	sum += i
# print(sum)

# for i in range(1,50):
# 	if i%7 == 0:
# 		print(i)

# number = int(input)
# sum = 0
# for i in number:
# 	if i < 0:
# 		break
# 	else:
# 		sum += i
# print(sum)

# sum = 0
# while True:
#     number = int(input())
#     if x < 0:
#         break
#     sum += x
# print(sum)

# count = 0
# my_string = "Python is awesome!."
# for i in my_string:
# 	if i == ' ':
# 		continue
# 	count += 1
# print(count)

number1 = int(input())
number2 = int(input())
i = 2
while i < 100:
	if number1%i == 0 and number2%i == 0:
		print(i)
		break
	i += 1
		