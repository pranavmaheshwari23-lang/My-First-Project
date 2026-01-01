# Circle Calculator (All values from any one input)
# Units: cm
# π value fixed as 22/7

import math

pi = 22 / 7

print("Circle Calculator")
print("Choose what value you have:")
print("1. Radius")
print("2. Diameter")
print("3. Circumference")
print("4. Area")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    r = float(input("Enter radius (cm): "))

elif choice == 2:
    d = float(input("Enter diameter (cm): "))
    r = d / 2

elif choice == 3:
    c = float(input("Enter circumference (cm): "))
    r = c / (2 * pi)

elif choice == 4:
    a = float(input("Enter area (cm²): "))
    r = math.sqrt(a / pi)

else:
    print("Invalid choice")
    exit()

# Calculations
diameter = 2 * r
circumference = 2 * pi * r
area = pi * r * r

# Output
print("\n--- Results ---")
print(f"Radius        : {r:.2f} cm")
print(f"Diameter      : {diameter:.2f} cm")
print(f"Circumference : {circumference:.2f} cm")
print(f"Area          : {area:.2f} cm²")
