#Casamento dos operadores +,-,?,* e {,}
import re

enunciado = r"Algoritmos e {em} programação {/em} de computadores"

x = re.search(r'Al(.*?)e(.*?)o',enunciado)

print(x.group())

y = re.search(r'Al(.+)e(.+)res',enunciado)

print(y.group())

z = re.search(r'Al(.*)e',enunciado)

print(z.group())

#Remoção de marcas no texto:


k = re.sub(r'{.*?}',"",enunciado)

print(k)






