def str2(func):
    def inner():
        str3=func()
        return str3.upper()
    return inner





@str2
def str1():
    return "amit"
print(str1())
