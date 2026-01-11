# Goal: Write a decorator that forgets to return func(*args). Print the result of the decorated function.

def deco(func):
  def inner(*args,**kwargs):
    func(*args,**kwargs)
  return inner
@deco
def add(a,b):
  return a+b
print(add(4,5))
