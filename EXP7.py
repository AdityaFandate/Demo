import numpy as np
from scipy.stats import norm, bernoulli

# Part 1: MLE for Normal Distribution
# Given Normal distribution dataset
normal_data = np.array([25, 28, 24, 27, 30, 26, 29, 23, 28, 27])

print("Normal Distribution Dataset:")
print(normal_data)

# Calculate MLE of Mean
mu_mle = np.mean(normal_data)

# Calculate MLE of Variance
variance_mle = np.mean((normal_data - mu_mle) ** 2)

# Calculate MLE of Standard Deviation
sigma_mle = np.sqrt(variance_mle)

print("\nMLE Estimates for Normal Distribution:")
print("Estimated Mean (μ) =", mu_mle)
print("Estimated Variance (σ2) =", variance_mle)
print("Estimated Standard Deviation (σ) =", sigma_mle)

# Part 2: MLE for Bernoulli Distribution

# Given Bernoulli dataset
bernoulli_data = np.array([1, 0, 1, 1, 0, 0, 1, 1, 0, 1])

print("\nBernoulli Distribution Dataset:")
print(bernoulli_data)

# Calculate number of successes
successes = np.sum(bernoulli_data)

# Total number of observations
n = len(bernoulli_data)

# MLE estimate of probability of success
p_mle = successes / n

print("\nMLE Estimate for Bernoulli Distribution:")
print("Number of Successes =", successes)
print("Total Observations =", n)
print("Estimated Probability (p) =", p_mle)
