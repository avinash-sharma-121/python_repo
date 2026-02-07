# reverse an array list using recursion

a=[1,2,3,4,5]

def reverse_array(a,i,n):

    if i>=n//2:
        return
    a[i],a[n-i-1]=a[n-i-1],a[i]
    reverse_array(a,i+1,n)

reverse_array(a,0,len(a))
#print(a)

# reverse a array using recursion for i to k index

b = [1,2,3,4,5,6,7,8,9]

#print(b)
def reverse_array_ik(b,i,k):

    if i>=k:
        return
    
    b[i],b[k]=b[k],b[i]
    reverse_array_ik(b,i+1,k-1)

reverse_array_ik(b,2,7)
#print(b)



# implement palindrom with recursion

a="mnboiobnm"

left=0
right=len(a)-1

def palindrom_recursion(a,left,right):
    if left>=right:
        return True
    
    if a[left]==a[right]:
        return palindrom_recursion(a,left+1,right-1)
    else:
        return False
    
print(palindrom_recursion(a,left,right))