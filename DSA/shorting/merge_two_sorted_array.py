
a=[1,2,5,8,33,78]
b=[3,4,8,9]

i=0
j=0

len_a=len(a)
len_b=len(b)
output=[]

while i < len_a and j < len_b:
    if a[i] <= b[j]:
        output.append(a[i])
        i+=1
    else:
        output.append(b[j])
        j+=1

if i < len_a:
    while i<len_a:
        output.append(a[i])
        i+=1

if j < len_b:
    while j<len_b:
        output.append(b[j])
        j+=1


print(output)

###

#output=[]
#max_len=0
#
#if len_a>len_b:
#    max_len=len_b
#else:
#    max_len=len_a
#
#for i in range(0,max_len):
#    print(a[i],b[j])
#    if a[i]>b[j]: 
#        output.append(b[j])
#        j=j+1
#    else:
#        output.append(a[i])
#print(output)
###

