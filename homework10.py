#1.Use the sorted() function to sort the list in ascending order with lambda.
lst = [12,65,7,45,106,64]
sorted_list = sorted(lst,key=lambda x:x)
print(sorted_list)

#2.Write a Python program to sort each sublist of strings in a given list of lists using lambda.
lst = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
sorted_list = [sorted(x, key=lambda x: x[0]) for x in lst]
print(sorted_list)

#3.Write a Python program to count float number in a given mixed list using lambda.
lst = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
float_numbers = list(filter(lambda x: type(x)==float,lst))
print(len(float_numbers))

#4.Write a Python program to count the occurrences of the items in a given list using lambda.
lst = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
occurence = dict(map(lambda x:(x,lst.count(x)),lst))
print(occurence)

#5.Write a Python program to remove None value from a given list using lambda function. 
lst = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
removed_list = list(filter(lambda x: x is not None,lst))
print(removed_list)

#6.Write a Python program to find palindromes in a given list of strings using Lambda.
lst = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindromes_list = list(filter(lambda x: x[0::]==x[-1::-1],lst))
print(palindromes_list)