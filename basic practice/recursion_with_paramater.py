#print x, n times using recursion

def func(x,n):

    if n==0:
        return
    print(x)
    func(x,n-1)

#func("Avinash", 5)

# print1 to n using recursion

def funct1(i,n):

    if i>n:
        return
    print(i)
    funct1(i+1,n)

#funct1(1,5)

# same we will try with backtracking tail recursion

def funct2(i,n):

    if i>n:
        return
    funct2(i+1,n)
    print(i)

#funct2(1,5)

# print 1 to n using tail recursion backtracking

def func3(n):

    if n==0:
        return
    func3(n-1)

    print(n)

#func3(5)


# find the sum of n natural numbers using recursion

def sum_natural(n):

    if n==0:
        return 0
    
    return n+ sum_natural(n-1)

#print(sum_natural(10))

# lets try with three variables sum of n natural numbers using recursion

def find_sum(sum,i,n):
    if i>n:
        return sum
    sum+=i
    return find_sum(sum,i+1,n)

#print(find_sum(0,1,10))


# factorial of n using recursion

def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)

print(factorial(0))