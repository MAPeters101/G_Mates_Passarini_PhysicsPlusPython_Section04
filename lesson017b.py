# The linear, surface, and volumetric expansions can be calculated,
# respectively, by the following formulas:
# delta_linear = length * lin_exp_coef * delta_temp
# delta_area = area * area_exp_coef * delta_temp
# delta_volume = volume * vol_exp_coef * delta_temp
# Write code that displays a menu for the user showing three options: if he/she
# wants to calculate the linear expansion, he/she must type 1.  if he/she
# wants to calculate the surface expansion, he/she must type 2. if he/she
# wants to calculate the volumetric expansion, he/she must type 3.

print("Please select an option from the following: ")
print("\tEnter 1 to calculate Linear expansion.")
print("\tEnter 2 to calculate Surface expansion.")
print("\tEnter 3 to calculate Volumetric expansion.")
choice = int(input("Enter selection: "))

if choice == 1:
    length = float(input("Enter the initial length: "))
    lin_exp_coef = float(input("Enter the linear expansion coefficient: "))
    delta_temp = float(input("Enter the change in temperature: "))
    delta_linear = length * lin_exp_coef * delta_temp
    print(f"The Linear expansion will be: {delta_linear}")
elif choice == 2:
    area = float(input("Enter the initial area: "))
    area_exp_coef = float(input("Enter the area expansion coefficient: "))
    delta_temp = float(input("Enter the change in temperature: "))
    delta_area = area * area_exp_coef * delta_temp
    print(f"The Surface expansion will be: {delta_area}")
elif choice == 3:
    volume = float(input("Enter the initial volume: "))
    vol_exp_coef = float(input("Enter the volumetric expansion coefficient: "))
    delta_temp = float(input("Enter the change in temperature: "))
    delta_volume = volume * vol_exp_coef * delta_temp
    print(f"The Volumetric expansion will be: {delta_volume}")
else:
    print("Invalid selection.")



