# Goal: Create a decorator that accepts a setting: @repeat(times=3).

def repeat(times):
    def deco(func):
        def wrap(*args,**kwargs):
            for _ in range(times):
                func(*args,**kwargs)
        return wrap
    return deco

@repeat(3)
def hello():
    print("Hi Riya!")

hello()
