# Goal: Compare map(lambda...) vs (x... for x...).

import time
start=time.time()
result=list(map(lambda x:x*x,[1,2,3,4,5,6]))
end=time.time()
print("Time taken for map+lambda: ",end-start)
start=time.time()
result_2=(x+1 for x in [1,2,3,4,5,6])
end=time.time()
print("Time taken for x... for x...: ",end-start)
