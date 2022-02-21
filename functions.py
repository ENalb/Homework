# def my_function():
# 	lst = [12,48,97]
# 	s = 0
# 	for i in lst:
# 		s += i
# 	return s 
# print(my_function())

# def my_function(lst):
# 	s = 0
# 	for i in lst:
# 		s += i 
# 	return s
# print(my_function([36,47,10]))

# def my_function(a,b,num):
# 	if num>=a and num<=b:
# 		print("num is in given range")
# 	else:
# 		print("num is not in given range")
# my_function(10,30,25)	


# def my_function(myString):
# 	count1 = 0
# 	count2 = 0
# 	for i in myString:
# 		if i.isupper():
# 			count1 += 1
# 		elif i.islower():
# 			count2 += 1
# 	print("The count of upper cases in string is",count1)
# 	print("The count of lower cases in string is",count2)
# my_function("I love My Country")

# def my_function(lst):
# 	lst2 = []
# 	for i in lst:
# 		if i not in lst2:
# 			lst2.append(i)
# 	return lst2
# print(my_function([1,23,1,1,4,7,7,4,69]))


# def my_function(lst):
# 	for i in lst:
# 		if i%2==0:
# 			print(i)
# my_function([9,8,7,2,4])

# def my_function(myString):
# 	for i in myString:
# 		if i.isalnum():
# 			continue
# 		else:
# 			print(i,myString.index(i))
# my_function("Armenia#2022%97*69")


def my_function(lst):
	maximum1 = lst[0]
	maximum2 = lst[0]
	for i in lst:
		if i > maximum1:
			maximum1 = i 
	for i in lst:
		if i > maximum2 and i < maximum1:
			maximum2 = i 
	return maximum2
print(my_function([14,105,36,47,98]))