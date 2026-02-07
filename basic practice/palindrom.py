# find palindrom for integer

def is_palindrome(n):
    original=n
    reverse_num=0
    while n>0:
        num=n%10
        reverse_num=reverse_num*10+num
        n=n//10
    if original==reverse_num:
        return True
    else:
        return False
    
#print(is_palindrome(121))
#print(is_palindrome(123))


# check char palindrom

a="nitin"

def palindrome(a):
    l=0
    r=len(a)-1
    while l<r:
        if a[l]==a[r]:
            l+=1
            r-=1
            continue
        else:
            return False
    
    return True

print(palindrome(a))        
