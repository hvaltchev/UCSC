#!/usr/bin/env python3
"""Two string types in Python 3:
      str and bytes
""" 
yen_symbol = chr(165) # unicode int
print("yen_symbol = chr(165)")
print("yen_symbol =", yen_symbol)
print("ord(yen_symbol) =", ord(yen_symbol))
print("type(yen_symbol) =", type(yen_symbol))
print()

yen_bytes = yen_symbol.encode("utf-8")
print('yen_bytes = yen_symbol.encode("utf-8")')
print("type(yen_bytes) =", type(yen_bytes))
print("yen_bytes =", yen_bytes)
print("""bytes(yen_symbol, encoding="utf-8") =""",
      bytes(yen_symbol, encoding="utf-8"))
print()

greeting = "Hello"
print('greeting = "Hello"')
print("type(greeting) =", type(greeting))
print("greeting =", greeting)
print("""bytes(greeting, encoding="utf-8") =""",
      bytes(greeting, encoding="utf-8"))
print()

greeting_bytes = b"Hello"
print('greeting_bytes = b"Hello"')
print("type(greeting_bytes) =", type(greeting_bytes))
print("greeting_bytes =", greeting_bytes)
print('str(greeting_bytes, encoding="utf-8") =',
      str(greeting_bytes, encoding="utf-8"))
print()
