# Goal: Create @admin_required. If global USER!='admin', raise PermissionError.

USER="guest"
def admin_required(func):
    def wrap(*args,**kwargs):
        if USER!="admin":
            raise PermissionError("Admin access required")
        return func(*args,**kwargs)
    return wrap
@admin_required
def dashboard():
    print("Admin Panel")
try:
    print(dashboard())
except PermissionError as e:
    print(f"Access denied: {e}")
USER="admin"
print(dashboard()) 
