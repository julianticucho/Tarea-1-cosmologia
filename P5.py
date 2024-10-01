import camb
import numpy as np
import matplotlib.pyplot as plt

pars = camb.set_params(H0=67.4, w=-0.1, cs2=0.1)
results = camb.get_results(pars)
z = np.linspace(0, 5000, 100)

Omega_m = results.get_Omega('cdm', z) + results.get_Omega('baryon', z)   
Omega_r = results.get_Omega('photon', z) + results.get_Omega('neutrino', z)  
Omega_de = results.get_Omega('de', z)  
Omega_k = results.get_Omega('K', z)    

plt.figure(figsize=(6, 4))
plt.plot(z, Omega_m, label=r'$\Omega_m$', color='b')
plt.plot(z, Omega_r, label=r'$\Omega_r$', color='g')
plt.plot(z, Omega_de, label=r'$\Omega_\Lambda$', color='r')
plt.plot(z, Omega_k, label=r'$\Omega_k$', color='k', linestyle='--')
plt.gca().invert_xaxis()

plt.xlabel(r'Redshift $z$', fontsize=16)
plt.ylabel(r'$\Omega_{s}$', fontsize=16)
plt.legend(loc='best', fontsize=8)
plt.show()
