a=[1,3,2,5,4,87,56,3,4]

#bubble sort

print("--------------Bubble sort------------------")
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            
print(a)

#insertion sort
a=[1,3,2,5,4,87,56,3,4]
print("-------------Insertion sort-----------------")

for i in range(0,len(a)):
    key=a[i]
    j=i-1
    
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j-=1
    
    a[j+1]=key
    
print(a)
    


#######
#Output
#--------------Bubble sort------------------
#[1, 2, 3, 3, 4, 4, 5, 56, 87]
#-------------Insertion sort-----------------
#[1, 2, 3, 3, 4, 4, 5, 56, 87]
        
        
        
        
        
        
        
    
    
