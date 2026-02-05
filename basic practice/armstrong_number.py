# need to check if the number is armstrong number or not

def armstrong_number(n):
    original=n
    sum=0
    while n>0:
        num=n%10
        sum=sum+num**len(str(original))
        n=n//10
    if original==sum:
        return True
    else:
        return False
    
print(armstrong_number(153))
print(armstrong_number(123))
print(armstrong_number(1634))   