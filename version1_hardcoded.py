# version1_hardcoded.py

# Coefficients
a = 0.5
b = -3
c = 28

# Time (e.g., 5th hour or day)
t = 5

# Temperature prediction
T = a * t**2 + b * t + c

# Output
print(f"Predicted temperature at t={t}: {T:.2f}°C")

