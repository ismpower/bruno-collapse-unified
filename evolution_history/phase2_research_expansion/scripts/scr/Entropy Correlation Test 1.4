# Re-run the comparison script after state reset
# Figure 57

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Load the dataset
file_path = "D:/entropy-research-library/entropy-hypothesis/Data/hlsp_rslss_roman_wfi_multi_wfc_v1_sim-ultradeep-mocks.txt"
df = pd.read_csv(file_path, sep=r'\s+')

# Parse delay values
parsed_data = []
for i, row in df.iterrows():
    try:
        delay_str = row['DELAY'].split(',')[0]
        delay_val = float(delay_str)
        parsed_data.append((row['ZLENS'], delay_val))
    except:
        continue

parsed_df = pd.DataFrame(parsed_data, columns=['ZLENS', 'DELAY'])

# Prepare data
x_data = parsed_df['ZLENS'].values
y_data = parsed_df['DELAY'].values

# Define logistic entropy saturation function
def logistic(z, L, k, z0):
    return L / (1 + np.exp(-k * (z - z0)))

# Fit model
initial_guess = [max(y_data), 4.8, 0.61]
popt_fitted, _ = curve_fit(logistic, x_data, y_data, p0=initial_guess)

# Fixed model from Figure 55
popt_fixed = [45.3, 4.8, 0.61]

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Real Data', alpha=0.4)
plt.plot(np.sort(x_data), logistic(np.sort(x_data), *popt_fitted), color='blue', label='Fitted Saturation Model')
plt.plot(np.sort(x_data), logistic(np.sort(x_data), *popt_fixed), color='red', linestyle='--', label='Fixed Model (Figure 55)')
plt.xlabel('ZLENS (Lens Redshift)')
plt.ylabel('DELAY (Time Delay)')
plt.title('Comparison: Fitted vs Fixed Entropy Saturation Curve')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Return fitted parameters
popt_fitted
