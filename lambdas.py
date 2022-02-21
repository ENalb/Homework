# my_function = lambda x: x+15
# my_function2 = lambda y: y*15
# print(my_function(5))
# print(my_function2(10))

# lst = [1,2,3,4,5,6]
# square_function=map(lambda x: x*x,lst)
# cube_function=map(lambda y: y**3,lst)
# print(list(square_function))
# print(list(cube_function))

# str=lambda x: True if x[0].istitle() else False
# print(str("Python"))

# my_list=[12,45,78,96,11,10,6,9]
# even_numbers=list(filter(lambda x: x%2==0,my_list))
# odd_numbers=list(filter(lambda y: y%2!=0,my_list))
# print(len(even_numbers))
# print(len(odd_numbers))

# lst1=[1,2,3,5,7,8,9,10]
# lst2=[1,2,4,8,9]
# intersection_function=list(filter(lambda x: x in lst1,lst2))
# print(intersection_function)

# lst1=[1,2,3]
# lst2=[4,5,6]
# add_func=list(map(lambda x,y: x+y, lst1, lst2))
# print(add_func)

# lst=[2,4,-6,-9,11,-12,14,-5,17]
# negative_numbers=list(filter(lambda x: x<0,lst))
# positive_numbers=list(filter(lambda y: y>0,lst))
# print(sum(negative_numbers))
# print(sum(positive_numbers))

lst = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
for x in lst:
	sorted_list=lambda x: sorted(x[0])
print(sorted_list(lst))