# Goal: Apply two decorators: @bold and @italic to a string returning function.

def bold(func):
    def wrap(*args,**kwargs):
        return "<b>"+func(*args,**kwargs)+"</b>"
    return wrap
def italic(func):
    def wrap(*args,**kwargs):
        return "<i>"+func(*args,**kwargs)+"</i>"
    return wrap
@bold
@italic
def text():
    return "Hello Riya!"
print(text())
