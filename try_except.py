# try:
# 	print(x)

# except:
# 	print("An exception occurred")

# except Exception as e:
# 	print(e)

# except NameError:
# 	print("Variable x is not defined")
# except:
# 	print("Something else went wrong")

# except:
# 	print("Something went wrong")
# finally:
# 	print("The 'try except' is finished")

# try:
# 	f=open("125.txt","r")
# except:
# 	print("File is not defined")

# try:
# 	print(25/0)
# except:
# 	print("Zero division error")

# lst=[5,6,7]
# try:
# 	print(lst[7])
# except IndexError:
# 	print("index error")
# except:
# 	print("something went wrong")

password=input()
count1=0 
count2=0 
if len(password)<6 or len(password)>16:
	raise Exception("The length of password is not correct")
for i in password:
	if i.isupper():
		count1+=1
	elif i.isdigit():
		count2+=1
if count1<1:
	raise Exception("Your password must have upper case")
elif count2<1:
	raise Exception("Your password must have digit")
else:
	print("Your password is valid")