import re

#Referenciando grupos dentro da própria expressão regular para construir padrões mais complexos

repeticao = "AAABBBCCCDDDEEEFFFGGGHHHKJKJKJKJKJKJKJKJ"

y = re.search(r'([KJ]{8})(.*)\1',repeticao)

print(y.group())


z  = re.sub(r'([KJ]{8})(.*)\1', r'\2', repeticao)

print(z)






