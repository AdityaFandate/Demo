# EXPERIMENT 9: FUZZY LOGIC CONTROLLER
# Aim: To control fan speed based on temperature and humidity.
#
# Installation (run in the VS Code terminal if needed):
# python -m pip install numpy scikit-fuzzy networkx

import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

# 1. Define input and output variables
temp = ctrl.Antecedent(np.arange(0, 101, 1), 'temp')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
speed = ctrl.Consequent(np.arange(0, 101, 1), 'speed')

# 2. Define membership functions
temp['cold'] = fuzzy.trimf(temp.universe, [0, 0, 20])
temp['warm'] = fuzzy.trimf(temp.universe, [0, 20, 40])
temp['hot'] = fuzzy.trimf(temp.universe, [20, 40, 40])

humidity['low'] = fuzzy.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzzy.trimf(humidity.universe, [0, 50, 100])
humidity['high'] = fuzzy.trimf(humidity.universe, [50, 100, 100])

speed['slow'] = fuzzy.trimf(speed.universe, [0, 0, 50])
speed['medium'] = fuzzy.trimf(speed.universe, [0, 50, 100])
speed['high'] = fuzzy.trimf(speed.universe, [50, 100, 100])

# 3. Define fuzzy rules
rule1 = ctrl.Rule(temp['cold'] & humidity['low'], speed['slow'])
rule2 = ctrl.Rule(temp['cold'] & humidity['medium'], speed['slow'])
rule3 = ctrl.Rule(temp['cold'] & humidity['high'], speed['medium'])

rule4 = ctrl.Rule(temp['warm'] & humidity['low'], speed['medium'])
rule5 = ctrl.Rule(temp['warm'] & humidity['medium'], speed['medium'])
rule6 = ctrl.Rule(temp['warm'] & humidity['high'], speed['high'])

rule7 = ctrl.Rule(temp['hot'] & humidity['low'], speed['medium'])
rule8 = ctrl.Rule(temp['hot'] & humidity['medium'], speed['high'])
rule9 = ctrl.Rule(temp['hot'] & humidity['high'], speed['high'])

# 4. Create the fuzzy control system
speed_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3,
    rule4, rule5, rule6,
    rule7, rule8, rule9
])

fan = ctrl.ControlSystemSimulation(speed_ctrl)

# 5. Set input values
temperature = 29
humidity_value = 77

fan.input['temp'] = temperature
fan.input['humidity'] = humidity_value

# 6. Compute the fuzzy output
fan.compute()

# 7. Display results
print("Fuzzy Logic Fan Controller")
print("--------------------------")
print("Temperature:", temperature, "°C")
print("Humidity:", humidity_value, "%")
print("Fan Speed:", round(fan.output['speed'], 2), "%")