
# Experiment: Bootstrap Confidence Interval and Permutation Test

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ==================================================
# 1. BOOTSTRAP CONFIDENCE INTERVAL
# ==================================================

data = np.array([10, 12, 15, 14, 13, 16, 18, 11, 15, 14])

original_mean = np.mean(data)
B = 10000

bootstrap_means = []

for _ in range(B):
    sample = np.random.choice(data, size=len(data), replace=True)
    bootstrap_means.append(np.mean(sample))

bootstrap_means = np.array(bootstrap_means)

lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)

print("===== BOOTSTRAP CONFIDENCE INTERVAL =====")
print("Original Sample Mean:", original_mean)
print("95% Confidence Interval:")
print(f"Lower Limit: {lower:.2f}")
print(f"Upper Limit: {upper:.2f}")

plt.figure(figsize=(10, 4))
plt.hist(bootstrap_means, bins=30, edgecolor="black")
plt.axvline(original_mean, linestyle="--", label="Original Mean")
plt.axvline(lower, linestyle="--", label="Lower Limit")
plt.axvline(upper, linestyle="--", label="Upper Limit")
plt.xlabel("Bootstrap Mean")
plt.ylabel("Frequency")
plt.title("Bootstrap Distribution of the Mean")
plt.legend()
plt.tight_layout()
plt.show()

# ==================================================
# 2. PERMUTATION TEST
# ==================================================

group_A = np.array([55, 58, 60, 57, 59])
group_B = np.array([65, 67, 64, 66, 68])

observed_difference = np.mean(group_A) - np.mean(group_B)
combined = np.concatenate([group_A, group_B])
n_A = len(group_A)

permutation_differences = []

for _ in range(B):
    shuffled = np.random.permutation(combined)
    difference = np.mean(shuffled[:n_A]) - np.mean(shuffled[n_A:])
    permutation_differences.append(difference)

permutation_differences = np.array(permutation_differences)

p_value = np.mean(
    np.abs(permutation_differences) >= abs(observed_difference)
)

print("\n===== PERMUTATION TEST =====")
print("Observed Difference:", observed_difference)
print("Permutation P-value:", p_value)

if p_value < 0.05:
    print("Decision: Reject H0")
    print("Conclusion: Significant difference between group means.")
else:
    print("Decision: Do not reject H0")
    print("Conclusion: Insufficient evidence of a difference.")

plt.figure(figsize=(10, 4))
plt.hist(permutation_differences, bins=30, edgecolor="black")
plt.axvline(
    observed_difference,
    color="red",
    linestyle="--",
    label="Observed Difference"
)
plt.xlabel("Difference in Means")
plt.ylabel("Frequency")
plt.title("Permutation Null Distribution")
plt.legend()
plt.tight_layout()
plt.show()
