llibres = [
    ["A Tale of Two Cities", "Charles Dickens"],
    ["Catcher in the Rye", "J.D. Salinger"],
    ["Don Quixote", "Miguel de Cervantes"],
    ["Harry Potter", "J.K. Rowling"],
    ["Moby Dick", "Herman Melville"],
    ["The Great Gatsby", "F. Scott Fitzgerald"],
    ["War and Peace", "Leo Tolstoy"]
]

trobat = False # Indica si s'ha trobat el llibre
inf = 0 # Primer element de la llista
sup = len(llibres) - 1 # Últim element de la llista
cerca = ["Moby Dick", "Herman Melville"] # Llista amb el nom i el autor del llibre que s'ha de trobar
while (inf <= sup) and (not trobat): # Bucle while que no finalitza fins que "trobat" sigui "true" o "inf" i "sup" siguin iguals
    mig = inf + (sup - inf) // 2 # Mida entre "inf" i "sup"
    if cerca[0] == llibres[mig][0]: # Si el nom del llibre és igual al cercat
        trobat = True # Marca que s'ha trobat el llibre
    else:
        if cerca[0] < llibres[mig][0]: # Si el nom del llibre és menor que el cercat
            sup = mig - 1 # Mida de la llista redueix de 1 per mitjà
        else:
            inf = mig + 1 # Mida de la llista incrementa de 1 per mitjà
if trobat: # Si s'ha trobat el llibre
    print("Llibre trobat:")
    print(llibres[mig]) # Imprimeix el llibre trobat
else:
    print("Llibre no trobat") # Si no s'ha trobat el llibre
    