# Percentage Increase and Decrease Calculator

print("Percentage Calculator")
print("1. Percentage Increase")
print("2. Percentage Decrease")

choice = input("Enter your choice (1 or 2): ")

original = float(input("Enter the original value: "))
new = float(input("Enter the new value: "))

if choice == "1":
    increase = new - original
    percentage = (increase / original) * 100
    print("Increase:", increase)
    print("Percentage Increase:", percentage, "%")
    print("I told you I will make it right within 5 minutes.")

elif choice == "2":
    decrease = original - new
    percentage = (decrease / original) * 100
    print("Decrease:", decrease)
    print("Percentage Decrease:", percentage, "%")
    print("I told you I will make it right within 5 minutes.")

else:
    print("Invalid choice")
    print("I told you I will make it right within 5 minutes.")
