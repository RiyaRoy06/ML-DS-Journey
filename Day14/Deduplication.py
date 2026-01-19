# Goal: Remove duplicates from a list while keeping order.

l=[2,2,4,4] 
a=[]
for i in l:
  if i not in a:
    a.append(i)
print(a)
