# Goal: Write a function wrapper(func) that runs code before/after runs. Apply it manually: new_func=wrapper(old_func).

def wrapper(func):
  def inner():
    print("Before Hello")
    func()
    print("After Hello")
  return inner
def hello():
  print("Hello")
new_func=wrapper(hello)
new_func()
