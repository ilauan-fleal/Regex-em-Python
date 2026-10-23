import re

#Trabalhando novamente com padrões de data


data = "18/09/1987"


formato =  r'(\d{2})/(\d{2})/(\d{4})'

novo_formato = r'\1-\2-\3'


data_formatada = re.sub(formato,novo_formato,data)

print(data_formatada)

outro_formato = r'\3/\2/\1'

nova_data_formatada  = re.sub(formato,outro_formato,data)

print(nova_data_formatada)