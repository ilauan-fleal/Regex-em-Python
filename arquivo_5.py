#Identificando formato de datas

import re

data = "01/02/1989"



y = re.search(r'([0-9]*.){3}', data)

print(y.group())


#Modificando a string

z = re.sub(r'([0-9]*.){3}','19/08/2000',data)

print(z)

