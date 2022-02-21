#1)Write a python program to find the longest word
f=open("text.txt","r")
for i in f.readlines():
	x = i.split()
	longest=x[0]
	for j in x:
		if len(j)>len(longest):
			longest=j
print(longest)
f.close()

#2)Write a Python program to count the frequency of words in a file.
f=open("text.txt","r")
frequency_dict={}
read=f.read()
words_list=read.split()
for i in words_list:
	frequency_dict[i]=words_list.count(i)
print(frequency_dict)
f.close()

#3) Write a Python program to read a random line from a file.
import random 
with open('text.txt') as file: 
    lines = file.readlines() 
    random_line = random.choice(lines) 
print(random_line)

#4)You have two list convert it in dictionary and add in (mydict.txt) and show result
f=open("mydict.txt","a")
def dictionary():
	first=["Ani","Jessy","Ben"]
	second=[1,2,3]
	my_dict={}
	for i in range(len(first)):
		my_dict[first[i]]=second[i]
	return my_dict
f.write(str(dictionary()))
f.close()


#5)Write a program that takes in a string as input, counts and outputs the number of vowels. And add result in json file.
import json
myString=input()
count=0 
vowels="aeiouAEIOU"
for i in myString:
	if i in vowels:
		count+=1
result=json.dumps(count)
print(result)

