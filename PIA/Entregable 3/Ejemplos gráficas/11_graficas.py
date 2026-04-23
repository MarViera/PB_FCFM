from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
p = plot(2*x + 3, (x, -5, 5),
     title='Función lineal',
     xlabel='x',
     ylabel='2x+3',
     show=True)
#p.show()

