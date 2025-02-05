#x = lambda a: a*a-3

#x(3)

#print(x(5))

#l = [4,5,8,12]
#l2 = list(map(lambda x:x*x,l,str(a) + "Kč" ))
#l3 = filter(lambda a: a<10,l)
#print(l2)

l = [4,5,8,12]
l = list(map(lambda a: str(a) + "Kč", filter(lambda a:a<10, l)))
print(list(l))
