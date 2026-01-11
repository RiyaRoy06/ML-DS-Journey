# Goal: Apply the wrapper using the @decorator syntex.

def my_decorator(func):
  def inner():
    print("Before Hello")
    func()
    print("After Hello")
  return inner
@my_decorator
def hello():
  print("Hello")
hello()
