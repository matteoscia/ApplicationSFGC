#Con list comprehension (versione ridotta)
def squarelista(lista):
    lista_quadratipari=[x**2 for x in lista if x**2%2==0] #qui si può mettere anche if x%2==0 per semplificare,quadrati di pari e di dispari rimangono sempre pari e dispari
    return lista_quadratipari


#Senza list comprehension (versione estesa)
def squarelista2(lista):
    lista_quadratipari=[]
    for x in lista:
        y=x**2
        if y%2==0:#idem qui: funziona anche x%2==0
            lista_quadratipari.append(y)
    return lista_quadratipari

l1=[1,2,3,4,5,6]

print(squarelista(l1))
print(squarelista2(l1))
