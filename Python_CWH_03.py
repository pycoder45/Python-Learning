# Chapter 3 
# Strings 
# 🎯 01.Strings 

# The Strings are the literals to store the words and (numbers)
# We Can Write The String In The Three Ways

# print('Hello World')
# print("Hello World")
# print('''Hello World''')

# All Of these Will Print.....
# Single and Double Quotation Marks are work only for single line.
# The Triple Quotation Marks are used to printing new lines and also include "" and '' in the string.
# You Can also use [\'] or [\"] to enter a quotation mark in string.

# print(''' Hello Brother's, I"ll back soon !''')
# print("Hello Brother's ")
# print('Hello Brother"s')

# Using This We have printed the Single And Double Quotes which is not possible in above two (-Possible If Different Quotation Marks Are Used-)
# Use can use \n,\t,\',\\ for newline,tab,',\

# SOME_MORE_EXAMPLES

# Ex.1 : Concatenation 
str_1 = "Good Morning "
str_2 = "Aditya"
str_12 = str_1 + str_2    #Concate Of String
print(str_12)

# Ex.2 : Indexing Of String
str_3 = "Rohit Sharma"
# print(str_3[0],end="")
# print(str_3[4])
# print(str_3[1])

# Remember: Indexing Always Start From A Zero
# It just Access the value from string, not set OR apply new string. 
# str_3[4] = "P"     --We Cannot Give The Value to It, it just give the value of perticular index.
# [end=""] is fuction which makes the print statement in the way that i doesn't take a full line, it just take the space that needed, So the next 'print' will also printed on a same line,Means if you wanted to next 'print' line on curent 'print' line then [end=""] us used.

# Ex.3 : Splicing Of String
name = "Aditya Vaste"

#Syntax:

#▪︎slice(stop)
#▪︎slice(start, stop, step)

#•Parameters:
#•start: Starting index where the slicing of object starts.
#•stop: Ending index where the slicing of object stops.
#•step: It is an optional argument that determines the increment between each index for slicing.

print(name[0:5]) 
#1st Number include last exclude

print(name[1:9])

print(name[2:300])
# It will print string from 2 to 300 if less than 300 character are present then it will print whole string 

print(name[0:0])
# Nothing will print...It will print empty no spaces or words

print(name[:])
# It will print whole string, because if you didn't give him value it will take automatically 1st or last value.
# It is equal to name[0:13]  <--Whole String

print(name[4:])
# As above said it will take automatically last value and print string from 4th postion to last

print(name[:6])
# Similar To above it start from 0 and print upto 5th index (5th include, 6th exclude)

print(name[-1])
# It will print last letter "e"
# Remember: In Negative indexing start from -1 not from 0

print(name[0:-1])
# That's awesome,it start from 0 and print the string before to "-1" means, string start from 0 and end with -2 (including)

# Negative Indexing 
print("A d i t y a   V a s t  e")
print("0 1 2 3 4 5 6 7 8 9 10 11 ")
print(".          . . . -3 -2 -1")

print(name[-3:2])
# This Will Not Work :/

print(name[2:-3])
# But This will work :)

print("---")
print(name[-5:-2])
# It is  giving result... ;)
# If You Make [-2:-5] then it will not give result.
print(name[-2:-5])
# It will not give result.
print(name[-2:-5:-1])
# It will give a result :)


print(name[::-1])
# Prints a reverse string (:: used)
# Based on three phase splicing (2:4:2)  --Mentioned at top of table.

# Ex.4 Operations on string

mystr = "Hello How are you"
print(len(mystr))

print(mystr.capitalize())
# Just capitalizes 1st word 

print(mystr.upper())
print(mystr.lower())
print(mystr.find("are"))
print(mystr.index("you"))
print(mystr.rindex("u"))
print(mystr.count("l"))
print(mystr.split())
# check our more at : https://www.w3schools.com/python/python_ref_string.asp
