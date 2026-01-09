# Goal: Create two generator: one squares numbers and other filter evens. Chain them: filter(square(nums)).

def gen():
  yield from[1,2,3,4,5,6,7,8,9,10,11]
g=gen()
def square(gen):
  for x in gen:
    yield x*x
def filter_even(gen):
  for x in gen:
    if x%2==0:
      yield x
result=filter_even(square(g))
for i in result:
  print("The result is: ",i)
