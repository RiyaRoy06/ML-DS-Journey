# Goal: Find two numbers in a list that add up to target.

nums=[2,5,11,15,4,7];target=9
s={}
for n in nums:
 if target-n in s: print(n,target-n)
 s[n]=1
