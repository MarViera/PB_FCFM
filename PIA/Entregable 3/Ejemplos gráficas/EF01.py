import matplotlib.pyplot as plt
import numpy as np

y = np.array([25, 100, 150, 125, 200, 100])
carreras = ['LM','LF','LCC','LA', 'LMAD', 'LSTI']
colores = ['red', 'green', 'yellow', 'magenta', 'cyan', 'red']
plt.pie(y, labels = carreras, colors = colores)
plt.legend(title = 'Ingresos FCFM')
plt.show()


    
        
    
