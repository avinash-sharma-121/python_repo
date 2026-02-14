#find the first non-repeating chatarter in string 

#first method using hash_map

a="swissabcaambbcwi"

hash_map={}

for i in range(len(a)):
    if a[i] in hash_map:
        hash_map[a[i]]+=1
    else:
        hash_map[a[i]]=1

#print(hash_map)

for key,value in hash_map.items():
    if value==1:
        print(key)
        break


# now lets try with assici method

arr=[0]*26


print(arr)


for ch in a:
    char_ass=int(ord(ch))
    #print(char_ass)
    arr[char_ass-97]+=1


for i in range(len(arr)):
    if arr[i]==1:
        print(i)
        get_char=chr(i+97)
        print(get_char)
        break

print(arr)

print(ord('@'))
print(chr(64))

