import re

#Outro exemplo

texto = "Ansha802ujzkndo"

letras = re.split(r'\d+',texto)

print(letras)


novos_caracteres = re.split(r'\D+',texto)

print('\n\n')

print(novos_caracteres)

#Lembrando que:

# \d = [0-9]

# \D = [^0-9] todo caractere que não é um dígito!
