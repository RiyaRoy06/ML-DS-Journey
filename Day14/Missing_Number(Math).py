# Goal: List 1 to 100 is missing one number. Find it.

l=list(range(1,101))
l.remove(67)
a=0
for i in l:
  a+=i
b=(100*(100+1))//2
print("The missing number is: ",b-a)
