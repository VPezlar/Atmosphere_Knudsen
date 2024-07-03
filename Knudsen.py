# Atmospheric model
import ussa1976

# Miscellaneous
import numpy as np
from matplotlib import pyplot as plt

# Distance between particle centers
d = 1*10**(-10)
# Reference Length (Nose radius)
L = 0.005

# Max Altitude
H = 100000  # [m]

# Assumed limit of computational resources between continuum and DSMC calculations
K_lim = 0.004

# Atmospheric profile from 0 to H
ds = ussa1976.compute(z=np.arange(0.0, H, 1.0))

# Extracting number density
n = ds["n_tot"].values
# Calculating mean-free-path
MFP = 1/(np.sqrt(2) * np.pi * d**2 * n)
# Calculating Knudsen Number based on d and L
K = np.array(MFP / L)

# Plotting
plt.semilogy(np.arange(0.0, H, 1.0)/1000, K)
plt.axhline(K_lim, linestyle='--')
plt.xlabel("Altitude [km]")
plt.ylabel("Knudsen Number")
plt.show()
