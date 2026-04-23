#Gráfica de pastel
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15,1,2,3,4,5])
frutas = ["Apples", "Bananas", "Cherries", "Dates","A","B","C","D","E"]

plt.pie(y, labels = frutas)
plt.show() 
