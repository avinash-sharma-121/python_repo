
#"abcabcbb"

def find_non_repeting_max_sub_string(s):
    n=len(s)
    hash_map=set()
    left=0
    start=0
    max_substring_count=0
    for right in range(n):
        while s[right] in hash_map:
            hash_map.remove(s[left])
            left+=1
        
        hash_map.add(s[right])

        if right-left+1 > max_substring_count:
            max_substring_count=right-left+1
            start=left
    
    return s[start:start+max_substring_count]

print(find_non_repeting_max_sub_string("abcabcbb"))
