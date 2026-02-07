# fibonacchi no with loop

n=9
sum=0
for i in range(0,n):
    #print(sum)
    sum+=i
    

#print(sum) not working

# lets try with recursion

def fibo_func(n):
    if n==0 or n==1:
        return n
    return fibo_func(n-1)+fibo_func(n-2)

print(fibo_func(n))