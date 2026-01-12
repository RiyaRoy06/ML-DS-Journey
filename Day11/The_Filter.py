# Goal: Remove all negative numbers from a list using filter().

result=list(filter(lambda x:x>=0,[1,-2,3,-4,5,-6]))
print("The result is: ",result)
result_2=(list(filter(None,[None,1,'hi','hello',0,2,6,5])))
print("The result is: ",result_2)
