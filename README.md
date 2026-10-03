# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW1/Lab A/environment.yml
conda activate cspc
```
 ## PW1 - Lab A: Reproducible Foundations

### What I built
I simulated radioactive decay in two ways: first using regular Python loops, and then using vectorized NumPy operations.

### Speed comparison
The difference in speed was pretty big:
- Python loop: 2.1325 s
- NumPy: 0.0002 s
- Speed-up: about 11,463x faster with NumPy

All the tests passed successfully.

### Conclusion
Using NumPy arrays made the simulation much faster than going through the values one by one with Python loops. This shows why vectorized operations are useful when working with large amounts of data or doing heavy calculations.

## PW1 - Lab B: Data, Plotting, and Automation

### What I built
I loaded the observed decay data from decay_observed.csv and plotted it together with the analytical decay curve, using N0*exp(-λt). This made it easier to compare the experimental data with the theoretical result.

### Result
The observed points followed roughly the same shape as the analytical curve, so the data seems to agree pretty well with the expected radioactive decay law.

### Automation
I also created a Snakefile so that the figure can be rebuilt automatically whenever needed. Instead of manually running plot.py every time, the whole process can now be done with one command.

## PW2 - Lab A: Motion from Tracking Data

The mean acceleration I calculated was -8.58 m/s^2, with a standard deviation of 28.7. The expected value is around -9.81 m/s^2. The difference is mostly caused by the points at the edges, where np.gradient has to use one-sided differences.

The acceleration was also much noisier than the original position data. This makes sense because taking a derivative compares neighbouring points, so even small errors in the position measurements get amplified. Taking the derivative twice makes this effect even stronger. The position data itself looked much smoother.

I also integrated the noisy acceleration twice to get the position back. The resulting position differed from the original by a maximum of about 0.78 m. This showed that integration can smooth out some of the noise that appears when taking derivatives.

## PW2 - Lab B: Optimization in Chemistry

### Part 2 - Three ways to find a minimum
For the simple function f(x) = (x-3)^2 + 1, all three optimization methods gave basically the same answer, around x = 3, which was expected.

The harder function g(x) = x^4 - 3x^2 + x + 5 was more interesting. Starting from x0 = 0, Newton's method converged to about x = 0.17, but this point was actually a maximum rather than a minimum. Gradient descent and SLSQP instead found x ≈ -1.30, which is a minimum.

When I started from x0 = 2, both Newton's method and gradient descent found x ≈ 1.13, which is another actual minimum.

This showed me that Newton's method is really looking for a point where the slope is zero, so it doesn't automatically know whether that point is a minimum or a maximum. It also showed how much the starting point can affect the result.

### Part 3 - Reaction rate fitting
I fitted the model C(t) = C0*exp(-kt) to the noisy kinetics data. The fitted value was k ≈ 0.262, which is fairly close to the expected value of 0.25. The fitted curve also matched the data reasonably well, as shown in kinetics.png.

### Part 4 - Chemical equilibrium
For the reaction H2 + I2 <=> 2HI with K = 15.6, I solved for the equilibrium value of x using both Newton's method and SLSQP.

Both methods gave almost exactly the same result, x ≈ 0.664. This corresponds to approximately:
- H2 = 0.336 mol
- I2 = 0.336 mol
- HI = 1.328 mol

These values were close to the expected lab results.

### Part 5 - Titration equivalence point
As a bonus, I looked for the point where the pH curve changes most rapidly by finding where its slope reaches a maximum.

The equivalence point came out to about 50 mL, which makes sense because this is where the pH suddenly increases from roughly 3 to 11 in the data.

Overall, these labs helped me see the difference between theoretical models and real/noisy data, and also showed how numerical methods like NumPy, optimization, differentiation, and integration can be used to solve practical problems.