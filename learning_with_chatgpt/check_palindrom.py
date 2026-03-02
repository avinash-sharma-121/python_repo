#Problem 2 — Check Palindrome (Without slicing)

s = "madam1"

def check_palindrom(s):
    l=0
    r=len(s)-1
    while l<=r:
        if s[l]==s[r]:
            l+=1
            r-=1
            continue
        else:
            return False
        
    return True

print(check_palindrom(s))