def calculate_temperature(a, b, c, t):
    return a * t**2 + b * t + c

def method_hardcoded():
    print("\n--- Method: Hardcoded Values ---")
    a = 0.5
    b = -3
    c = 28
    t = 5
    T = calculate_temperature(a, b, c, t)
    print(f"Predicted temperature at t={t}: {T:.2f}°C\n")
