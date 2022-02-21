# my_string = input()
# x = my_string.replace('r','$')
# print(x)

# text = input()
# x = text.replace(","," ")
# y = x.replace(".",",")
# z = y.replace(" ",".")
# print(z)

# txt = input()
# sum=0
# for i in txt:
# 	if i.isdigit():
# 		sum += int(i)
# print(sum)

# text = input()
# x = text.replace(" ","")
# print(x)

# string = input()
# x = string.split()
# for i in x:
# 	if len(i) % 2 == 0:
# 		print(i)

# word = input()
# count = 0
# for i in word:
# 	if i.isdigit():
# 		continue
# 	else:
# 		count += 1
# print(count)


# text = input()
# x = text.upper()
# y = text.lower()
# print(x,"\n",y)

# list = ['Geeks', 'for', 'Geeks']
# x = "-".join(list)
# print(x)

# list = ["hello", "this", "is", "pythonlobby"]
# x = " ".join(list)
# y = x.title()
# print(y)

# string = "hello world"
# count1,count2,count3,count4,count5,count6,count7 = 0,0,0,0,0,0,0
# for i in string:
# 	if i == "h":
# 		count1 += 1		
# 	if i == "e":
# 		count2 += 1		
# 	if i == "l":
# 		count3 += 1		
# 	if i == "o":
# 		count4 += 1		
# 	if i == "w":
# 		count5 += 1		
# 	if i == "r":
# 		count6 += 1
# 	if i == "d":
# 		count7 += 1
# print("h",count1)
# print("e",count2)
# print("l",count3)
# print("o",count4)
# print("w",count5)
# print("r",count6)
# print("d",count7)
# 		

string = "hello world"
for i in string:
	x = string.count(i)
	print(i,x)