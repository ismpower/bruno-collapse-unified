import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Constants
kappa = 1366  # Bruno Constant in K^-1

# Test Cases: Name, Radius (m), Temperature (K)
systems = [
    ("GW150914 Black Hole", 1.83e5, 1.2e-8),
    ("Neutron Star", 1.2e4, 1e6),
    ("White Dwarf", 7e6, 1e5),
    ("CMB Epoch", 4.3e26, 3000),
    ("Primordial BH", 1e-15, 1e23)
]

# Compute beta_B and 3/R
data = []
for name, R, T in systems:
    beta_B = kappa * T
    boundary = 3 / R
    status = "Surface Collapse" if beta_B >= boundary else "Volumetric"
    data.append((name, R, T, beta_B, boundary, status))

# Convert to DataFrame
df = pd.DataFrame(data, columns=["System", "Radius (m)", "Temperature (K)", "β_B = κ·T", "3/R", "Collapse Regime"])

# Prepare plot
T_vals = np.logspace(-10, 25, 500)
R_boundary = 3 / (kappa * T_vals)

plt.figure(figsize=(10, 6))
plt.loglog(T_vals, R_boundary, label="Bruno Collapse Boundary", linewidth=2)

for _, row in df.iterrows():
    plt.scatter(row["Temperature (K)"], row["Radius (m)"], label=row["System"])
    plt.text(row["Temperature (K)"], row["Radius (m)"]*1.5, row["System"], fontsize=9)

plt.xlabel("Temperature (K)")
plt.ylabel("Radius (m)")
plt.title("Bruno Collapse Boundary in Radius–Temperature Space")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Bruno Collapse Test Results", dataframe=df)

####
# Estimate the core temperature of a massive star before it collapsed into the GW150914 black hole
# Typical temperature range at core-collapse (supernova) phase is ~1e9 to 1e10 K
# We'll test two scenarios: T = 1e9 K and T = 1e10 K

# Recompute β_B = κ · T and compare to 3/R for GW150914
R_gw150914 = 1.83e5  # m
kappa = 1366  # K^-1

temperatures = [1e9, 1e10]
results = []

for T in temperatures:
    beta_B = kappa * T
    threshold = 3 / R_gw150914
    status = "Surface Collapse" if beta_B >= threshold else "Volumetric"
    results.append((T, beta_B, threshold, status))

# Create a summary table
pd.DataFrame(results, columns=["Core Temperature (K)", "β_B = κ·T", "3/R", "Collapse Regime"])


####

# Define κ again for clarity
kappa = 1366  # Bruno Constant in K^-1

# Collapse transition stages: Name, Temperature (K), Radius (m)
collapse_stages = [
    ("White Dwarf Core", 1e7, 7e6),
    ("Neutron Star Core", 1e9, 1e4),
    ("Massive Star Pre-BH Core", 1e10, 1e5)
]

# Calculate Bruno Constant values and compare to threshold
transition_results = []
for name, T, R in collapse_stages:
    beta_B = kappa * T
    threshold = 3 / R
    status = "Surface Collapse" if beta_B >= threshold else "Volumetric"
    transition_results.append((name, T, R, beta_B, threshold, status))

# Present results
pd.DataFrame(transition_results, columns=["Stage", "Temperature (K)", "Radius (m)", "β_B = κ·T", "3/R", "Collapse Regime"])

###

# Simulate time-evolution tracks in Radius–Temperature space for three systems:
# White Dwarf → Neutron Star → Black Hole transition

# Define temperature and radius evolution (simplified and idealized)
time_steps = np.linspace(0, 1, 100)  # normalized time (0 = start, 1 = final collapse)

# Define initial and final (T, R) for each object type
tracks = {
    "WD → NS": {
        "T_start": 1e7, "T_end": 1e9,
        "R_start": 7e6, "R_end": 1.2e4
    },
    "NS → BH": {
        "T_start": 1e9, "T_end": 1e10,
        "R_start": 1.2e4, "R_end": 1.83e5
    },
    "Primordial BH (cooling)": {
        "T_start": 1e23, "T_end": 1e16,
        "R_start": 1e-15, "R_end": 1e-12
    }
}

# Generate the Bruno Collapse boundary curve
T_vals = np.logspace(-10, 25, 500)
R_boundary = 3 / (kappa * T_vals)

# Plot setup
plt.figure(figsize=(10, 6))
plt.loglog(T_vals, R_boundary, label="Bruno Collapse Boundary", linewidth=2, linestyle='--')

# Plot each track
for label, params in tracks.items():
    T_track = np.logspace(np.log10(params["T_start"]), np.log10(params["T_end"]), 100)
    R_track = np.logspace(np.log10(params["R_start"]), np.log10(params["R_end"]), 100)
    plt.plot(T_track, R_track, label=label)

plt.xlabel("Temperature (K)")
plt.ylabel("Radius (m)")
plt.title("Entropy Collapse Tracks Across Bruno Boundary")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

####

# Let's begin with SN1987A — the best-documented core-collapse supernova
# We'll estimate β_B for SN1987A based on core parameters prior to collapse

# Known estimated values for SN1987A (core-collapse phase)
T_core_sn1987a = 4e9   # Temperature in Kelvin
R_core_sn1987a = 1.5e4  # Core radius in meters (estimated)

# Bruno Constant
kappa = 1366  # K^-1

# Compute beta_B and threshold
beta_B_sn1987a = kappa * T_core_sn1987a
threshold_sn1987a = 3 / R_core_sn1987a
status = "Surface Collapse" if beta_B_sn1987a >= threshold_sn1987a else "Volumetric"

# Display result
{
    "SN1987A Core Temperature (K)": T_core_sn1987a,
    "SN1987A Core Radius (m)": R_core_sn1987a,
    "β_B = κ·T": beta_B_sn1987a,
    "3/R": threshold_sn1987a,
    "Collapse Regime": status
}

###

# Neutrino physics parameters and escape timing estimate for SN1987A

# Observed neutrino burst time before visible light
neutrino_early_time_sec = 10800  # 3 hours in seconds

# Light travel time across stellar radius (~20 solar masses)
# Approximate total stellar radius (before collapse): ~40 million km = 4e7 km = 4e10 m
R_star = 4e10  # in meters
c = 3e8  # speed of light in m/s

# Time it would take for photons to escape if they could move freely (they can't, but it's a reference)
t_light_escape = R_star / c  # seconds

# Time neutrinos take to escape from a collapsing core (order of seconds to tens of seconds)
# Let's assume they are emitted from near the collapsing core (~10 km), escape immediately after collapse

# Compare that to the time light takes to escape from the surface after shock breakout
# This gives a window between neutrino emission and visible light

{
    "SN1987A Neutrino Burst Lead Time": f"{neutrino_early_time_sec / 3600:.2f} hours",
    "Stellar Radius": f"{R_star:.2e} m",
    "Light Escape Time (free path estimate)": f"{t_light_escape:.2f} seconds"
}

####

# Let's analyze TOV limit vs Bruno Collapse threshold
# The TOV limit gives the maximum mass a neutron star can support against gravitational collapse

# Typical TOV limit range (observational/theoretical range)
TOV_min = 2.1  # in solar masses
TOV_max = 2.3  # in solar masses
solar_mass = 1.98847e30  # kg

# Convert mass to Schwarzschild radius: R_s = 2GM/c^2
G = 6.67430e-11  # gravitational constant
c = 3e8  # speed of light

# Choose a mid-range TOV mass
M_TOV = 2.2 * solar_mass
R_s_TOV = 2 * G * M_TOV / c**2

# Estimate core collapse temperature for NS exceeding TOV limit (~1e10 K)
T_core_TOV = 1e10  # K

# Compute Bruno constant β_B = κ·T and compare to 3/R_s
kappa = 1366
beta_B_TOV = kappa * T_core_TOV
threshold_TOV = 3 / R_s_TOV
collapse_status = "Surface Collapse" if beta_B_TOV >= threshold_TOV else "Volumetric"

{
    "TOV Limit Mass (kg)": M_TOV,
    "Schwarzschild Radius (m)": R_s_TOV,
    "β_B = κ·T": beta_B_TOV,
    "3 / R_s": threshold_TOV,
    "Collapse Regime": collapse_status
}

#

import numpy as np
import matplotlib.pyplot as plt

# Constants
a_rad = 7.5657e-16  # Radiation constant (J·m⁻³·K⁻⁴)
kappa = 1313        # Bruno Constant (1/K)
V = 1.0             # Arbitrary volume (m³)

# Temperature range
T_vals = np.logspace(1, 12, 300)  # from 10 K to 1e12 K

# Entropy calculations
S_3D = (4/3) * a_rad * T_vals**3 * V
S_2D = (4/3) * a_rad * T_vals**2 * V / kappa
ratio_S2D_to_S3D = S_2D / S_3D
beta_B_vals = kappa * T_vals

# Plot entropy values
plt.figure(figsize=(10, 6))
plt.loglog(T_vals, S_3D, label="S_3D (Volumetric Entropy)", color='blue')
plt.loglog(T_vals, S_2D, label="S_2D (Projected Entropy)", color='orange', linestyle='--')
plt.axvline(1/kappa, color='red', linestyle=':', label="Collapse Threshold (β_B = 1)")
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy (J/K)")
plt.title("3D vs Projected 2D Entropy Across Temperature")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.tight_layout()
plt.show()

# Plot entropy ratio
plt.figure(figsize=(10, 6))
plt.semilogx(T_vals, ratio_S2D_to_S3D, label="S_2D / S_3D", color='purple')
plt.axhline(1, color='gray', linestyle='--', label="Equality Line (β_B = 1)")
plt.axvline(1/kappa, color='red', linestyle=':', label="Collapse Threshold (1/κ)")
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy Ratio (S_2D / S_3D)")
plt.title("Entropy Ratio vs Temperature")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.tight_layout()
plt.show()

#

# First, calculate κ from first principles using Planck units
import math

# Physical constants (SI)
hbar = 1.054571817e-34     # Reduced Planck constant (J·s)
G = 6.67430e-11            # Gravitational constant (m³/kg/s²)
c = 299792458              # Speed of light (m/s)
k_B = 1.380649e-23         # Boltzmann constant (J/K)

# Planck length and temperature
l_P = math.sqrt(hbar * G / c**3)              # meters
T_P = math.sqrt(hbar * c**5 / G) / k_B        # Kelvin

# κ from Planck units
kappa_planck = 3 / (l_P * T_P)

# Now calculate κ empirically from GW150914 black hole data:
# Hawking temperature for GW150914
T_H_GW150914 = 1.2e-8     # Kelvin (estimated)
R_GW150914 = 1.83e5       # meters (Schwarzschild radius)

# From Bruno collapse condition: β_B = A/V = 3/R = κ * T → κ = 3 / (R * T)
kappa_gw150914 = 3 / (R_GW150914 * T_H_GW150914)

{
    "κ from Planck Units": kappa_planck,
    "κ from GW150914 Backsolve": kappa_gw150914,
    "Percent Difference (%)": abs(kappa_planck - kappa_gw150914) / ((kappa_planck + kappa_gw150914)/2) * 100
}

###

# Temperature range
T_vals = np.logspace(1, 12, 300)  # 10 K to 1e12 K

# Constants
a_rad = 7.5657e-16  # Radiation constant (J·m⁻³·K⁻⁴)
kappa = 1313        # Bruno constant
V = 1.0             # Volume in m³

# Internal energy (same for both models)
U = a_rad * T_vals**4 * V

# Entropy models
S_3D = (4/3) * a_rad * T_vals**3 * V
S_2D = (4/3) * a_rad * T_vals**2 * V / kappa

# Free energy computations
F_3D = U - T_vals * S_3D
F_2D = U - T_vals * S_2D

# Plotting
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.loglog(T_vals, F_3D, label="F_3D (Volumetric)", color='blue')
plt.loglog(T_vals, F_2D, label="F_2D (Projected)", color='orange', linestyle='--')
plt.axvline(1/kappa, color='red', linestyle=':', label="Collapse Threshold (β_B = 1)")
plt.xlabel("Temperature (K)")
plt.ylabel("Free Energy (J)")
plt.title("Free Energy: 3D vs Projected (2D) Entropy")
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# Plot the difference
plt.figure(figsize=(10, 6))
plt.semilogx(T_vals, F_2D - F_3D, label="ΔF = F_2D - F_3D", color='purple')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(1/kappa, color='red', linestyle=':', label="Collapse Threshold (β_B = 1)")
plt.xlabel("Temperature (K)")
plt.ylabel("Free Energy Difference (J)")
plt.title("Thermodynamic Preference: 2D vs 3D Entropy")
plt.grid(True, which="both", linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

###
#dS/dt	Collapse timing	Dynamic signal

# Reload and convert data to numeric types
df = pd.read_csv(csv_path, header=None, names=["Time", "Entropy", "Volume", "Area"])

# Convert all columns to numeric (in case some entries are strings with whitespace or bad formatting)
df = df.apply(pd.to_numeric, errors='coerce')

# Drop rows with NaNs caused by bad data
df.dropna(inplace=True)

# Calculate dS/dt (entropy rate of change)
df["dS_dt"] = df["Entropy"].diff() / df["Time"].diff()

# Smooth derivative for visualization
df["dS_dt_smooth"] = df["dS_dt"].rolling(window=3, center=True).mean()

# Plot Entropy over time
plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["Entropy"], label="Entropy (S)", color="black")
plt.xlabel("Time")
plt.ylabel("Entropy (J/K)")
plt.title("Entropy Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot dS/dt over time
plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["dS_dt_smooth"], label="dS/dt (Smoothed)", color="blue")
plt.axhline(0, color="gray", linestyle="--")
plt.xlabel("Time")
plt.ylabel("Entropy Rate of Change (dS/dt)")
plt.title("Rate of Entropy Change Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

###

# Calculate β_B = κ·T, where T is derived from entropy and volume (assuming blackbody radiation)
# S = (4/3) a T^3 V  =>  T = (3S / 4aV)^(1/3)
T_estimated = ((3 * df["Entropy"]) / (4 * a_rad * df["Volume"])) ** (1/3)

# Compute β_B = κ · T
df["beta_B"] = kappa * T_estimated

# Find time when β_B crosses 1
collapse_crossing = df[df["beta_B"] >= 1].iloc[0]  # First crossing point

# Plot dS/dt again with β_B = 1 marker
plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["dS_dt_smooth"], label="dS/dt (Smoothed)", color="blue")
plt.axhline(0, color="gray", linestyle="--")
plt.axvline(collapse_crossing["Time"], color="red", linestyle="--", label="β_B = 1 (Collapse Threshold)")
plt.xlabel("Time")
plt.ylabel("Entropy Rate of Change (dS/dt)")
plt.title("dS/dt with Bruno Collapse Threshold Marker")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.tight_layout()
plt.show()

# Output time where beta_B = 1
collapse_crossing["Time"]

###
#d²F/dT²	Critical point	Phase-transition signature
#

# Reuse entropy and free energy functions from before
# F = U - T*S

# Compute Free Energy for both 3D and projected 2D entropy
U_vals = a_rad * T_vals**4 * V
S_3D_vals = (4/3) * a_rad * T_vals**3 * V
S_2D_vals = (4/3) * a_rad * T_vals**2 * V / kappa

F_3D_vals = U_vals - T_vals * S_3D_vals
F_2D_vals = U_vals - T_vals * S_2D_vals

# Compute second derivative (numerical) of F_3D and F_2D w.r.t. T
d2F_3D = np.gradient(np.gradient(F_3D_vals, T_vals), T_vals)
d2F_2D = np.gradient(np.gradient(F_2D_vals, T_vals), T_vals)

# Plot second derivatives to check for discontinuity at beta_B = 1
plt.figure(figsize=(10, 6))
plt.semilogx(T_vals, d2F_3D, label="d²F_3D/dT²", color='blue')
plt.semilogx(T_vals, d2F_2D, label="d²F_2D/dT²", color='orange', linestyle='--')
plt.axvline(1/kappa, color='red', linestyle=':', label="β_B = 1")
plt.xlabel("Temperature (K)")
plt.ylabel("Second Derivative of Free Energy")
plt.title("Free Energy Curvature: Phase Transition Signature at Collapse")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.tight_layout()
plt.show()

###
#S/A vs R	Collapse scale	Entropy flattening marker

# Use the existing dataset (Entropy_Collapse_Export_1.5.csv) with Area and Entropy
# We want to compute S/A vs Radius to observe entropy flattening scale

# Estimate radius from surface area: A = 4πR² → R = sqrt(A / 4π)
df["Radius"] = np.sqrt(df["Area"] / (4 * np.pi))

# Compute S/A (entropy per unit area)
df["S_per_A"] = df["Entropy"] / df["Area"]

# Plot S/A vs Radius
plt.figure(figsize=(10, 6))
plt.plot(df["Radius"], df["S_per_A"], marker='o', linestyle='-', color='teal')
plt.axvline(np.sqrt((1 / kappa) / (4 * np.pi)), color='red', linestyle='--', label="Critical Radius from β_B = 1")
plt.xlabel("Radius (m)")
plt.ylabel("Entropy per Unit Area (S/A)")
plt.title("Entropy Surface Density vs Radius")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

###
#κ vs Mass	Universality check	Strengthens theoretical claim

# We'll calculate κ = 3 / (R * T) for different mass-based systems
# Create a list of representative compact objects with known mass, temperature, and radius

# Constants
solar_mass = 1.98847e30  # kg
G = 6.67430e-11          # m^3/kg/s^2
c = 299792458            # m/s

# Sample systems: name, mass (kg), temperature (K), radius (m)
systems = [
    ("White Dwarf", 1.0 * solar_mass, 1e5, 7e6),
    ("Neutron Star", 1.4 * solar_mass, 1e6, 1.2e4),
    ("Pre-BH Core", 20 * solar_mass, 1e10, 1.83e5),
    ("GW150914 BH", 62 * solar_mass, 1.2e-8, 1.83e5),
    ("Primordial BH", 1e12, 1e23, 1e-15),
]

# Compute κ and compactness (M/R)
results = []
for name, M, T, R in systems:
    kappa = 3 / (R * T)
    compactness = M / R
    results.append((name, M, R, T, kappa, compactness))

# Convert to DataFrame
df_kappa_mass = pd.DataFrame(results, columns=["Object", "Mass (kg)", "Radius (m)", "Temp (K)", "κ (1/K)", "M/R (kg/m)"])
df_kappa_mass.sort_values("Mass (kg)", inplace=True)
df_kappa_mass.reset_index(drop=True, inplace=True)

# Plot κ vs Mass
plt.figure(figsize=(10, 6))
plt.loglog(df_kappa_mass["Mass (kg)"], df_kappa_mass["κ (1/K)"], marker='o')
plt.xlabel("Mass (kg)")
plt.ylabel("Bruno Constant κ (1/K)")
plt.title("κ vs Mass: Universality Check")
plt.grid(True, which="both", linestyle="--")
plt.tight_layout()
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Bruno Constant vs Mass", dataframe=df_kappa_mass)


###
#CMB fluct. vs β_B	Cosmology	Big swing, big win

# Let's estimate beta_B = κ · T for the CMB and compare against structure formation/anisotropy scale

# Constants
kappa = 1313               # Bruno constant (1/K)
T_CMB = 2.725              # CMB average temperature in Kelvin
beta_B_CMB = kappa * T_CMB

# Estimate a physical scale from early universe: last scattering surface radius ~ 4.3e26 m
# We'll use the Bruno collapse condition: β_B = A/V = 3/R → R = 3/β_B
R_Bruno_CMB = 3 / beta_B_CMB

{
    "CMB Temperature (K)": T_CMB,
    "β_B (CMB)": beta_B_CMB,
    "Critical Collapse Radius at CMB (m)": R_Bruno_CMB,
    "Last Scattering Surface Radius (m)": 4.3e26,
    "Collapse within LSS?": R_Bruno_CMB < 4.3e26
}

###