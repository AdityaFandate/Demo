# EXPERIMENT 10: HYBRID NEURO-FUZZY SYSTEM (ANFIS)
#
# Installation (run in the VS Code terminal if needed):
# python -m pip install numpy

import numpy as np


# Generalized bell membership function
def bell_mf(x, a, b, c):
    return 1.0 / (1.0 + np.abs((x - c) / a) ** (2 * b))


class ANFIS:
    def __init__(self, premise, consequent):
        self.premise = premise
        self.consequent = np.array(consequent, dtype=float)

    def forward(self, x, y, verbose=False):
        # Layer 1: Fuzzification
        muA1 = bell_mf(x, *self.premise["A1"])
        muA2 = bell_mf(x, *self.premise["A2"])
        muB1 = bell_mf(y, *self.premise["B1"])
        muB2 = bell_mf(y, *self.premise["B2"])

        # Layer 2: Rule firing strengths
        w = np.array([muA1 * muB1, muA2 * muB2])

        # Layer 3: Normalize firing strengths
        w_bar = w / w.sum()

        # Layer 4: Rule consequents
        inputs = np.array([x, y, 1.0])
        f = self.consequent @ inputs
        weighted_f = w_bar * f

        # Layer 5: Final output
        output = weighted_f.sum()

        if verbose:
            print("Layer 1 (Membership grades):")
            print(f" muA1({x}) = {muA1:.4f}, muA2({x}) = {muA2:.4f}")
            print(f" muB1({y}) = {muB1:.4f}, muB2({y}) = {muB2:.4f}")

            print("Layer 2 (Firing strengths):")
            print(f" w1 = {w[0]:.4f}, w2 = {w[1]:.5f}")

            print("Layer 3 (Normalized strengths):")
            print(f" w1_bar = {w_bar[0]:.4f}, w2_bar = {w_bar[1]:.4f}")

            print("Layer 4 (Rule outputs):")
            print(f" f1 = {f[0]:.4f}, f2 = {f[1]:.4f}")
            print(
                f" w1_bar*f1 = {weighted_f[0]:.4f}, "
                f"w2_bar*f2 = {weighted_f[1]:.4f}"
            )

            print("Layer 5 (Final output):")
            print(f" O = {output:.4f}")

        # Save values for parameter update
        self.cache = {"w_bar": w_bar, "inputs": inputs}

        return output

    def update_consequent(self, target, output, lr, verbose=False):
        # Calculate error
        error = target - output
        w_bar = self.cache["w_bar"]
        inputs = self.cache["inputs"]

        # Gradient descent update
        gradient = -error * np.outer(w_bar, inputs)
        delta = -lr * gradient

        old = self.consequent.copy()
        self.consequent += delta

        if verbose:
            names = ["p", "q", "r"]
            print(f"{'Param':<6}{'-dE/dθ':>10}{'Δθ':>10}{'Old':>10}{'New':>10}")

            for i in range(2):
                for j in range(3):
                    print(
                        f"{names[j]}{i+1:<5}"
                        f"{-gradient[i, j]:>10.4f}"
                        f"{delta[i, j]:>10.4f}"
                        f"{old[i, j]:>10.4f}"
                        f"{self.consequent[i, j]:>10.4f}"
                    )


if __name__ == "__main__":

    # Initial membership function parameters
    premise = {
        "A1": (2, 1, 2),
        "A2": (2, 1, 6),
        "B1": (2, 1, 4),
        "B2": (2, 1, 8)
    }

    # Initial consequent parameters
    consequent = [
        [2, 1, 1],
        [1, 3, -2]
    ]

    # Input values, target and learning rate
    x, y = 3, 4
    target = 12
    lr = 0.02

    model = ANFIS(premise, consequent)

    # Forward pass
    print("=" * 50)
    print("(a) FORWARD PASS")
    print("=" * 50)

    output = model.forward(x, y, verbose=True)

    # Calculate error
    print("\n" + "=" * 50)
    print("(b) ERROR")
    print("=" * 50)

    error = target - output
    E = 0.5 * error ** 2

    print(f"e = {target} - {output:.4f} = {error:.4f}")
    print(f"E = 0.5 * e^2 = {E:.4f}")

    # Update consequent parameters
    print("\n" + "=" * 50)
    print(f"(c) CONSEQUENT UPDATE (learning rate = {lr})")
    print("=" * 50)

    model.update_consequent(target, output, lr, verbose=True)

    # Verify updated parameters
    print("\nVerification with updated parameters:")
    new_output = model.forward(x, y)
    new_error = 0.5 * (target - new_output) ** 2

    print(f"New output = {new_output:.4f}")
    print(f"New error = {new_error:.4f} (was {E:.4f})")

    # Train for 10 epochs
    print("\n" + "=" * 50)
    print("BONUS: Training for several epochs")
    print("=" * 50)

    model = ANFIS(premise, consequent)

    for epoch in range(1, 11):
        output = model.forward(x, y)
        E = 0.5 * (target - output) ** 2

        print(
            f"Epoch {epoch:2d}: "
            f"output = {output:.4f}, error = {E:.6f}"
        )

        model.update_consequent(target, output, lr)