#!/usr/bin/env python3
""" CryptoHack - Introduction - Bytes and Big Integers """
""" Pré-requisito: pip install pycryptodome """

from Crypto.Util.number import *

# Número inteiro fornecido pelo desafio
num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Converte o inteiro para bytes
flag_bytes = long_to_bytes(num)

# Decodifica os bytes para a string final da flag
print(flag_bytes.decode())
