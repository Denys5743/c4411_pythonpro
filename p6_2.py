try:
    print("start code")
    print(10/0)
    print("No error")
except NameError:
    print("We have a NameError")
except ZeroDivisionError:
    print("We have a ZeroDivisionError")
print("code after")