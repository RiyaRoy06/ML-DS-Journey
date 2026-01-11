# Goal: Print func.__name__ of a decorated function.

from functools import wraps
def deco(func):
    @wraps(func)
    def wrap(*args,**kwargs):
        return func(*args,**kwargs)
    return wrap
@deco
def test():
    "pass"
print(test.__name__)
print(test.__doc__)
