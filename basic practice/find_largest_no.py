a=[12,-23,10,34,54,11,4,5,89,31,21]

#Basic Python way
print(max(a))

# Using for loop basic traverse

max1=a[0]
for i in range(0,len(a)):
    if a[i]>=max1:
        max1=a[i]
print(max1)

# Uisng keeping varialbe -inf varialbe as an max value 

max2=float("-inf")
print(max2)

for i in range(0,len(a)):
    max2=max(a[i],max2)

print(max2)
