import pandas as pd

df = pd.read_csv('input.csv')

#simulacion archivo

df["out"] = ((df["in0"] & df["in1"]) | (df["in2"] & df["in3"])).astype(int)

#print(df)

#concatenar bits
bitstring = "".join(df["out"].astype(str).tolist())
print("bits concatenados:", bitstring)

#convenrtir cadena binario a texto ascii
#dividir de 8 en 8

chars = [chr(int(bitstring[i:i+8], 2)) for i in range(0, len(bitstring), 8)] 
decoded = "".join(chars)

print("\nTexto decodificado:", decoded)