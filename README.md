# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW1/Lab A/environment.yml
conda activate cspc
```
## PW1 - Lab A: Reproducible Foundations

**What I built:**
Simulated radioactive decay using pure Python loops and vectorized NumPy operations.

**Speed comparison (loop vs NumPy):**
- loop : 2.1325 s
- numpy : 0.0002 s
- speed-up: 11463.01 x faster

**Tests:** all passing? yes

**Conclusion:**
Simulating decay with NumPy vectors is orders of magnitude faster than iterating with standard Python loops, showing why array operations are essential for heavy computations.



## PW1 - Lab B: Data, Plotting, and Automation

**What I built:**
Loaded the observed decay data from decay_observed.csv and plotted it next to the analytical curve N0*exp(-λt) to compare them side by side.

**Result:**
The observed points follow the same shape as the analytical curve, so the data matches the decay law pretty well.

**Automation:**
Made a Snakefile so the figure gets rebuilt automatically from the data with one command, instead of running plot.py by hand every time.

## PW2 - Lab A: Motion from Tracking Data

**Mean acceleration:** -8.58 m/s^2 (std 28.7). Expected about -9.81, the gap comes mostly from the edge points where np.gradient uses one-sided differences.

**Why the acceleration is noisy:** a derivative compares neighbouring points, so the small measurement noise in the position gets amplified, and two derivatives in a row amplify it a lot. The position itself is smooth.

**Integrating back:** integrating the noisy acceleration twice gave a position that differs from the original by at most 0.78 m, so integration averages the noise out.

## PW2 - Lab B: Optimization in Chemistry

**Part 2 - Three routes to a minimum:**
On the easy function f(x)=(x-3)^2+1, all three methods agreed and landed on x≈3, no surprises there. The harder function g(x)=x^4-3x^2+x+5 was more interesting: starting from x0=0, Newton converged to x≈0.17, but that's actually a maximum, not a minimum — gradient descent and SLSQP found x≈-1.30 instead. Starting from x0=2, Newton and gradient descent both found x≈1.13, which is a real minimum this time. So Newton just finds where the slope is zero, it doesn't care if that's a hill or a valley, and where you start really changes what you get.

**Part 3 - Reaction rate fitting:**
Fit C(t)=C0*exp(-kt) to the noisy kinetics data and got k≈0.262, pretty close to the expected 0.25. The curve matches the data reasonably well, see kinetics.png.

**Part 4 - Chemical equilibrium:**
For H2 + I2 <=> 2HI with K=15.6, solved for x both with Newton and with SLSQP, and they matched: x≈0.664 both times. That gives H2≈0.336 mol, I2≈0.336 mol, HI≈1.328 mol, close to what the lab expected.

**Part 5 (bonus) - Titration equivalence point:**
Looked at where the pH curve's slope peaks and got V=50 mL, right where pH jumps from around 3 to 11 in the data.