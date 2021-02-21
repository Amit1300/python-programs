#list comprenhsion
l=[i*2 for i  in range(1,11)]
print(l)



l2=['RAJ','MOHAN','SHOHAN']
l3=[i[0] for i in l2]
print(l3)



l4=[i[::-1] for i in l2]
print(l4)


l5=[n for n in range(1,21) if n%2==0]
print(l5)



