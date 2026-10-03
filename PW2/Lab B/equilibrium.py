"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
    return (2*x)**2 / ((a - x)*(b - x)) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x_newton = newton(k_imbalance, x0=0.5)
print("Newton x:", x_newton)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
res = minimize(lambda x: k_imbalance(x[0])**2, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]
print("SLSQP x:", x_slsqp)

print("Agree?", np.isclose(x_newton, x_slsqp, atol=1e-3))
# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
x_eq = x_newton  # use the Newton result (they agree)
H2_eq = a - x_eq
I2_eq = b - x_eq
HI_eq = 2 * x_eq
print(f"Equilibrium: H2={H2_eq:.3f}, I2={I2_eq:.3f}, HI={HI_eq:.3f}")

x_range = np.linspace(0, 0.999, 200)
H2_range = a - x_range
I2_range = b - x_range
HI_range = 2 * x_range

plt.plot(x_range, H2_range, label="H2")
plt.plot(x_range, I2_range, label="I2")
plt.plot(x_range, HI_range, label="HI")
plt.axvline(x_eq, color='black', linestyle='--', label=f"equilibrium x={x_eq:.3f}")
plt.xlabel("Extent x")
plt.ylabel("Amount (mol)")
plt.legend()
plt.savefig('equilibrium.png')
