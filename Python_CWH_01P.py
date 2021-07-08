#--------☆ Practise Set 1 Started ☆------------

# Q.1 Write a programme to print the poem or lyrics of twinkle twinkle song

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
''')

print("-----------------------")

# This Is how you can write a new line using a python ,use a '''(Triple single quotation marks) due to this what you have written in any manner it will execute.
# If you use double or single quotation mark then it will not print it will give a error as "Error while scanning the string literal"
# The single and double quotation marks are made for single line only 

#Q.2: Print table of 5 using REPL

# Using the terminal/interpreter you can do it.
# You must start with writing a "Python" so it will understand you are writing/excuting a python codes from here

#Q.3: Write a code to import a modules and run a code

#pip install playsound

#from playsound import playsound
#playsound('/storage/emulated/0/#Music/cradlespy.mp3')

import sys 
print("The Current Version is : ",sys.version)
print("-----------------------")
print("The Current Version_Info is : ",sys.version_info)
print("-----------------------")

# In terminal on android currently we can't use <playsound> module.
# Here we used the // because a single slash and character coinside then different sequences are made. 

#Q 4: Write A python program to print the directories in your programs using os module by searching on web.

import os
print(os.listdir())  #List of files or directories 
print(os.getcwd())   # Curent working directories

#OR

#import os
#files = os.listdir()
#print(files) #print(files[0])

print("-----------------------")
# It forms the LIST of files and directories

#Q 5: For The Question 4 write A author,name (labels) using comments

# Author : Aditya Vaste
# Place  : Uplai bk
# Date   : 02/06/2021

import os
print(os.listdir()[0]) #1st element of array

#--------☆ Practise Set 1 Completed ☆----------