# Entropy-only evolution model (spacetime-agnostic)
# Hypothesis: entropy evolves through structural iteration (not classical time)
# Figure 35
from sympy import symbols, Function, Eq, Derivative, simplify, dsolve, sqrt, solve, diff, log

# Define symbolic variables
tau = symbols('tau')                  # Structural iteration (not time)
S = Function('S')                     # Entropy as a function of tau
k_val = 0.1                           # Entropy decay constant
S0 = 1.0                              # Initial entropy value at tau = 0


# Clean analytical decay solution
sqrt_solution = (sqrt(S0) - (k_val * tau) / 2)**2

# Define entropy decay equation: dS/dτ = -k * sqrt(S)
sqrt_decay_eq = Eq(S(tau).diff(tau), -k_val * sqrt(S(tau)))

# Solve the differential equation (without IC first)
general_solution = dsolve(sqrt_decay_eq, S(tau))

# Solve for integration constant using S(0) = S0
C1 = symbols('C1')
rhs_with_C1 = general_solution.rhs
C1_value = solve(rhs_with_C1.subs(tau, 0) - S0, C1)[0]
sqrt_solution = rhs_with_C1.subs(C1, C1_value)

# Print entropy function
print("Validated entropy decay function:", sqrt_solution)


# Correct entropy decay function (derived manually)
sqrt_solution = (sqrt(S0) - (k_val * tau) / 2)**2

# Evaluate at τ = 10
S_tau_10 = sqrt_solution.subs(tau, 10).evalf()
print("Validated entropy decay function:", sqrt_solution)
print("Entropy at τ = 10:", S_tau_10)

# Validate LHS vs RHS at τ = 5
tau_val = 5
lhs = diff(sqrt_solution, tau).subs(tau, tau_val).evalf()
rhs = (-k_val * sqrt(sqrt_solution.subs(tau, tau_val))).evalf()
print(f"Validation at τ = {tau_val}:")
print("LHS (dS/dτ) =", lhs)
print("RHS (-k * sqrt(S)) =", rhs)
print("Match?", abs(lhs - rhs) < 1e-6)


# === Future steps ===
# 1. Import real entropy measurements or thermodynamic data
# 2. Map measured data to S(τ) and compare shape
# 3. Identify decay rate k_val empirically
# 4. Test entropy preservation or deviation from model

####

import csv
import matplotlib.pyplot as plt
import numpy as np

# === Example: Load real entropy data from CSV ===
# CSV format: tau, measured_entropy
# e.g.
# 0, 1.00
# 1, 0.85
# 2, 0.73
# ...

# Placeholder path — update this with your file location
data_file = r"D:\entropy-research-library\entropy-hypothesis\scr\entropy_data.csv"

tau_data = []
measured_entropy = []

# Load CSV data
try:
    with open(data_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if present
        for row in reader:
            tau_data.append(float(row[0]))
            measured_entropy.append(float(row[1]))
except FileNotFoundError:
    print("CSV file not found. Please verify the file path.")

# === Model prediction from symbolic solution ===
model_entropy = [sqrt_solution.subs(tau, t).evalf() for t in tau_data]

# === Plot comparison ===
plt.plot(tau_data, measured_entropy, 'ro-', label='Measured Data')
plt.plot(tau_data, model_entropy, 'b--', label='Model Prediction')
plt.xlabel('τ (structural iteration)')
plt.ylabel('Entropy')
plt.title('Entropy Decay: Measured vs. Modeled')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
