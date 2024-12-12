import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Función para crear un cubo en un octante específico
def plot_octant(ax, xsign, ysign, zsign, color):
    # Vértices del cubo
    vertices = [
        [0, 0, 0],
        [xsign, 0, 0],
        [xsign, ysign, 0],
        [0, ysign, 0],
        [0, 0, zsign],
        [xsign, 0, zsign],
        [xsign, ysign, zsign],
        [0, ysign, zsign]
    ]
    
    # Crear las 6 caras del cubo
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Cara en el plano XY (parte inferior)
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # Cara en el plano YZ (frontal)
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Cara en el plano ZX (lateral derecha)
        [vertices[3], vertices[0], vertices[4], vertices[7]],  # Cara en el plano YZ (trasera)
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Cara en el plano XY (parte superior)
        [vertices[4], vertices[5], vertices[6], vertices[7]]   # Cara en el plano ZX (lateral izquierda)
    ]
    
    # Crear una colección de polígonos y añadirla al gráfico
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='black', alpha=0.5))

# Colores para cada octante
colors = ['red', 'blue', 'green', 'yellow']

# Plotear los octantes inferiores
plot_octant(ax, 1, 1, -1, colors[0])   # Quinto octante
plot_octant(ax, -1, 1, -1, colors[1])  # Sexto octante
plot_octant(ax, -1, -1, -1, colors[2]) # Séptimo octante
plot_octant(ax, 1, -1, -1, colors[3])  # Octavo octante


labels = [
    (2, 2, -2),    # Quinto octante: x > 0, y > 0, z < 0
    (-1.1, 1.1, -1.1),   # Sexto octante: x < 0, y > 0, z < 0
    (-1.1, -1.1, -1.1),  # Séptimo octante: x < 0, y < 0, z < 0
    (2, -2, -2) 
]

# Etiquetas de los octantes
octant_names = [
    "Octante 5 (X, Y, -Z)", "Octante 6 (-X, Y, -Z)", "Octante 7 (-X, -Y, -Z)", "Octante 8 (X, -Y, -Z)"
]

# Plotear cada etiqueta en su posición correspondiente
for i, label in enumerate(labels):
    ax.text(label[0], label[1], label[2], octant_names[i], color='black', fontweight='bold')


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

# Ajustar la vista para enfocar en la parte inferior
ax.view_init(elev=-30, azim=30)

# Mostrar la gráfica
plt.show()
