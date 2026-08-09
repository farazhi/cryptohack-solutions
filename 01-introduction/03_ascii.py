#!/usr/bin/env python3
""" CryptoHack - Introduction - ASCII """

# Lista de inteiros que precisam ser convertidos para caractere a partir da tabela ASCII
lista = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("Flag: ", end="")
# Percorre cada inteiro da lista e o transforma em caractere da tabela ASCII
for caractere in lista:
    print(chr(caractere), end="")
print()