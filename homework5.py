# lst = [1,2,6,7,6,4,2]
# # for i in lst:
# #     if lst.count(i)>1:
# #         print(i)
# #         x=lst.index(i)
# #         y = lst.pop(x)
# #         print(y)
# lst.sort()
# print(lst)
# for i in lst:
#     if i == i+1:
#         continue
# print(lst)
 
# t = ['a', 'b', 'c', 'd']
# t2 = ['a', 'c', 'd']
# for t in t2:
#     x=t.append(t.remove())
# print(x)
 
# my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
# print("List Before ", my_list)
# temp_list = []
 
# for i in my_list:
#     if i not in temp_list:
#         temp_list.append(i)
 
# my_list = temp_list
 
# print("List After removing duplicates ", my_list)
 
# lst = ["apple","banana",1,6,[14,56],"pink"]
# x=lst.copy()
# print(x)
 
# myList = [1,"Hayastan",14,36,"Yerevan"]
# print(myList[0:3])
 
# list_of_strings = ["apple","cherry","kiwi","","banana",""]
# for i in list_of_strings:
#     if i == "":
#         list_of_strings.remove(i)
# print(list_of_strings)
    
#         list_of_strings.pop(i)
# #list_of_strings.remove("")
# print(list_of_strings)
 
# numbers = [15,47,64,25,47,36]
# x = sorted(numbers,reverse=True)
# print(x[-2])
 
# lst1 = [1,2,3,4,5,6,7,8,9]
# lst2 = [1,2,3,4]
# lst3 = []
# for i in lst1:
#     if i in lst2:
#         continue
#     else:
#         lst3.append(i)
# print(lst3)
 
# lst = ['Red','Green','White','Black','Pink','Yellow']
# lst.pop(5)
# lst.pop(4)
# lst.pop(0)
# print(lst)
 
# lst1 = [12,34,25,69,"apple"]
# lst2 = [14,105,12,"banana"]
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             print("True")

# lst = [5,6,7,12,4,3,5,6]
# lst1 = []
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)

string1="hello"
string2="world"
print(string1-string2)
 