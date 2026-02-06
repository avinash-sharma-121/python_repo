freq=["a","b","c","a","b","c","m","c","d","z","z","y","z"]

que=["q","b","a","r","c","z"]

#lets try with hash_list

hash_list=[0]*26

for i in range(len(freq)):
    assici_val=ord(freq[i])
    #print(assici_val)
    index_value=assici_val-97
    hash_list[index_value]+=1

#print(hash_list)
    
for i in range(len(que)):
    assici_val=ord(que[i])
    index_value=assici_val-97
    print(f"for {que[i]} total char count is {hash_list[index_value]}")
    
#Lets try with dict

hash_dict={}

for i  in freq:
    if i in hash_dict:
        hash_dict[i]+=1
    else:
        hash_dict[i]=1
print(hash_dict)

for i in que:
    if i in hash_dict:
        print(f"for {i} total char count is {hash_dict[i]}")
    else:
        print(f"for {i} total char count is 0")
