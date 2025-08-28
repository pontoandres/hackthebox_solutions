from pathlib import Path

contenido = Path("out.txt").read_text(encoding="utf-8").strip()

lineas = contenido.splitlines()

if len(lineas) != 3:
    raise ValueError(f"se esperaban 3 lineas (iv, C2, C2) y hay {len(lineas)}, revisa  out.txt")

iv_hex = lineas[0].strip()
c1_hex = lineas[1].strip()
c2_hex = lineas[2].strip()

print("IV (hex):", iv_hex)
print("C1 (hex) len:", len(c1_hex), "chars", c1_hex)
print("C2 (hex) len:", len(c2_hex), "chars", c2_hex)

message = b"Our counter agencies have intercepted your messages and a lot "
message += b"of your agent's identities have been exposed. In a matter of "
message += b"days all of them will be captured"

c1 = bytes.fromhex(c1_hex)
c2 = bytes.fromhex(c2_hex)
iv = bytes.fromhex(iv_hex)
 # forma 1 sacar K con K = c1 XOR plaintext 1 (message)
keystream = bytes( [a^b for a,b, in zip(c1, message)] )

print("Keystream (hex):", keystream.hex())

#luego usar Flag = K XOR c2
flag = bytes([a^b for a,b in zip(keystream, c2)])

print("Flag (plaintext):", flag.decode("utf-8"))

#forma 2 no hay necesidad de sacar K si se hace c1 XOR c2 = p1 XOR p2 (p1 y p2 son plaintext1 y plaintext2)
p1XORp2 = bytes([a^b for a,b, in zip(c1, c2)])
print("p1 XOR p2:", p1XORp2.hex())

#luego sacamos p2 directamente usando p2 = (p1 XOR (p1XORp2 = c1XORc2))
p2 = bytes([a^b for a,b in zip(p1XORp2, message)])
print("Flag (plaintext) forma 2:", p2.decode("utf-8"))