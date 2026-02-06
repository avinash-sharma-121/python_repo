
# Basic practice of creating frequency map of integers in a list
a=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

frequency_map={}

for i in a:
    if i in frequency_map:
        frequency_map[i]+=1
    else:
        frequency_map[i]=1

print(frequency_map)

# enhanced version using get method

b=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

fm={}
for i in range(len(b)):
    fm[b[i]]=fm.get(b[i],0)+1
print(fm)