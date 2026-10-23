#Utilizando classes já definidas em Python!

import re

texto = "Estudo de códigos e programação"


resultado = re.search(r'(\w*)progr(\w*)', texto)


print(resultado.group())

#Posicionamento da string



print(resultado.span())


novo_texto = "Codificação para estudo e conhecimento"

#\w = [a-za-Z0-9] -> Caractere alfanumérico

print('\n')

j = re.search(r'\w*$', novo_texto)

print(j.group())


