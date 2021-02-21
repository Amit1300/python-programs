l=[10,30,40,50,40]
l2=[]
for x in l:
    if x not in l2:
        l2.append(x)
print(l2)


def word(n,str):
    words=[]
    txt=str.split(" ")
    for x in txt:
        if len(x)>n:
            words.append(x)
    print(words)
word(3,"amit mohit yogesh ")
            
num=[x**2 for x in l]
print(num)


