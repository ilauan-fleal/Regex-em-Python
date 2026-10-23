#Exercício 2: Identificando padrões de núumeros de telefone com dois ou três dígitos:

import re

numero = input("Insira um número de telefone, considerando os parênteses e um traço entre os dígitos iniciais e finais:")

z = re.search(r'(.([0-9]*){3}.)\s+([0-9]*){4,5}[-]([0-9]*){4}',numero)

print(z)

#Lembrando que \s = [ \t\n\r\f\v]
cep = input("Introduza um CEP, considerando os 5 dígitos iniciais, o traço e os 3 últimos:")

k = re.search(r'(([0-9]*){5})[-]([0-9]*){3}', cep)

print(k)

cpf = input("Introduza um CPF, considerando que os 9 primeiros dígitos, deverão estar todos juntos e os últimos 2 separados por um traço:")

f = re.search(r'(([0-9]*){9})[-]([0-9]*){2}', cpf)

print(f)

email = input("Introduza um email, considerando a necessidade de usar o '@' e o .:")

g = re.search(r'[a-zA-Z0-9_]*[\][a-z].*',email)
print(g)
