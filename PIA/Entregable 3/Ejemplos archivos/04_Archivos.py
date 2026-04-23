import random

numeros = list()
for i in range(10):
    numeros.append(random.randint(1,100))

fo = open("Evaluaciones.txt","a")
print(numeros)
#Como guardamos cada elemento de la lista en un archivo
for calificacion in numeros:
    fo.write(str(calificacion)+'\n')

#for i in range(len(numeros)): 
#    fo.write(str(numeros[i])+'\n')
fo.close()

