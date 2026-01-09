# Goal: Manually call next(gen) untill it crashes.

def gen():
  yield from[1,2,3,4,5]
g=gen()
while True:
  try:
    print(next(g))
  except StopIteration:
    print("Generator Crashed")
    break
