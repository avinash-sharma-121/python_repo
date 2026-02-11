#Bassic approach like we can sort the array/list and return second larget
a=[12,-23,10,34,54,11,4,5,89,31,21]

a.sort()

print(a)

print(a[-2])
print(a[len(a)-2])

#now lets go with best approach

largest=float("-inf")
sec_larget=float("-inf")

for i in range(0, len(a)):
    if largest < a[i]:
        largest=a[i]
for i in range(0, len(a)):
    if sec_larget < a[i] and a[i] != largest:
        sec_larget=a[i]

print(sec_larget)

# now optimul solution

largest=float("-inf")
sec_larget=float("-inf")

print("best solution")

for i in range(0,len(a)):
    if largest < a[i]:
        sec_larget=largest
        largest=a[i]
    elif a[i]> sec_larget and a[i]!=largest:
        sec_larget=[i]

    

print(sec_larget)

# thrd max no

largest=float("-inf")

sec_larget=float("-inf")

thi_larget=float("-inf")

for i in range(0, len(a)):
    if largest < a[i]:
        sec_larget=largest
        largest=a[i]

    
# Need to work on thir largest no