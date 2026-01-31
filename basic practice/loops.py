a=["a","b","c","d"]

for i in a:
    print(i) 

a.append("e") # Meanse addign in last
print(a)

a.pop()  # removes last element
print(a)

a.pop(0) # removes element at index 0
print(a)

a.insert(0,"f") # inserts f at index 0
print(a)

a.insert(3,"demo") # inserts demo at index 3
print(a)

a.remove("c") # removes element with value c
print(a)

a.sort() # sorts the list
print(a)