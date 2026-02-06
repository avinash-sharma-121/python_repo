
#Need to find the occurance of each number in the list
#Using hashing technique to store the frequency of each number
n=[1,2,1,5,7,5,9,1,2,5,7,9,3,4,6,8,3,2,1]

m=[12,32,131,1,3,4,5,5,5,5,3,2,1,2,3,4,5,6,7,8,9,0,34,54,234,532,123,123,123,12]


# hash_list to store frequency

#output={}
hash_list=[0]*10
for i in n:
    hash_list[i]+=1

for i in m:
    if i < 0 or i > 10:
        print(0)
    else:
        print(hash_list[i])


# next method using dictionary

hash_dict={}

print("Using dictionary")

for i in n:
    if i in hash_dict:
        hash_dict[i]+=1
    else:
        hash_dict[i]=1

for i in m:
    if i in hash_dict:
        print(hash_dict[i])
    else:
        print(0)