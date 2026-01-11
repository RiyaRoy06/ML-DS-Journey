# Goal: Create a @timer decorator that prints execusion time using time.time().

import time
def timer(func):
  def inner(*args,**kwargs):
    start=time.time()
    result=func(*args,**kwargs)
    end=time.time()
    print("Execution time: ",end-start,"seconds")
    return result
  return inner
@timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

print(slow_add(3, 4))
