# reverse string

a = "hello"
b = a[::-1]
print(b)  # output: "olleh"


print(''.join(reversed(a)))  # output: <reversed object at ...>

# another method to reverse string
c = ''.join(reversed(a))
print(c)  # output: "olleh"


# using loop to reverse string
d = ""
for char in a:
    d = char + d
print(d)  # output: "olleh"


# using recursion to reverse string
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])       
