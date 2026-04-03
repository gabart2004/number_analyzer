#LEITURA DOS NÚMEROS

n1, n2 = map(int, input("Digite dois números: ").split())

if n1 > n2:
	n1, n2 = n2, n1

# CONTADOR DE PARES E ÍMPARES

pares = 0
soma_pares = 0
impares = 0
soma_impares = 0
lista_pares = []
lista_impares = []

for p in range(n1, n2+1):
	if p%2 == 0:
		pares += 1
		soma_pares += p
		lista_pares.append(p)
	else:
		impares += 1
		soma_impares += p
		lista_impares.append(p)

print(f"\nTotal de números pares: {pares}")
print(f"Soma dos pares: {soma_pares}")
print(f"Números pares: {lista_pares}")	
print(f"\nTotal de números ímpares: {impares}")
print(f"Soma dos ímpares: {soma_impares}")
print(f"Números ímpares: {lista_impares}")

# TOTAL DE NÚMEROS PARES E ÍMPARES E SOMA ENTRE ELES

print(f"\nTotal de pares e ímpares: {pares+impares}")

#SOMA TOTAL ENTRE OS PARES E ÍMPARES

soma_total = soma_pares + soma_impares
print(f"Soma entre os números: {soma_total}")

# MÉDIA ENTRE PARES E ÍMPARES

if pares> 0:
	media_pares = soma_pares/pares
else:
	media_pares = 0
print(f"\nMédia entre os pares: {media_pares}")

if impares > 0:
	media_impares = soma_impares/impares
else:
	media_impares = 0

print(f"Média entre os ímpares: {media_impares}")