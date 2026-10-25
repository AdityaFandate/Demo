def hebb_learning(inputs, targets):
    weights = [0, 0]
    bias = 0

    for x, target in zip(inputs, targets):
        weights[0] += x[0] * target
        weights[1] += x[1] * target
        bias += target

    return weights, bias


def predict(x, weights, bias):
    net = x[0] * weights[0] + x[1] * weights[1] + bias
    return 1 if net > 0 else 0


inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

targets = [0, 0, 0, 1]

weights, bias = hebb_learning(inputs, targets)

print("Hebb Learning Rule - AND Gate")
print("X1 X2 | Output")
print("-" * 18)

for x in inputs:
    output = predict(x, weights, bias)
    print(x[0], " ", x[1], " | ", output)

print("\nFinal weights:", weights)
print("Final bias:", bias)