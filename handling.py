try:
    n=int(input("enter number"))
    if n==type(int):
        print(n)
except exception:
    print("type error")
else:
    print("int")
finally:
    print("dhvdshd")

class amiterror(Exception):
    pass
def valid(val):
    if len(val)<5:
        raise amiterror(" amiterror")
name=input("put name")
valid(name)
print(name)


import pdb
pdb.set_trace()
name=input("segsg")
print(name)
