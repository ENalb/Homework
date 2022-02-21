# myTuple = (11, [22, 33], 44, 55)
# myTuple[1][0] = 222
# print("myTuple =",myTuple)

# myString = "python3.0"
# myTuple = tuple(myString)
# print(myTuple)

# tup = (17,36,45,17,"apple")
# if tup.count(tup[0]) == len(tup):
# 	print("All elements are same")
# else:
# 	print("All elements not same")
	


# my_set = {25,36,98,105,5}
# sorted_set = sorted(my_set)
# print("The min element in set is",sorted_set[0])
# print("The max element in set is",sorted_set[-1])
# minimum = maximum = 0
# for i in my_set:
# 	if i < minimum:
# 		minimum = i
# 
# for j in my_set:
# 	if j > maximum:
# 		maximum = j
# 


# set1 = {14,56,98,"banana","apple"}
# set2 = {95,36,14,"cherry"}
# if set1.isdisjoint(set2):
# 	print("Sets have no elements in common")
# else:
# 	print("Sets have common element")


# my_set = {25,36,98,105,5}
# for i in my_set:
# 	min_num = i
# 	max_num = i
# 	for j in my_set:
# 		if j < min_num:
# 			min_num = j
# 		elif j > max_num:
# 			max_num = j
# print(min_num,max_num)

my_set = {25,36,98,105,5}
minimum=my_set.pop()
maximum=my_set.pop()
for i in my_set:
	if i < minimum:
		minimum=i
print(minimum)
for i in my_set:
	if i>maximum:
		maximum=i
print(maximum)