# Chapter 2
# Variables, Data Types And Operators 

# 🎯 1.VARIABLES 
# They are container Store the perticular values

a = "Aditya"    # String
b = 264         # Integer
c = 45.93       # Float (with points)
d = True        # Boolean
e = None        # None/ Nothing In Python

# These are the 5 type of value we can store in variable

# Rules For Naming Of Variables :
# 1) Name Can Contain Only (A-Z)/(a-z)/(_)/(0-9)
# 2) Name Must start with (A-Z)/(a-z)/(_)
# 3) It do not start with (0-9)/Any special char.
# 4) White-Spaces are not allowed in naming
# IF YOUR BREAK THE RULES GIVE A SYNTAX ERROR

# 🎯 2.DATA TYPES 
# Finding The Data Type Of Variables

print(type(a))         #str
print(type(b))         #int
print(type(c))         #float
print(type(d))         #bool
print(type(e))         #NoneType

# * Variable :- Container To Store Value
# * Keywords :- Reserved Words In Python 
# * Identifiers :- Class/Function/Variable Names 
# * Variable Name Are Case Sensitive 
# * Valid Variable Names :- "Harry","hello","a45","_Name"

# 🎯 3. Operators 

# 01.Logical Operators : +,-,*,/,**,//,%
num1 = 5
num2 = 6

print("Sum Of Num1 &  Num2 : ",num1 + num2)
print("Sub Of Num1 &  Num2 : ",num1 - num2)
print("Pro Of Num1 &  Num2 : ",num1 * num2)
print("Div Of Num1 &  Num2 : ",num1 / num2)
print("Power Of Num1 with Num2 : ",num1 ** num2)
print("Float Div Of Num1 &  Num2 : ",num1 // num2)
print("Remainder Of Num1 &  Num2 in Divsion : ",num1 % num2)

# 02.Assignment Operator's 

num1 += 2
num2 -= 3
print("New num1 : ", num1)
print("New num2 : ", num2)

num3 = 10
num3 *= 2
print("Product of num3 : ", num3)

# Similarly You Can Use %,/,//,** operator's

# 03.Caparison Operator's 
x = 12==13
y = 12!=13
z = 12>13
xy = 12<13
yz = 12>=13
xz = 12<=13

print(x,x,z,xy,yz,xz)

# 04.Logical Operator's 

var_tr = True 
var_fl = False

print("Using and: ",(var_fl and var_tr))
print("Using or: ",(var_fl or var_tr))
print("Using not: ",(not var_tr))

# 🎯 4. Type Casting 

# Following Are used to convert Type Of Literal

str_1 = "String"
str_2 = "3484"
int_1 = 3583
flt_1 = 34.75

print(int(str_2))
print(int(flt_1))
print(float(int_1))
print(str(int_1))    
# print(int(str_1))    #*

# print(type(int_1))
# As Wr haven't changed the main value we have just printed using float,str,int. We didn't misbehave with original values.
# For * "case invalid literal for int()" error comes as we cant convert string to integers or float. 

# 🎯 5. Input 

_input_ = input("Enter A Number: ")
print(_input_,type(_input_))

# For The Input It always makes the string of any literals(int,float,str), means any value coming from input is always and always STRING 