#list practice
a=[1,2,3,4,5]
print(a)
#reverse the list
print(a[::-1])
#a=a[::-1]
print(a)
#slicing the list
print(a[2:5])
#length of the list
print(len(a))
#append an element  
a.append(6)
print(a)
#insert an element at index 2
a.insert(2, 2.5)
print(a)
#remove an element      
a.remove(3)
print(a)
#pop an element
a.pop()
print(a)
#sort the list
a.sort(reverse=True)
print(a)
#join a list of strings
d=["Hello", "World"]