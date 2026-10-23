#Encontrando correspondências!

import re

x = "email_hipotetico@example.com"

z = re.search(r'[a-zA-Z0-9_]*[\][a-z].*',x)

print(z.group())

print('\n\n')

k = re.findall(r'[a-zA-Z0-9_]+',x)

print(k)
