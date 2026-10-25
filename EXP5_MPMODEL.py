# MP Neuron Implementation 1

# AND Gate
w1 = 1
w2 = 1
theta = 2

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

for x1, x2 in inputs:
  summation = x1*w1 + x2*w2

  if summation >= theta:
    output = 1
  else:
    output = 0
  print(x1, x2, '->', output)

# OR Gate 
w1 = 1
w2 = 1
theta = 1

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

for x1, x2 in inputs:
  summation = w1*x1 + w2*x2

  if summation >= theta:
    output = 1
  else:
    output = 0
  print(x1, x2, '->', output)



# MP Neuron Implementation 2

def mp_neuron(x1, x2, w1, w2, threshold):
    net_input = (x1 * w1) + (x2 * w2)

    if net_input >= threshold:
        return 1
    else:
        return 0


inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]


# AND Gate
print("AND Gate using MP Neuron")
print("X1  X2 | Output")
print("-" * 16)

for x1, x2 in inputs:
    output = mp_neuron(x1, x2, 1, 1, 2)
    print(f"{x1}   {x2}  |   {output}")


# OR Gate
print("\nOR Gate using MP Neuron")
print("X1  X2 | Output")
print("-" * 16)

for x1, x2 in inputs:
    output = mp_neuron(x1, x2, 1, 1, 1)
    print(f"{x1}   {x2}  |   {output}")
