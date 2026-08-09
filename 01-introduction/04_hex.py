#!/usr/bin/env python3
""" CryptoHack - Introduction - Hex """

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Converte a string hexadecimal em bytes
flag_bytes = bytes.fromhex(hex_string)

# .decode() converte os bytes para texto legível (UTF-8/ASCII)
flag_legivel = flag_bytes.decode()
print(flag_legivel)