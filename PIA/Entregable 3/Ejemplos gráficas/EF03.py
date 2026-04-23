import matplotlib.pyplot as plt
import numpy as np

y = np.array([25, 100, 150, 125, 200, 100])
x = np.array(['LM','LF','LCC','LA', 'LMAD', 'LSTI'])
colores = ['red', 'green', 'yellow', 'magenta', 'cyan', 'red']
plt.plot(x,y, '-*')
plt.grid()
plt.title('Nuevo ingresos FCFM')
plt.xlabel('Carreras')
plt.ylabel('Estudiantes')
plt.axis(ymin=0, ymax=210)
plt.show()


    
        
    
