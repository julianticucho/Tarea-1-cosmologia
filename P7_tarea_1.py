import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from matplotlib import cm

c = 3e5  
H0 = 67.5  

def E(z, Omega_m, Omega_Lambda):
    Omega_k = 1 - Omega_m - Omega_Lambda
    return np.sqrt(Omega_m * (1 + z)**3 + Omega_k * (1 + z)**2 + Omega_Lambda)

def fK_Omega_k_pos(z, Omega_k, Omega_m, Omega_Lambda):
    integral, _ = quad(lambda x: 1/E(x, Omega_m, Omega_Lambda), 0, z)
    return (c / (H0 * np.sqrt(Omega_k))) * np.sinh(np.sqrt(Omega_k) * integral)

def fK_Omega_k_0(z, Omega_m, Omega_Lambda):
    integral, _ = quad(lambda x: 1/E(x, Omega_m, Omega_Lambda), 0, z)
    return (c / H0) * integral

def fK_Omega_k_neg(z, Omega_k, Omega_m, Omega_Lambda):
    integral, _ = quad(lambda x: 1/E(x, Omega_m, Omega_Lambda), 0, z)
    return (c / (H0 * np.sqrt(-Omega_k))) * np.sin(np.sqrt(-Omega_k) * integral)

z_values = [0.001, 0.9, 4, 9, 17, 29, 47, 72, 1100]
Omega_m_values = np.linspace(0, 3, 100)
Omega_Lambda_values = np.linspace(0, 3, 100)
Omega_m_grid, Omega_Lambda_grid = np.meshgrid(Omega_m_values, Omega_Lambda_values)

cmap = cm.PRGn
fig, axs = plt.subplots(3, 3, figsize=(10, 10))
fig.subplots_adjust(hspace=0.3)

for k, z in enumerate(z_values):
    i = k // 3
    j = k % 3
    fK_grid = np.zeros_like(Omega_m_grid)

    for x in range(Omega_m_grid.shape[0]):
        for y in range(Omega_m_grid.shape[1]):
            Omega_m = Omega_m_grid[x, y]
            Omega_Lambda = Omega_Lambda_grid[x, y]
            Omega_k = 1 - Omega_m - Omega_Lambda
            
            if Omega_k > 0:
                fK_grid[x, y] = fK_Omega_k_pos(z, Omega_k, Omega_m, Omega_Lambda)
            elif Omega_k == 0:
                fK_grid[x, y] = fK_Omega_k_0(z, Omega_m, Omega_Lambda)
            else:
                fK_grid[x, y] = fK_Omega_k_neg(z, Omega_k, Omega_m, Omega_Lambda)

    ax = axs[i, j]
    cset1 = ax.contourf(Omega_m_grid, Omega_Lambda_grid, fK_grid, levels=50, cmap=cmap, alpha=0.9)
    cset2 = ax.contour(Omega_m_grid, Omega_Lambda_grid, fK_grid, levels=cset1.levels, colors='k')
    cset2.set_linestyle('solid')
    ax.set_title(f'z = {z}')
    ax.set_xlabel(r'$\Omega_{m,0}$')
    ax.set_ylabel(r'$\Omega_{\Lambda,0}$')

plt.tight_layout()
plt.show()
