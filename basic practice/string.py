a="avinash"
print(a)
#reverse the string
print(a[::-1])
#a=a[::-1]
print(a)
#slicing the string
print(a[2:5])
#length of the string
print(len(a))
#convert to uppercase
print(a.upper())
#convert to lowercase
print(a.lower())
#replace a character
print(a.replace("a","o"))
#find a character
print(a.find("n"))
#check if string is alphanumeric
print(a.isalnum())
#check if string is alphabetic
print(a.isalpha())
#check if string is numeric
print(a.isnumeric())
#split the string
print(a.split("i"))
#strip whitespace
b="  avinash  "
print(b.strip())
#concatenate strings
c="kumar"
print(a + " " + c)
#format string
print("Hello, {}".format(a))
#check if string starts with a substring
print(a.startswith("avi"))
#check if string ends with a substring
print(a.endswith("nash"))
#count occurrences of a character
print(a.count("a"))
#capitalize the string
print(a.capitalize())
#title case the string
print(a.title())
#check if string is lowercase
print(a.islower())
#check if string is uppercase
print(a.isupper())
#replace substring
print(a.replace("avinash", "avikumar"))
#join a list of strings
d=["Hello", "World"]