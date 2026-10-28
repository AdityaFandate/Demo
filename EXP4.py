import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("employee_salary_dataset.csv")
salary = data["Monthly_Salary"].dropna()

# Population statistics
population_mean = salary.mean()
print("Number of Employees:", len(salary))
print("Population Mean:", round(population_mean, 2))
print("Population Std Dev:", round(salary.std(), 2))

# CLT simulation
sample_sizes = [5, 10, 30, 50]
num_samples = 1000

plt.figure(figsize=(12, 8))

for i, n in enumerate(sample_sizes):
    sample_means = [
        salary.sample(n=n, replace=True).mean()
        for _ in range(num_samples)
    ]

    print(f"\nSample Size = {n}")
    print("Mean:", round(np.mean(sample_means), 2))
    print("Std Dev:", round(np.std(sample_means), 2))

    plt.subplot(2, 2, i + 1)
    plt.hist(sample_means, bins=30, edgecolor="black", color="skyblue")
    plt.axvline(population_mean, color="red", linestyle="--",
                label="Population Mean")
    plt.title(f"Sample Size = {n}")
    plt.xlabel("Sample Mean Monthly Salary")
    plt.ylabel("Frequency")
    plt.legend()

plt.suptitle("Central Limit Theorem - Employee Salary", fontsize=15)
plt.tight_layout()
plt.show()