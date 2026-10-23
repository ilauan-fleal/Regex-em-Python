#Expressões regulares
import re

#Search irá retornar a primeira ocorrência da substring, de acordo com o padrão especificado.

#No caso a string inteira será retornada!

x = "Linguagem regular"

resultado = re.search(r'[a-zA-Z0-9_]*[ \t][a-zA-Z0-9_]*', x)

print(resultado.group())
