# Figure 65

import matplotlib.pyplot as plt
import numpy as np

# Data from previous calculations
entropy_density_chajar = 4.5863672699599516e+73  # J/K/m^3
surface_entropy_density = 6.395122638568381e+44  # J/K/m^2

# Prepare data for plotting
labels = ['Volumetric (Chajar)', 'Surface (Horizon)']
values = [entropy_density_chajar, surface_entropy_density]
log_values = np.log10(values)

# Plot
plt.figure(figsize=(8, 6))
bars = plt.bar(labels, log_values, color=['blue', 'red'])
plt.ylabel('log10(Entropy Density) [J/K/m^x]')
plt.title('Entropy Density: Volume vs Surface Encoding')

# Annotate bars with actual exponent values
for bar, val in zip(bars, values):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2,
             f"10^{int(np.log10(val))}", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.show()
