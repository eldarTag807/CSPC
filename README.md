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