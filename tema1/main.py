
# ex 1
import copy

lista = [7,8,9,2,3,1,4,10,5,6]

# ex 2
lista_ordonata = copy.deepcopy(lista)
lista_ordonata.sort()
print(lista)
print(lista_ordonata)

# ex 3
lista_ordonata_desc = copy.deepcopy(lista)
lista_ordonata_desc.sort()
lista_ordonata_desc.reverse()
print(lista)
print(lista_ordonata)

# ex 4
print(lista_ordonata[1::2])

# ex 5
print(lista_ordonata[::2])

# ex 6
print(lista_ordonata[2::3])


