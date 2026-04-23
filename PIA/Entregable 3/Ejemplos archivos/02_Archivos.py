#Leemos
fo = open("01HolaMundo.txt","r") #nombre del archivo puede ser una variable
#fo tendrá una línea por cada línea del archivo
print(fo)
for line in fo:
    print(line,end='')
fo.close()
