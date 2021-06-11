# PRACTICE SET 3
#STRINGS

# Q.1 Write a python program to print the Good Morning <Name> using users input
name = input("What is your name\n")
print(f"Good Morning {name}")

# Q.2 Write python program to display a greeting message with given date and Name 

uname = input("Your Name : ")
udate = input("Enter Date : ")

print("----------------------------------")
print(f'''Hello,{uname}
     Congratulations !!! 
     You are selected for the Microsoft Company 
                   Regards,
                   Microsoft Team
                   {udate}
''')
print("----------------------------------")

# Or 

template = '''Hello,{NAME}
     Congratulations !!! 
     You are selected for the Microsoft Company 
                   Regards,
                   Microsoft Team
                   {DATE}
'''
template = template.replace("{NAME}","Aditya")
template =template.replace("{DATE}","29 Feb 2020")
print(template)

print("----------------------------------")

# Q.3 Write a program to find double spaces in string. 

thestr = "Hello  how are you  brother"
print(thestr.find("  "))
print(thestr.count("  "))

# Q.4 Replace that double spaces by single spaces

print(thestr.replace("  "," "))

# Q.5 Write a programme to format the letter using escape sequences.

str123 = "Dear Harry,This Python courses are awesome. Thanks!! "
print(str123)

str123 = "Dear Harry,\n\tThis Python courses are awesome. \n \t\t\t Thanks!! "
print(str123)