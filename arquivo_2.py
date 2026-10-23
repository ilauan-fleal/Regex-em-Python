#O método findall irá retornar uma lista com todas as ocorrências de acordo com o padrão especificado pela Regex.
import re

y = "Expressões regulares em Python"


resultado = re.findall(r'[a-zA-Z0-9_]*',y)

print(resultado)