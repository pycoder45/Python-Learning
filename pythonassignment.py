# Assignment No.2

#Algorithm
 
'''
1.Start
2.Create A Variable 'usr_input' to take input
3.Create A Variable 'input_list'
4.Use function split() to make list of input numbers, and store that list in 'input_list' variable.
5. Create a 'num_list' variable to store integer type number list.
5.Use For Loop to convert each item in 'input_list' in 'int' data type
6. create 'max' variable and use max() function on 'num_list'
7. create 'min' variable and use min() function on 'num_list'
8. create 'sum' variable and use sum() function on 'num_list'
9. create 'avg' variable and use sum/(num_list) to find average
10. Print All Values
11.End
'''

#Program

usr_input = input('Enter Numbers Seperated by Comma:- ')
input_list = usr_input.split(',')
num_list = []

for i in input_list:
	num_list.append(int(i))
	
max = max(num_list)
min = min(num_list)
sum = sum(num_list)
avg = sum/len(num_list)

print(f"\n* Maximum Number: {max}\n* Minimum Number: {min}\n* Sum Of Number: {sum}\n* Average Of Numbers: {avg}")


# Assignment No.3

#Algoritham 
'''
1.Start
2.create a function add() accepting 2 argument and return the summation of this numbers
3.create a function sub() accepting 2 argument and return the substraction of this numbers
4.create a function mult() accepting 2 argument and return the multiplication of this numbers
5.create a function div() accepting 2 argument and return the Division of this numbers
6. Use the if conditions
  if ipt=='A':
	sum(Num1,Num2). Summation of NUMBERS
  if ipt=='S':
	sub(Num1,Num2)  substraction of number
  if ipt=='M':
	mult(Num1,Num2) multiplication of number
  if ipt=='D':
  div(Num1,Num2). Division of number
  else:
	('Enter The Command Correctly')
7.End
'''

print('\n•Use The Following Commands ')
print('''
* Addition : A
* Substraction : S
* Multiplication : M
* Division :D
''')

def sum(a,b):
	print('Summation: ', a+b)
def sub(a,b):
	print('Substraction: ', a-b)
def mult(a,b):
	print('Multiplication: ',a*b)
def div(a,b):
	print('Division: ', a/b)

ipt = input('~ ')
Num1 = int(input ('Enter The Number 1: '))
Num2 = int(input('Enter The Number 2: '))

if ipt=='A':
	sum(Num1,Num2)
if ipt=='S':
	sub(Num1,Num2)
if ipt=='M':
	mult(Num1,Num2)
if ipt=='D':
  div(Num1,Num2)
else:
	print('Enter The Command Correctly')

#Assignment No.4

#Algoritham
'''
1.Start
2.Create variable "str_ipt" to accept the numbers from users in string format Seperated by commma
3.Create Variable "str_lst" and store value of str_ipt.split(",") in it.
4.Create a variable "int_lst" with empty list.
5.Create a for loop to convert numbers in "int" data type.
6. Create a "odd" and "even" variables with empty list.
7.Use for loop and if else loop,
  for i in int_lst :
    if i%2== 0: 
      even.append(i)
    else : 
      odd.append(i)
8.Print odd even values
9.End
''' 

#Program
str_ipt = input("Enter The Numbers Seperated by comma ")
str_lst = str_ipt.split(",")
int_lst =[]
for i in str_lst: 
  int_lst.append(int(i))

odd =[]
even = []

for i in int_lst: 
  if i%2== 0: 
    even.append(i)
  else: 
    odd.append(i)
  
print(f"Odd Numbers : {odd}")
print(f"Even Numbers : {even}")