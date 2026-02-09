#permission checker
def admin_only(func):
    def wrapper(username):
        if username=="admin":
            func(username)
        else:
            print("access denied")
    return wrapper
@admin_only
def dashboard(username):
    print("welcome to dashboard")
dashboard("admin")
dashboard("me")

