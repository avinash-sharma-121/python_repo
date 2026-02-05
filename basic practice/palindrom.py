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
    
print(is_palindrome(121))
print(is_palindrome(123))