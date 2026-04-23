#Leemos de una forma más "sencilla"
with open ("01HolaMundo.txt","r") as file: #file = fo
    for line in file:
        print(line,end='')
print("Se acabo")
print(file)
