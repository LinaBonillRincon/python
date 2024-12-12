import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definir los puntos para etiquetar los octantes
# Definir los vértices de los cubos que representan los octantes inferiores
def plot_octant(ax, xsign, ysign, zsign, color):
    xx, yy = np.meshgrid([0, xsign], [0, ysign])
    ax.plot_surface(xx, yy, zsign, color=color, alpha=0.5, rstride=1, cstride=1)
    ax.plot_surface(xx, yy, 0, color=color, alpha=0.5, rstride=1, cstride=1)

# Colores para cada octante
colors = ['red', 'blue', 'green', 'yellow']

# Plotear los octantes inferiores
plot_octant(ax, 1, 1, -1, colors[0])   # Quinto octante
plot_octant(ax, -1, 1, -1, colors[1])  # Sexto octante
plot_octant(ax, -1, -1, -1, colors[2]) # Séptimo octante
plot_octant(ax, 1, -1, -1, colors[3])  # Octavo octante

labels = [
    (1, 1, -1),    # Quinto octante: x > 0, y > 0, z < 0
    (-1, 1, -1),   # Sexto octante: x < 0, y > 0, z < 0
    (-1, -1, -1),  # Séptimo octante: x < 0, y < 0, z < 0
    (1, -1, -1)  
]

# Etiquetas de los octantes
octant_names = [
    "Octante 5 (X, Y, -Z)", "Octante 6 (-X, Y, -Z)", "Octante 7 (-X, -Y, -Z)", "Octante 8 (X, -Y, -Z)"
]

# Plotear cada etiqueta en su posición correspondiente
for i, label in enumerate(labels):
    ax.text(label[0], label[1], label[2], octant_names[i], color='red')

# Establecer los límites del gráfico
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar los planos coordenados
ax.plot([0, 0], [0, 0], [-1.5, 1.5], color='black')  # Eje Z
ax.plot([0, 0], [-1.5, 1.5], [0, 0], color='black')  # Eje Y
ax.plot([-1.5, 1.5], [0, 0], [0, 0], color='black')  # Eje X
ax.view_init(elev=-20, azim=30)
# Mostrar la gráfica
plt.show()
