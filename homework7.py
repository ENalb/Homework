# dict_1 = {'key1': 1, 'key2': 3, 'key3': 2}
# dict2 = {'key1': 1, 'key2': 2}
# for i,j in dict_1.items():
# 	for x,y in dict2.items():
# 		if i==x and j==y:
# 			print(i,j,"is present in both dictionaries")

my_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
if my_dict.values() == None:
	k = my_dict.values()
my_dict.pop(k)
print(my_dict)
# for x,y in my_dict.items():
# 	if y == None:
# 		k = x
# my_dict.pop(k)
# print(my_dict)

# dict_1 = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# dict_1.update({"Math":[89,90,91],"Physics":[90,92,87]})
# print(dict_1)

# list1 = ["num1","num2","num3"]
# list2 = [1,2,3]
# my_dict = {}
# for i in range(len(list1)):
# 	my_dict[list1[i]] = list2[i]
# print(my_dict)


# n = int(input())
# my_dict = {}
# for i in range(1,n+1):
# 	my_dict[i]=i*i
# print(my_dict)


# maximum = max(my_dict.values())
# for x,y in my_dict.items():
# 	if y == maximum:
# 		print(x,y)
# 		k = x
# my_dict.pop(k)
# maximum2 = max(my_dict.values())
# for x,y in my_dict.items():
# 	if y == maximum2:
# 		print(x,y)
# 		m = x
# my_dict.pop(m)
# maximum3 = max(my_dict.values())
# for x,y in my_dict.items():
# 	if y == maximum3:
# 		print(x,y)
#print(my_dict)
# my_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# sorted_dictionary = sorted(my_dict.values())
# for x,y in my_dict.items():
# 	for i in range(-1,-4,-1):
# 		if y == sorted_dictionary[i]: 
# 			print(x,y)



		