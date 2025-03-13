import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Criar a figura e os eixos 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Definir intervalos para y e calcular z
y = np.linspace(0, 3, 50)  # Apenas valores positivos (1º quadrante)
x = np.linspace(0, 2, 50)  # Apenas valores positivos (1º quadrante)
Y, X = np.meshgrid(y, x)
Z = 9 - Y**2  # Superfície parabólica

# Plotar a superfície parabólica
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')

# Criar o plano vertical em x=2
y_plane = np.linspace(0, 3, 10)
z_plane = np.linspace(0, 9, 10)
Yp, Zp = np.meshgrid(y_plane, z_plane)
Xp = np.full_like(Yp, 2)  # x = 2 fixo

ax.plot_surface(Xp, Yp, Zp, color='red', alpha=0.3)  # Plano vertical vermelho

# Criar a base do sólido (plano no chão z=0)
X_base, Y_base = np.meshgrid(np.linspace(0, 2, 10), np.linspace(0, 3, 10))
Z_base = np.zeros_like(X_base)
ax.plot_surface(X_base, Y_base, Z_base, color='gray', alpha=0.3)  # Base do sólido

# Criar a face lateral do sólido (plano no eixo y=0)
X_side, Z_side = np.meshgrid(np.linspace(0, 2, 10), np.linspace(0, 9, 10))
Y_side = np.zeros_like(X_side)
ax.plot_surface(X_side, Y_side, Z_side, color='blue', alpha=0.3)  # Face azul

# Configurar rótulos e título
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Sólido no 1º Octante: z = 9 - y², x = 2')

# Ajustar limites dos eixos
ax.set_xlim(0, 2)
ax.set_ylim(0, 3)
ax.set_zlim(0, 10)

# Melhor ângulo de visualização
ax.view_init(elev=25, azim=220)

# Mostrar o gráfico
plt.show()
