S = []
i = 0
j = 0

def KSA(key):
	global S
	#Inicializa el arreglo S
	for i in range(256):
		S.append(i)
	j = 0
	for i in range (256):
		a=(i%(len(key)//2))*2
		j = (j + S[i] + int(key[a]+key[a+1],16)) % 256
		aux = S[i]
		S[i] = S[j]
		S[j] = aux

def PRGA():
	global S, i, j
	i = (i + 1) % 256
	j = (j + S[i]) % 256
	aux = S[i]
	S[i] = S[j]
	S[j] = aux
	return S[(S[i] + S[j]) % 256]

#CADENA --> ASCII
def str_hex(string):
	hx=''
	for x in string:
		hx += hex(ord(x))[2:]
	return hx

#primero KSA luego PRGA
KSA(str_hex(input()))
text=str_hex(input())#Guarda la entrada en formato ascii hexadecimal
auxXOR=''
for txt in range(0,len(text),2):
	auxK=bin(PRGA())[2:].zfill(8)#Guarda el byte actual del KS
	auxT=bin(int(text[txt:txt+2],16))[2:].zfill(8) #Guarda byte por cifrar del texto
	for x in range(8):#Se realiza el xor bit por bit de los bytes actuales
		auxXOR += str(int(auxT[x])^int(auxK[x]))
print(hex(int(auxXOR,2))[2:].upper())#Transforma el resultado de xor a hexadecimal

