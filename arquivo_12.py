#Exercício 1 -> Identificar um número real, que pode ser um valor inteiro ou de ponto flutuante!

import re

numero = input("Introduza um valor numérico:")

y = re.search(r'^[+-]?[0-9]*.[0-9]*$', numero)

print(y)







