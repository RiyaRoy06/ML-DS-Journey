# Goal: Write a generator that yields values from two sub-generator using yield from.

def gen1():
  yield 1
  yield 2
  yield 3
def gen2():
  yield 4 
  yield 5
  yield 6
def gen3():
  yield from gen1()
  yield from gen2()
g=gen3()
for i in g:
  print(i)
