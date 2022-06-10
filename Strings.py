# "String" a Data structure used in python and its methods..
'''
 Now Methods of Strings are
1 len()  : To get the length of a string, use the len() function.
2 upepr()  : The upper() method returns the string in upper case
3 lower()  : The lower() method returns the string in lower case
4 strip()  : Whitespace is the space before and/or after the actual text,
             and very often you want to remove this space
5 replace()  : The replace() method replaces a string with another string
6 split()  : The split() method returns a list where the 
             text between the specified separator becomes the list items.
7 capitalize() :	Converts the first character to upper case
8 casefold():	Converts string into lower case
9 center() :	Returns a centered string
10 count() :	Returns the number of times a specified value occurs in a string
11 encode():	Returns an encoded version of the string
12 endswith():	Returns true if the string ends with the specified value
13 expandtabs():	Sets the tab size of the string
14 find() : 	Searches the string for a specified value and returns the position of where it was found
17 index(): 	Searches the string for a specified value and returns the position of where it was found
18 isalnum() :	Returns True if all characters in the string are alphanumeric
19 isalpha() :	Returns True if all characters in the string are in the alphabet
20 isdecimal():	Returns True if all characters in the string are decimals
21 isdigit():	Returns True if all characters in the string are digits
22 islower() :	Returns True if all characters in the string are lower case
23 isnumeric():	Returns True if all characters in the string are numeric
24 isupper() :	Returns True if all characters in the string are upper case
25 join() : 	Joins the elements of an iterable to the end of the string
26 find()	Searches the string for a specified value and returns the last position of where it was found
27 startswith()	Returns true if the string starts with the specified value
28 title()	Converts the first character of each word to upper case

'''

abc = "Automobile industry in INDIA is growing rapidly"
print('1 length of the string is: ', len(abc))
print('2 upper case string:\n', abc.upper())
print('3 lower case string:\n', abc.lower())
print("4", abc.replace("Automobile", "car"))
print('5 capitalised string:\n', abc.capitalize())
print('6 string casefold:\n', abc.casefold())
print('7  Count of A : ', abc.count("A"))
print("8 Find position of 'in' within string: ", abc.find("in"))
print("9 index of Character/s 'in': ", abc.index('in'))




