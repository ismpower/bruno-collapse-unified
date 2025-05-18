import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Load the dataset from specified absolute path
file_path = "D:/entropy-research-library/entropy-hypothesis/data/hlsp_rslss_roman_wfi_multi_wfc_v1_sim-ultradeep-mocks.txt"
df = pd.read_csv(file_path, sep='\\s+')  # Updated syntax for whitespace-delimited file

# Define a simple entropy-like saturation model (logistic function)
def entropy_saturation(x, L, x0, k):
    return L / (1 + np.exp(-k * (x - x0)))

# We'll use the redshift of the lens (ZLENS) vs the delay (first value in DELAY)
parsed_data = []
for i, row in df.iterrows():
    try:
        delay_str = row['DELAY'].split(',')[0]
        delay_val = float(delay_str)
        parsed_data.append((row['ZLENS'], delay_val))
    except:
        continue

parsed_df = pd.DataFrame(parsed_data, columns=['ZLENS', 'DELAY'])

# Fit the entropy saturation model to the data
x_data = parsed_df['ZLENS'].values
y_data = parsed_df['DELAY'].values

initial_guess = [max(y_data), np.median(x_data), 10]
popt, pcov = curve_fit(entropy_saturation, x_data, y_data, p0=initial_guess)

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Real Data', alpha=0.4)
plt.plot(np.sort(x_data), entropy_saturation(np.sort(x_data), *popt), color='red', label='Entropy Saturation Fit')
plt.xlabel('ZLENS (Lens Redshift)')
plt.ylabel('DELAY (Time Delay)')
plt.title('Entropy Saturation Model Fit to Time Delay vs Lens Redshift')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
