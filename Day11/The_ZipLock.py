# Goal: Combine names=["A","B"] and ages=[20,30] into a dictionary.

names=["A","B"]
ages=[20,30]
result=dict(zip(names,ages))
print("The result is: ",result)
