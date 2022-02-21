def my_function(str):
    str2=""
    for i in str:
        str2=i+str2
    return str2
str="1234abcd"
print(my_function(str))


input_str="green-red-yellow-black-white"
def myfunction(input_str):
    x=input_str.split('-')
    sorted_input=sorted(x)
    y='-'.join(i for i in sorted_input)
    return y
y=myfunction(input_str)
print(y)


def myfunction():
    number = 67.9843
    str_number=str(number)
    for i in str_number:
        if i=='.':
            print(str_number[0:str_number.index(i)+3])
myfunction()


import random
def my_function():
    x=random.randint(1,10)
    i=0
    while True:
        num=int(input())
        if num>x:
            print('too high')
        elif num<x:
            print('too low')
        elif num==x:
            print('you win')
            break
my_function()


def my_function():
    n=25
    for x in range(1,n+1):
        if n%x==0:
            print(x)
my_function()
