n=10

def find_factors(n):
    factor=[]
    for i in range(1,n+1):
        if n%i==0:
            factor.append(i)
    
    return factor
print(find_factors(n))

# optimized way

def optimized_find_factors(n):
    factor=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            factor.append(i)
        if n//i!=i and n%i==0:
            factor.append(n//i)
    
    return sorted(factor)

print(optimized_find_factors(n))


#more optimized way

from math import sqrt
def more_optimized_find_factors(n):
    factor=[]
    for i in range (1, int(sqrt(n))+1):
        if n%i==0:
            factor.append(i)
            if n//i!=i:
                factor.append(n//i)

    return sorted(factor)

print(more_optimized_find_factors(n))