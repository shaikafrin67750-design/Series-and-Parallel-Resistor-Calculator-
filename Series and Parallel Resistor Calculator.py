# Series and Parallel Resistor Calculator

print("===== RESISTOR CALCULATOR =====")
print("1. Series Resistors")
print("2. Parallel Resistors")

choice = int(input("Enter your choice (1 or 2): "))

n = int(input("Enter number of resistors: "))

resistors = []

for i in range(n):
    r = float(input(f"Enter resistance R{i + 1} (Ohms): "))
    resistors.append(r)

if choice == 1:
    # Series resistance
    total = sum(resistors)

    print("\n===== RESULT =====")
    print("Total Series Resistance =", round(total, 2), "Ω")

elif choice == 2:
    # Parallel resistance
    if any(r <= 0 for r in resistors):
        print("Resistance must be greater than zero.")
    else:
        total = 1 / sum(1 / r for r in resistors)

        print("\n===== RESULT =====")
        print("Total Parallel Resistance =", round(total, 2), "Ω")

else:
    print("Invalid choice!")