a=1234523422332

count=0
while a> 0:
    count+=1
    a=a//10

print("Number of digits:",count)

## Another way

b = 2343242342342342355423424234242423

c=str(b)

print("Number of digits:",len(c))

# count the difits with log

from math import *

def count_digits(n):
    if n == 0:
        return 1
    return log10(n)+1

print("Number of digits:",int(count_digits(1234523422332)))