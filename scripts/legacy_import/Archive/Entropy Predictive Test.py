import numpy as np
import matplotlib.pyplot as plt

# Define cosmic time in billions of years
cosmic_time = np.array([0.38, 1, 5, 10, 13.8])  # Big Bang to present

# Define entropy values from previous model validation (arbitrary scaling)
entropy_values = np.array([1e-36, 5e-30, 1e-25, 1e-23, 1e-23])

# Define another cosmological parameter for correlation (e.g., structure formation scale factor)
structure_formation = np.array([1e-5, 1e-4, 5e-3, 0.1, 1.0])  # Hypothetical scaling of structure growth

# Create the figure
plt.figure(figsize=(8, 5))

# Plot entropy vs. cosmic time
plt.plot(cosmic_time, entropy_values, marker='o', linestyle='-', color='b', label="Entropy Scaling")

# Plot structure formation growth for correlation
plt.plot(cosmic_time, structure_formation, marker='s', linestyle='--', color='r', label="Structure Formation Scaling")

# Apply logarithmic scale for better comparison
plt.yscale('log')

# Labels and title
plt.xlabel("Cosmic Time (Billion Years)")
plt.ylabel("Value (Log Scale)")
plt.title("Entropy Scaling vs. Structure Formation Over Cosmic Time")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
