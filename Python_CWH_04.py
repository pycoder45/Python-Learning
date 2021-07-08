# Chapter 4
# Lists  and tuples

# 🎯 1.LISTS

a = [1,4,7,53,29]
print(a)

# Indexing start from 0
print(a[0],a[1],a[-1])

# IndexError: list index out of range
#print(a[6]) 

# You Can Change the list items,mutable...
a[3] = "Changed :)"
print(a)

# We can create a list items with different data Types 
b = [34,"Harrybhai",True,45.93]
print(b)

# We can make the slicing of list 
# Rules of slicing of string and list are same
c = ["Rahul","Narendra","Amar","Vishwa","Divya"]
print(c[0:2])
print(c[::-1])

# Methods of list
numbers = [3,8,7,9,28,86,92,23]

# Sort the list 
# print(numbers.sort())
# This is not works.....because it changes the actual list. 
numbers.sort()
print(numbers)

# Reverse the list
numbers.reverse()
print(numbers)

# Append element at a end of list 
numbers.append(45)
print(numbers)

# Insert at perticular index 
numbers.insert(2,4444) 
# Insert 4444 at index 2
print(numbers)

# Pop 
numbers.pop(2)
# Delete the element with index 2
print(mum)


