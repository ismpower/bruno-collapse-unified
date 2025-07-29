# 📘 Entropy-First Model: Deriving Energy-Temperature Relations
# 📂 Script Name: Entropy Energy Temperature 3
# Figure 60: Empirical Divergence + Frequency Scaling

# Constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)
c = 299792458       # Speed of light (m/s)
h = 6.62607015e-34  # Planck constant (J*s)

# Foundational Assumptions (Entropy-First Framework):
# 1. Entropy (S) is treated as the fundamental descriptor of any system.
# 2. Temperature (T) is emergent and only meaningful in the presence of energy distribution.
# 3. Energy (E) exists as the field excitation structured by entropy, not as an independent primitive.

# Hypothesis-based example:
def entropy_field_model(E, alpha=1.5, E0=1e-21):
    from numpy import power
    return k_B * power(E / E0, alpha)

def temperature_from_entropy(E, alpha=1.5, E0=1e-21):
    from numpy import power
    dSdE = alpha * k_B / E0 * power(E / E0, alpha - 1)
    return 1 / dSdE

# Classical comparison: Planck-derived temperature from flux, parametrized by frequency band

def temperature_from_flux_planck(F_nu, nu=1.8e14):
    numerator = h * nu
    denominator = k_B * np.log((2 * h * nu ** 3) / (c ** 2 * F_nu))
    return numerator / denominator

# ✅ Load and process data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def load_roman_mock_catalog(file_path):
    return pd.read_csv(file_path)

def abmag_to_flux_wm2hz(mag):
    return 10 ** (-(mag + 48.6) / 2.5) * 1e-26

def compute_entropy_temperature_column(df, flux_column_name, new_column_name):
    df[new_column_name] = temperature_from_entropy(df[flux_column_name])
    return df

def compute_planck_temperature_column(df, flux_column_name, new_column_name, nu):
    df[new_column_name] = temperature_from_flux_planck(df[flux_column_name], nu=nu)
    return df

def plot_flux_vs_temperature(df):
    plt.figure(figsize=(9, 6))
    plt.loglog(df['Flux_MAGH'], df['Temp_from_MAGH'], 'o', markersize=4, alpha=0.6, label='Entropy Temp (MAGH)')
    plt.loglog(df['Flux_MAGH'], df['Temp_Planck_MAGH_1.8e14'], '.', markersize=3, alpha=0.6, label='Planck Temp ν=1.8e14')
    plt.loglog(df['Flux_MAGH'], df['Temp_Planck_MAGH_3e14'], '.', markersize=3, alpha=0.4, label='Planck Temp ν=3e14')
    plt.loglog(df['Flux_MAGH'], df['Temp_Planck_MAGH_1e13'], '.', markersize=3, alpha=0.4, label='Planck Temp ν=1e13')
    plt.xlabel("Flux (W/m²/Hz)")
    plt.ylabel("Temperature (K)")
    plt.title("Planck vs Entropy Model — Frequency Scaling")
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig("Figure_60.png", dpi=300)
    plt.show()

    # Export to CSV
    df_export = df[[
        'MAGH', 'Flux_MAGH', 'Temp_from_MAGH',
        'Temp_Planck_MAGH_1.8e14', 'Temp_Planck_MAGH_3e14', 'Temp_Planck_MAGH_1e13'
    ]]
    df_export.to_csv("Figure_60_Data.csv", index=False)
    print("\nData exported to 'Figure_60_Data.csv' and plot saved as 'Figure_60.png'.")

if __name__ == "__main__":
    df = load_roman_mock_catalog("entropy-hypothesis/Data/hlsp_rslss_roman_wfi_multi_wfc_v1_sim-ultradeep-mocks.csv")

    df['Flux_MAGH'] = abmag_to_flux_wm2hz(df['MAGH'])
    df = compute_entropy_temperature_column(df, 'Flux_MAGH', 'Temp_from_MAGH')

    df = compute_planck_temperature_column(df, 'Flux_MAGH', 'Temp_Planck_MAGH_1.8e14', nu=1.8e14)
    df = compute_planck_temperature_column(df, 'Flux_MAGH', 'Temp_Planck_MAGH_3e14', nu=3e14)
    df = compute_planck_temperature_column(df, 'Flux_MAGH', 'Temp_Planck_MAGH_1e13', nu=1e13)

    plot_flux_vs_temperature(df)

# ✅ Exported image and dataset for Figure 60
