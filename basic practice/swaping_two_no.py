a=12
b=14
print(f"before swapping: a={a}, b={b}")

# using third variable
temp=a
a=b
b=temp

print(f"after swapping using third variable: a={a}, b={b}")

# without using third variable
a=a+b
b=a-b
a=a-b

print(f"after swapping without using third variable: a={a}, b={b}")
