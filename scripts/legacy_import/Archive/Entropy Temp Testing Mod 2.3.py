# Entropy-only evolution model (spacetime-agnostic)
# Hypothesis: entropy evolves through structural iteration (not classical time)

from sympy import symbols, Function, Eq, Derivative, simplify

# Define symbols
S, tau, k = symbols('S tau k')
Phi = Function('Phi')(S)  # entropic decay function dependent on S

# Entropy-only evolution equation
entropy_evolution_eq = Eq(Derivative(S, tau), -k * Phi)

# Example: test with linear decay function Phi(S) = S
entropy_evolution_linear = entropy_evolution_eq.subs(Phi, S)

# Simplify for clarity
entropy_evolution_linear_simplified = simplify(entropy_evolution_linear)

# Display results
print("General entropy evolution equation:", entropy_evolution_eq)
print("Assuming linear decay (Phi = S):", entropy_evolution_linear_simplified)

# Notes:
# - tau is a structural evolution parameter, not time
# - k is a positive constant related to entropy dissipation rate
# - Result is a pure exponential-like decay of entropy toward zero
# - This can be extended to nonlinear Phi(S) later

###

from sympy import symbols, Function, Eq, dsolve, sqrt, solve, simplify
from sympy import diff


# Define symbols
tau = symbols('tau')
S = Function('S')
C1 = symbols('C1')
k_val = 0.1

# Define the equation (no initial condition yet)
sqrt_eq = Eq(S(tau).diff(tau), -k_val * sqrt(S(tau)))
sqrt_solution_general = dsolve(sqrt_eq, S(tau))


# Solve for C1 using S(0) = 1
S0 = 1.0
rhs_with_C1 = sqrt_solution_general.rhs
C1_value = solve(rhs_with_C1.subs(tau, 0) - S0, C1)[0]

# Substitute C1 back into solution
sqrt_solution = rhs_with_C1.subs(C1, C1_value)
sqrt_solution = -1 * sqrt_solution + 2 * S0  # reflect decay, preserve S(0) = 1.0
S_tau_10_sqrt = sqrt_solution.subs(tau, 10).evalf()

print("Square root decay solution (Φ = √S):", sqrt_solution)
print("Entropy at τ = 10 (√S):", S_tau_10_sqrt)

from sympy import diff

# Check if entropy is increasing or decreasing
S_prime = diff(sqrt_solution, tau)
print("dS/dτ =", S_prime)

from sympy import sqrt

# Define tau symbolically for evaluation
tau_val = 5  # Test point; you can try other values too

# Corrected entropy decay function
S_corrected = -0.0025 * tau**2 - 0.1 * tau + 1

# LHS: dS/dτ
dS_dtau = S_corrected.diff(tau)

# RHS: -k * sqrt(S)
rhs = -k_val * sqrt(S_corrected)

# Evaluate both at tau_val
lhs_num = dS_dtau.subs(tau, tau_val).evalf()
rhs_num = rhs.subs(tau, tau_val).evalf()

print(f"Validation at τ = {tau_val}:")
print("LHS (dS/dτ) =", lhs_num)
print("RHS (-k * sqrt(S)) =", rhs_num)
print("Match?", abs(lhs_num - rhs_num) < 1e-6)
