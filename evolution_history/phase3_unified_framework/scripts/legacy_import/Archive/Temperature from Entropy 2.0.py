# 📘 Entropy-First Model: Deriving Energy-Temperature Relations
# 📂 Script Name: Entropy Energy Temperature_2.0
# Figure 59

# Constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)
c = 299792458       # Speed of light (m/s)
h = 6.62607015e-34  # Planck constant (J*s)

# Foundational Assumptions (Entropy-First Framework):
# 1. Entropy (S) is treated as the fundamental descriptor of any system.
# 2. Temperature (T) is emergent and only meaningful in the presence of energy distribution.
# 3. Energy (E) exists as the field excitation structured by entropy, not as an independent primitive.

# Start with statistical thermodynamics:
# Traditional: S = k_B * ln(W)  =>  entropy is a measure of state multiplicity

# Postulate 1: Define entropy in terms of energy field coherence:
# For a system governed by coherent field states:
# S = k_B * ln(Ω(E)) where Ω(E) is the count of distinguishable energy field configurations

# Goal: Derive T(E) from dS/dE (temperature as a derivative)
# By entropy-first:
#   1/T = dS/dE  =>  T(E) = 1 / (dS/dE)
# The shape of S(E) dictates the thermodynamic evolution

# Hypothesis-based example:
def entropy_field_model(E, alpha=1.5, E0=1e-21):
    from numpy import power, log
    return k_B * power(E / E0, alpha)

def temperature_from_entropy(E, alpha=1.5, E0=1e-21):
    from numpy import power
    dSdE = alpha * k_B / E0 * power(E / E0, alpha - 1)
    return 1 / dSdE

# Classical comparison: Planck-derived temperature from flux

def temperature_from_flux_planck(F_nu):
    """
    Estimate temperature from flux density using a simplified inversion of Planck's law.
    This assumes F_nu ≈ (2 * h * nu^3 / c^2) / (exp(h * nu / (k_B * T)) - 1)
    Rearranged for high-frequency (Wien) approximation:
    T ≈ h * nu / (k_B * ln((2 * h * nu^3 / c^2) / F_nu))
    """
    nu = 1.8e14  # Approximate H-band frequency (Hz)
    numerator = h * nu
    denominator = k_B * np.log((2 * h * nu ** 3) / (c ** 2 * F_nu))
    return numerator / denominator

# ✅ Load and extract relevant energy-temperature points

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def load_roman_mock_catalog(file_path):
    return pd.read_csv(file_path)

def abmag_to_flux_wm2hz(mag):
    return 10 ** (-(mag + 48.6) / 2.5) * 1e-26

def compute_entropy_temperature_column(df, flux_column_name, new_column_name):
    df[new_column_name] = temperature_from_entropy(df[flux_column_name])
    return df

def compute_planck_temperature_column(df, flux_column_name, new_column_name):
    df[new_column_name] = temperature_from_flux_planck(df[flux_column_name])
    return df

def plot_flux_vs_temperature(df):
    plt.figure(figsize=(8, 6))
    plt.loglog(df['Flux_MAGH'], df['Temp_from_MAGH'], 'o', markersize=4, alpha=0.6, label='Entropy Temp (MAGH)')
    plt.loglog(df['Flux_MAGH'], df['Temp_Planck_MAGH'], '.', markersize=3, alpha=0.6, label='Planck Temp (MAGH)')
    plt.loglog(df['Flux_APMAG_H'], df['Temp_from_APMAG_H'], 'x', markersize=4, alpha=0.6, label='Entropy Temp (APMAG_H)')
    plt.loglog(df['Flux_APMAG_H'], df['Temp_Planck_APMAG_H'], '+', markersize=3, alpha=0.6, label='Planck Temp (APMAG_H)')
    plt.xlabel("Flux (W/m²/Hz)")
    plt.ylabel("Temperature (K)")
    plt.title("Entropy vs Planck: Temperature-Flux Comparison")
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_roman_mock_catalog("entropy-hypothesis/Data/hlsp_rslss_roman_wfi_multi_wfc_v1_sim-ultradeep-mocks.csv")

    df['Flux_MAGH'] = abmag_to_flux_wm2hz(df['MAGH'])
    df['Flux_APMAG_H'] = abmag_to_flux_wm2hz(df['APMAG_H'])

    df = compute_entropy_temperature_column(df, 'Flux_MAGH', 'Temp_from_MAGH')
    df = compute_entropy_temperature_column(df, 'Flux_APMAG_H', 'Temp_from_APMAG_H')

    df = compute_planck_temperature_column(df, 'Flux_MAGH', 'Temp_Planck_MAGH')
    df = compute_planck_temperature_column(df, 'Flux_APMAG_H', 'Temp_Planck_APMAG_H')

    print(df[['MAGH', 'Flux_MAGH', 'Temp_from_MAGH', 'Temp_Planck_MAGH']].head())

    plot_flux_vs_temperature(df)

# ✅ Confirm alignment and potential deviations between classical and entropy-first predictions
