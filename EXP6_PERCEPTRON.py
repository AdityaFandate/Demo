def train_perceptron(inputs, targets, learning_rate=0.1, epochs=10):
    weights = [0, 0]
    bias = 0

    for _ in range(epochs):
        for x, target in zip(inputs, targets):
            total = x[0] * weights[0] + x[1] * weights[1] + bias
            output = 1 if total >= 0 else 0
            error = target - output

            weights[0] += learning_rate * error * x[0]
            weights[1] += learning_rate * error * x[1]
            bias += learning_rate * error

    return weights, bias


def predict(x, weights, bias):
    total = x[0] * weights[0] + x[1] * weights[1] + bias
    return 1 if total >= 0 else 0


inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
and_targets = [0, 0, 0, 1]
or_targets = [0, 1, 1, 1]

and_weights, and_bias = train_perceptron(inputs, and_targets)
or_weights, or_bias = train_perceptron(inputs, or_targets)

print("A B | AND OR")
print("------------")
for x in inputs:
    print(x[0], x[1], "| ", predict(x, and_weights, and_bias), "  ",
          predict(x, or_weights, or_bias))

print("\nAND weights:", and_weights, "Bias:", and_bias)
print("OR weights:", or_weights, "Bias:", or_bias)
