import re

#Exemplo de modificação de string

#Substituição de zero ou mais caracteres, nos quais não são considerados dígitos  por :!


texto = "f28fjsnq98223ij"



nova_string = re.sub(r'\D*', ":", texto)


print(nova_string)

