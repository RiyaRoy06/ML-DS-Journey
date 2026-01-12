# Goal: Create a function power(base,exp). Use functools.partial to create a new function square(x) that locks exp=2.

from functools import partial
def power(base,exp):
  return base**exp
square=partial(power,exp=2)
print("The answer is: ",square(7))
