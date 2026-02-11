# simple brute force method.

#a=[2, 3, -8, 7, -1, 2, 3,12,-9]
a=[-2,1,-3,4,-1,2,1,-5,4]

maxi=float("-inf")

for i in range(0,len(a)):
    total=0
    for j in range(i,len(a)):
        total=total+a[j]
    maxi=max(maxi,total)

print(maxi)

# optimal solution Kadanes algo

maxi=float("-inf")

sum=0

for i in range(0,len(a)):
    sum=sum+a[i]
    maxi=max(sum,maxi)
    if sum < 0:
        sum=0
    
print(maxi)