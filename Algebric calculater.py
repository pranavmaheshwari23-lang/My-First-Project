print("BASIC ALGEBRA SOLVER ")
print("Solve equations like: 2*x + 5 = 15")
print("-" * 40)

equation = input("Enter equation: ")

# Detect variable automatically
for ch in equation:
    if ch.isalpha():
        var = ch
        break

# Split equation
left, right = equation.split("=")

# Convert equation to expression = 0
expr = left + "-(" + right + ")"

# Replace variable with value 0 and 1 to find coefficient
expr0 = expr.replace(var, "(0)")
expr1 = expr.replace(var, "(1)")

value0 = eval(expr0)
value1 = eval(expr1)

# Calculate coefficient and constant
coefficient = value1 - value0
constant = value0

# Solve ax + b = 0
answer = -constant / coefficient

print(f" {var} = {answer}")
