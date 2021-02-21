def a(a):
    x='aieou'
    if a in x:
        print("vowel")
print(a('e'))


def sum_list(l):
    sum=0
    for x in l:
        sum=sum+x
        print(sum)
sum_list([5,5,5,5])



def maxi(l):
    max=l[0]
    for a in l:
        if a< max:
            max=a
            print(max)
maxi([5,3,55,5])

