#1)
l=[("Apple","7","orange"),("Cherry","banana",45),("3","9","Pinapple")]
l.sort(key=lambda x:x[1])
print(l)

#2)
def sortsublist(input):
    result=[sorted(x,key=lambda x:x[0]) for x in input]
    return result
color=(["green","orange"],["black","white"],["white","black","orange"])
print(sortsublist(color))

#3)
def count_float(lst):
    y=list(filter(lambda x:isinstance(x,float),lst))
    result=len([i for i in y if i])
    return(result)
lst=[1,'abcd',3.12,1.2,4,'xyz',5,'pqr',7,-5,-12.22]
print(count_float(lst))

#4)
mylist=[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
occurence=dict(map(lambda x:(x,mylist.count(x)),mylist))
print(occurence)

#5)
original_list=[12,0,None,23,None,-55,234,89,None,0,6,-12]
removed_list=list(filter(lambda x:x is not None,original_list))
print(removed_list)

#6)
original_list=['php','w3r','Python','abcd','Java','aaa']
palindrome_list=list(filter(lambda x:x[0::]==x[-1::-1],original_list))
print(palindrome_list)
