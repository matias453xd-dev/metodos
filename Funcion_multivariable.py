import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función f(x, y) = x^2 + y^2
def f(x, y):
    return x**2 + y**2

# Crear los datos para la gráfica
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Crear la figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Etiquetas de los ejes
ax.set_title('Gráfica de $f(x, y) = x^2 + y^2$', fontsize=14)
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_zlabel('$f(x, y)$', fontsize=12)

plt.show()
