# Goal: Create a generator g. Loop through it once. Try to loop through it again.

def gen():
  yield 1
  yield 2
  yield 3
  yield 4
g=gen()
print("First Loop: ")
for i in g:
  print(i)
print("Second Loop: (not created)")
for i in g:
  print(i)
