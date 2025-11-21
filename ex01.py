qualificacions = [8.8, 9.5, 7.0, 10.0, 9.3, 8.5, 7.4, 9.9, 9.2, 7.8] # LLista amb les qualificacions
n = len(qualificacions) # La longitud de la llista
canvi = True # Indica si hi ha hagut canvis o no
while canvi: # Bucle while que no finalitza fins que "canvi" sigue "false"
    canvi = False # cania "canvi" a "false" per iniciar el bucle
    for i in range(n - 1): # comprova cada element de la llista
        if qualificacions[i] > qualificacions[i+1]: # si el primer element és major que el segon
            qualificacions[i], qualificacions[i+1] = qualificacions[i+1], qualificacions[i] # intercambia els dos
        canvi = True # canvia el valor de "canvi" a "true"
    n -= 1 # redueix la longitud de la llista
print("Qualificacions ordenades:") 
print(qualificacions)