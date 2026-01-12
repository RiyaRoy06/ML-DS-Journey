# Goal: Check if any number in a list is negative. Check if all are positive.

print("Any number is negative: ",any(x<0 for x in [1,2,-3,-1,-6]))
print("All numbers are positive: ",all(x>0 for x in [1,2,-3,-1,-6]))
