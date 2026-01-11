# Goal: Write a @cache decorator that stores results of expensive function calls in a dictionary.

def cache(func):
    store={}
    def wrap(n):
        if n in store:
            return store[n]
        store[n]=func(n)
        return store[n]
    return wrap
@cache
def square(n):
    print("Computing")
    return n*n
print(square(4))
print(square(4))
