#!/usr/bin/env python3
""" CryptoHack - Introduction - Base64 """

import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Converte a string hexadecimal em bytes
flag_bytes = bytes.fromhex(hex_string)

# Codifica os bytes em Base64
flag_base64 = base64.b64encode(flag_bytes)

# Converte o objeto de bytes em string legível para exibir na tela
print(flag_base64.decode())