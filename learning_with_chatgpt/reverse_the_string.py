s = "oracle"

#basic slicing method
def reverse_string(s):
    return s[::-1]
print(reverse_string(s))


#manuall way to reverse the string

def reverse_string_manual(s):

    l=0
    r=len(s)-1

    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return "".join(s)
    

print(reverse_string_manual(list(s)))