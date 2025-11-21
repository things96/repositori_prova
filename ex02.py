participants = [
    ["Joan", 22],
    ["Maria", 45],
    ["Carlos", 38],
    ["Anna", 19],
    ["Pere", 56],
    ["Laura", 24],
    ["Enric", 12],
    ["Sònia", 27],
    ["David", 31],
    ["Elena", 18],
    ["Ricard", 42]
]

n = len(participants) # Longitud de la llista
canvi = True # Indica si hi ha hagut canvis o no
while canvi: # Bucle while que no finalitza fins que "canvi" sigui "false"
    canvi = False # Canviem "canvi" a "false" per iniciar el bucle
    for i in range(n - 1): # Comprova cada element de la llista
        if participants[i][1] > participants[i+1][1]: # Si el primer element és major que el segon
            participants[i], participants[i+1] = participants[i+1], participants[i] # intercambia els dos
            canvi = True # canvia el valor de "canvi" a "true"
    n -= 1 # redueix la longitud de la llista
print("Llista ordenada:")
print(participants) 