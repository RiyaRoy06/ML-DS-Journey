# Goal: Calculate the product of a list(1*2*3*4) using functools.reduce.

from functools import reduce
result=reduce(lambda x,y:x*y,[1,2,3,4])
print("The result is: ",result)
