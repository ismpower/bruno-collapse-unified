# Entropy Horizon Table Generator
# Produces a list of (k, tau_horizon) values for analysis or paper inclusion

import numpy as np
import pandas as pd
from sympy import symbols, ln

# Define constants
S_inf = 1.0
S_target = 0.999 * S_inf

# Inverted entropy saturation formula
def tau_horizon(k, S_target=S_target, S_inf=S_inf):
    if k <= 0 or S_target >= S_inf:
        return np.nan
    return -np.log(1 - S_target / S_inf) / k

# Sample k values
k_values = np.linspace(0.001, 0.1, 25)
tau_results = [tau_horizon(k) for k in k_values]

# Create DataFrame
data = {
    "k (decay constant)": k_values,
    "τ_horizon (where S ≈ 0.999)": tau_results
}
df = pd.DataFrame(data)

# Display
#import ace_tools as tools
#tools.display_dataframe_to_user(name="Entropy Horizon Table", dataframe=df)

# Display result in terminal instead of ace_tools
print(df.to_string(index=False))

# Optional: Save to CSV for export
df.to_csv("D:/entropy-research-library/entropy-hypothesis/scr/entropy_horizon_table.csv", index=False)

