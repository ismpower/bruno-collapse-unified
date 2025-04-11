import pandas as pd

# Load the extracted ASASSN dataset
df = pd.read_csv("/mnt/data/asassn_extracted_bruno_ready.csv")

# Preview and basic info
df_info = df.info()
df_preview = df.head(10)

# Basic statistics for fluence
fluence_stats = df["Fluence (J/m²)"].describe()

# Count how many events are above Bruno threshold (e.g., 1e-5 J/m²)
above_threshold_count = (df["Fluence (J/m²)"] > 1e-5).sum()

# Total number of usable events (not NaN)
total_valid_fluence = df["Fluence (J/m²)"].notna().sum()

# Return summary
df_info, df_preview, fluence_stats, above_threshold_count, total_valid_fluence
