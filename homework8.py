# myString = "Hello Armenia"
# print(len(myString))

# lst = [-5,16,48,76,-6]
# s = 0
# for i in lst:
# 	s += i
# print("The sum of list items:",s)

# lst = [2,6,-4,14,-5]
# p = 1
# for i in lst:
# 	p *= i
# print(p)

# myList = [96,104,-9,200,-4]
# maximum = myList[0]
# for i in myList:
# 	if i > maximum:
# 		maximum = i
# print("The maximum number in list is",maximum)

# myList = [45,369,14,23,-9,12]
# minimum = myList[0]
# for i in myList:
# 	if i < minimum:
# 		minimum = i 
# print("The minimum number in list is",minimum)

# string1 = "Welcome to Yerevan"
# for i in string1:
# 	if i.isspace():
# 		continue
# 	print(i,string1.count(i))

# myString = "google.com"
# myDict = {}
# for i in myString:
# 	myDict[i] = myString.count(i)
# print(myDict)

# lst = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for i in lst:
# 	if len(i) >= 2 and i[0] == i[-1]:
# 		count += 1
# print(count)

lst = [(2,5),(1,2),(4,4),(2,3),(2,1)]
minimum1 = lst[0]
minimum2 = lst[0]
minimum3 = lst[0]
minimum4 = lst[0]
sorted_list = []
for i in lst:
	if i[1]<minimum1[1]:
		minimum1=i
lst.remove(minimum1)
for i in lst:
	if i[1]<minimum2[1]:
		minimum2=i
lst.remove(minimum2)
for i in lst:
	if i[1]<minimum3[1]:
		minimum3=i 
lst.remove(minimum3)
for i in lst:
	if i[1]<minimum4[1]:
		minimum4=i
lst.remove(minimum4)
for i in lst:
	last = i
sorted_list.append(minimum1)
sorted_list.append(minimum2)
sorted_list.append(minimum3)
sorted_list.append(minimum4)
sorted_list.append(last)
print(sorted_list)

# sorted_list = sorted(lst, key = lambda y: y[1])
# print(sorted_list)

# myString = input()
# if len(myString) < 2:
# 	print("Empty string")
# else:
# 	print(myString[0:2]+myString[-2:])

# myString = 'restart'
# replaced_string = myString.replace(myString[0],"$")
# result = myString[0]+replaced_string[1::]
# print(result)

# str1 = 'abc' 
# str2 = 'xyz'
# myString = str1+" "+str2
# replaced_string1 = myString.replace(myString[0:2:1],".")
# replaced_string2 = replaced_string1.replace(myString[-3:-1:1],myString[0:2:1])
# replaced_string = replaced_string2.replace(".",myString[-3:-1:1])
# print(replaced_string)

# myString = "string"
# if myString[-3::1]!="ing":
# 	myString += "ing"
# else:
# 	myString += "ly"
# print(myString)

# myString =  'The lyrics is not that poor!'
# x = myString.find("not")
# y = myString.find("poor")
# if y > x:
# 	myString = myString.replace(myString[x:-1],"good")
# print(myString)


# list_of_words = ["apple","orange","banana","pineapple"]
# longest = list_of_words[0]
# for i in list_of_words:
# 	if len(i) > len(longest):
# 		longest = i 
# print("The longest word is",longest)

# input_1 = int(input())
# if type(input_1)==int:
# 	print("input is integer")
# else:
# 	print("input is not integer")

# dict1 = {9:45,10:12,14:36,47:89,25:100}
# for i in sorted(dict1.values()):
# 	for x,y in dict1.items():
# 		if y == i:
# 			print(x,i)
# print("\n")
# for j in sorted(dict1.values(),reverse=True):
# 	for x,y in dict1.items():
# 		if y == j:
# 			print(x,j)

# dict1 = {5:50,14:56,1:47,3:15,2:69}
# for i in sorted(dict1.keys()):
# 	print(i,dict1[i])
# print("\n")
# for j in sorted(dict1.keys(),reverse=True):
# 	print(j,dict1[j])

# myDict = {0: 10, 1: 20}
# myDict[2] = 30
# print(myDict)

# dic1 = {1:10,2:20}
# dic2 = {3:30,4:40}
# dic3 = {5:50,6:60}
# dic4 = {7:70,8:80}
# dic5 = {9:90,10:100}
# dic = {}
# for x in (dic1,dic2,dic3,dic4,dic5):
# 	dic.update(x)
# print(dic)


# myDict = {"name":"Emi","surname":"Nalbandyan","age":20,"country":"Armenia"}
# key = "age"
# k = False
# for x in myDict.keys():
# 	if x == key:
# 		k = True
# if(k):
# 	print("Given key is exists in a dictionary")
# else:
# 	print("Given key is not exists in a dictionary")

# myDict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
# for x,y in myDict.items():
# 	print(x,y)

# list1 = [14,56,32,47,14,56,98,105]
# list2 = []
# for i in list1:
# 	if i not in list2:
# 		list2.append(i)
# print(list2)

# lst = [12,13,16]
# if bool(lst) == True:
# 	print("List is not empty")
# else:
# 	print("List is empty")

# lst = [1,6,7,"apple","banana",14]
# copy_list = lst.copy()
# print(copy_list)

# str1 = "Welcome"
# n = int(input())
# for i in range(len(str1)):
# 	if i == n:
# 		continue
# 	print(str1[i])

# str1 = "Yerevan"
# str2 = str1.replace(str1[0]," ")
# str3 = str2.replace(str2[-1],str1[0])
# str4 = str3.replace(" ",str2[-1])
# print(str4)
	 
# myString = "mysterious"
# for i in range(len(myString)):
# 	if i%2!=0:
# 		continue
# 	print(myString[i])

# n = int(input())
# myString = "The most beautiful things in the world cannot be seen or touched, they are felt with the heart."
# string_list = myString.split()
# lst = []
# for i in string_list:
# 	if len(i) > n:
# 		lst.append(i)
# print(lst)


# myString = "It is the time you have wasted for your rose that makes your rose so important."
# string_list = myString.split()
# for i in string_list:
# 	print(i,string_list.count(i))


# list1 = [1,2,3,4,5,6,7,8]
# list2 = [5,6,7,14,36,25,9]
# k = False
# for i in list1:
# 	for j in list2:
# 		if i == j:
# 			k = True
# print(k)  