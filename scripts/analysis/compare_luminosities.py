import pandas as pd
import matplotlib.pyplot as plt

def load_clean_dat_file(filepath):
    df = pd.read_csv(filepath, sep=r"\s+", header=None, comment="#")
    return df

# 💡 Add these lines
file_15 = "data/raw/totalLuminosity_15SolarMass.dat"
file_30 = "data/raw/totalLuminosity_30SolarMass.dat"

df_15_clean = load_clean_dat_file(file_15)
df_30_clean = load_clean_dat_file(file_30)

# ... analysis continues here ...

# Helper to clean and load the file
def load_clean_dat_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Keep only lines that contain only numeric tokens (after splitting)
    clean_lines = [line for line in lines if all(tok.replace('.', '', 1).replace('e', '', 1).replace('+', '', 1).replace('-', '', 1).isdigit() for tok in line.strip().split()[:2])]
    
    # Save cleaned to a temporary file
    cleaned_path = filepath + "_cleaned.dat"
    with open(cleaned_path, 'w') as f:
        f.writelines(clean_lines)

    # Try loading the cleaned file
    df = pd.read_csv(cleaned_path, sep=r"\s+", header=None)
    return df

# Clean and load both files
df_15_clean = load_clean_dat_file(file_15)
df_30_clean = load_clean_dat_file(file_30)

# Assign generic column names based on number of columns
num_cols = df_15_clean.shape[1]
column_names = [f"Col_{i}" for i in range(num_cols)]
df_15_clean.columns = df_30_clean.columns = column_names

# Add source label
df_15_clean["Mass"] = "15Msun"
df_30_clean["Mass"] = "30Msun"

# Combine for comparison
df_combined_clean = pd.concat([df_15_clean, df_30_clean], ignore_index=True)

import matplotlib.pyplot as plt

# After processing:
plt.plot(df_15_clean.iloc[:, 0], df_15_clean.iloc[:, 1], label='15 Solar Mass')
plt.plot(df_30_clean.iloc[:, 0], df_30_clean.iloc[:, 1], label='30 Solar Mass')

plt.xlabel("Time")
plt.ylabel("Luminosity")
plt.title("Luminosity Comparison")
plt.legend()
plt.show()
# Display first few rows of each cleaned dataset
print("=== 15 Solar Mass Star Luminosity Data ===")
print(df_15_clean.head(10))
print("\n=== 30 Solar Mass Star Luminosity Data ===")
print(df_30_clean.head(10))

#import ace_tools as tools; tools.display_dataframe_to_user(name="Cleaned Supernova Luminosity Data", dataframe=df_combined_clean.head(100))
print("✅ Luminosity comparison complete.")
from IPython.display import display

display(df_15_clean.head(10))
display(df_30_clean.head(10))
