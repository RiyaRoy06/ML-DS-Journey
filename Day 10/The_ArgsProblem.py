# Goal: Try to decorate a function that takes arguments add(a,b) with a wrapper that takes none.

def  deco(func):
  def inner(*args,**kwargs):
    print("Before Hello")
    return func(*args,**kwargs)
    print("After Hello")
  return inner
@deco
def add(a,b):
  return a+b
print(add(4,5))
