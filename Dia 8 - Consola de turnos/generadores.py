#los generadores ayudan a producir código cada que se necesite
#de una lista [1,2,3,4,5,6] devolvera [1,], [1,2] y así sucesivamente cada que se requiera

def mi_generador():
    yield 4

print(mi_generador())

g = mi_generador()

#print(next(g))

#ejemplo iterador
def otro_generador():

    for x in range(1, 5):
        yield x * 10


g1 = otro_generador()

print(next(g1))
print(next(g1))
