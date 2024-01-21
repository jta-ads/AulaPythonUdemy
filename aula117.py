
def multi (numero):
    def multiplos (quant):
        return numero * quant
    return multiplos

duplica = multi(2)
triplicar = multi(3)
quadruplicar = multi(4)

print(duplica(3))
print(triplicar(3))
print(quadruplicar(3))