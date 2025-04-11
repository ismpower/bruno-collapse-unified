import pandas as pd

# Updated loader with proper separator and header
df = pd.read_csv("data/raw/IceCube_Gold_Bronze_Events.csv")
print("Detected columns:", df.columns.tolist())
print(df.head(3))  # Optional: shows first few rows




# Print actual column names to verify
print("Detected columns:", df.columns.tolist())

# Try matching best-guess column names
for col in df.columns:
    print(col)

# Optionally, rename them (only once you've confirmed them)
df = df.rename(columns={
    'RA': 'ra',
    'RA.1': 'ra',
    'Dec': 'dec',
    'Dec.1': 'dec',
    'Date': 'date',
    'Time': 'time',
    'Energy': 'energy',
    'Signalness': 'signalness'
})

# If you find 'Date' and 'Time', build event_time
if 'date' in df.columns and 'time' in df.columns:
    df["event_time"] = df["date"] + " " + df["time"]
    print(df[['ra', 'dec', 'event_time']].head())

print("Detected columns:", df.columns.tolist())
print(df.head(3))
