import matplotlib.pyplot as plt
import numpy as np

y = np.array([25, 100, 150, 125, 200, 100])
x = np.array(['LM','LF','LCC','LA', 'LMAD', 'LSTI'])
colores = ['red', 'green', 'yellow', 'magenta', 'cyan', 'red']
plt.bar(x,y, color = colores)
plt.grid()
plt.title('Ingresos FCFM')
plt.show()


    
        
    
