#Novos padrões de expressões regulares:

import re

texto = "1282809xyz8hjj"

letragem = re.sub(r'[0-9]*', 'D', texto)

print(letragem)

#Os dígitos não irão aparecer na divisão de palavras!


novas_letras = re.split(r'[0-9]*',texto)

print(novas_letras)


