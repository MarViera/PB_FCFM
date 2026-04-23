# Fuerza de atracción gravitacional

import matplotlib.pyplot as plt
# Draw the graph
def draw_graph(x, y):
    plt.plot(x, y, marker='*')
    plt.xlabel('Distancia [m]')
    plt.ylabel('Fuerza gravitacional [N]')
    plt.title('Relación entre la fuerza gravitacional y la distancia')
    plt.show()

#Datos
# Constante, G
G = 6.674e-11
# Masas
m1 = 0.5
m2 = 1.5

#Creamos la lista de valores sobre los que se variará la distancia
r = range(100, 1001, 50)
#Creamos la lista de valores de la fuerza
F = list()
for dist in r:  #obs: Calculamos la fuerza en cada uno de los valores de la lista de distancias (r). usamos un etiqueta (force) para referirse a la fuerza calculada y agregarla a la lista (F).
    force = G*(m1*m2)/(dist**2)
    F.append(force)

draw_graph(r, F)
