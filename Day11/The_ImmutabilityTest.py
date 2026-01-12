# Goal: Try to modify a tuple inside a map function.

nums=(1,2,3)
print("The answer is: ",nums,list(map(lambda x:x*2,nums)))
