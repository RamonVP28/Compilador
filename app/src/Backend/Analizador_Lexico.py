import numpy as np

TableTokens = {}

def setTableTokens(type, value):
    TableTokens[type] = value

#Analizador lexico
def AnalizadorLexico():
    array = []
    count = 0
    for typo, Nombre in TableTokens.items(): 
        count += 1	
        array.append([count, typo, Nombre])
    array = np.array(array)
    return array
