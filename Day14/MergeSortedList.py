# Goal: Combine two sorted lists into one sorted list.

a=[10,15,20]
b=[5,11,17,25,30]
i=j=0
arr=[]
while i<len(a) and j<len(b):
 if a[i]<b[j]:
   arr.append(a[i])
   i+=1
 else:
   arr.append(b[j])
   j+=1
arr+=a[i:]+b[j:]
print(arr)
