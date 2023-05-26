from triangulo import Triangulo

ladoA = 12
ladoB = 17
ladoC = 15
t1 = Triangulo(ladoA, ladoB, ladoC)
t2 = Triangulo(ladoA, ladoB, ladoC)

t2 = t1

print(id(t1))
print(id(t2))

if t1 == t2:
    print("Os objetos são iguais")
else:
    print("Os objetos são diferentes")