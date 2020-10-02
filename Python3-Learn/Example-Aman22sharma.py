// AUTHOR: Aman Kumar sharma
// Python3 Concept: Demo Example
// GITHUB: https://github.com/Aman22sharma

//Add your python3 concept below

#Standard Data Types in Python :
#Python Numbers
var1 = 50
var2 = 45.5
var3 = 3.14j
print(type(var1))
print(type(var2))
print(type(var3))

#Python Strings
str = 'Hello World!'

print(type(str))
print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string

#Python List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(type(list))
print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd 
print(list[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist) # Prints concatenated lists

#Python Tuple
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(type(tuple))
print(tuple)           # Prints complete tuple
print(tuple[0])        # Prints first element of the tuple
print(tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print(tuple[2:])       # Prints elements starting from 3rd element
print(tinytuple * 2)   # Prints tuple two times
print(tuple + tinytuple) # Prints concatenated tuple

#Python Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(type(dict))
print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values
