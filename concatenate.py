# l = [1,2,3]
# k = [i for i in l]
# print(k)

# d = {1:1,2:2,3:3}
# k = {key:value for key,value in d.items()}
# print(k)

# key_list = ["name","surname","age"]
# value_list = ["Emi","Nalbandyan",20]
# my_dict = {key_list[i]:value_list[i] for i in range(len(key_list))}
# print(my_dict)

list1 = [1,2,3,4]
dict1= {}
for i in list1:
	dict1[i] = i*i
print(dict1)