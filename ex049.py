tabuada = int(input('qual tabuada você quer? '))
armazen = tabuada

for i in range(1, 11):
    armazen = tabuada * i
    print('{} * {} = {}' .format(tabuada, i, armazen))