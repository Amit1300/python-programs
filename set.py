import operator
d={1:2,3:4,4:3,2:1,0:0}
x=dict(sorted(d.items(),key=operator.itemgetter(1)))
d.update({2:15})
print(d)




dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
    print(d)
print(dic4)


d = {'x': 10, 'y': 20, 'z': 30} 
for p,dict_value in d.items():
    print(p,"=",dict_value)
	
n=int(input("amti"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x


print(d)

for x,y in d.items():
    print(x,d[x])
