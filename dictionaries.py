# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# dict4={}
# for i in dict1,dict2,dict3:
# 	dict4.update(i)
# print(dict4)


# my_dict={"speed":250,"speed2":200,"speed3":140}
# for x in my_dict.values():
# 	if x==200:
# 		print("Yes")

# my_dict={"emp1":{"name":"John","salary":7500},"emp2":{"name":"Brad","salary":6500}}
# for x in my_dict.keys():
# 	if x=="emp2":
# 		my_dict[x]["salary"]=8500
# print(my_dict)

lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
S1 = 0
S2 = 0
for i in lst:
	for j in i.values():
		if j=="item1":
			S1 += i["amount"]
		elif j == "item2":
			S2 += i["amount"]
print("item1:",S1)
print("item2:",S2)
