from PyThermalAnalysis.thermodynamicstate import ThermodynamicState
from PyThermalAnalysis.exergyanalysis import ExergyAnalysis

# Define ambient conditions
T0 = 298.15  # K
h0 = 0.0     # kJ/kg
s0 = 0.0     # kJ/kg-K

# Create thermodynamic states
state1 = ThermodynamicState(500, 101325, 2800, 6.8)
state2 = ThermodynamicState(300, 101325, 1500, 5.2)

# Perform exergy analysis
exergy_analyzer = ExergyAnalysis(T0, h0, s0)
exergy1 = exergy_analyzer.calculate_exergy(state1)
exergy2 = exergy_analyzer.calculate_exergy(state2)
exergy_destruction = exergy_analyzer.exergy_balance([state1], [state2])

print(f"Exergy at state 1: {exergy1:.2f} kJ/kg")
print(f"Exergy at state 2: {exergy2:.2f} kJ/kg")
print(f"Exergy destruction: {exergy_destruction:.2f} kJ")
