# The linear, surface, and volumetric expansions can be calculated,
# respectively, by the following formulas:
# delta_linear = length * lin_exp_coef * delta_temp
# delta_area = area * area_exp_coef * delta_temp
# delta_volume = volume * vol_exp_coef * delta_temp
# Write code that displays a menu for the user showing three options: if he/she
# wants to calculate the linear expansion, he/she must type 1.  if he/she
# wants to calculate the surface expansion, he/she must type 2. if he/she
# wants to calculate the volumetric expansion, he/she must type 3.


question = int(input(f'''What do you want to calculate?

[1] Linear expansion
[2] Surface expansion
[3] Volumetric expansion

'''))

if question == 1:
    L0 = float(input("Initial length: "))
    alfa = float(input("Linear expansion coefficient: "))
    dT = float(input("Variation of temperature: "))
    dL = L0*alfa*dT
    print(f"The variation in length was {dL}")
elif question == 2:
    A0 = float(input("Initial area: "))
    beta = float(input("Linear surface coefficient: "))
    dT = float(input("Variation of temperature: "))
    dA = A0*beta*dT
    print(f"The variation in area was {dA}")
elif question == 3:
    V0 = float(input("Initial volume: "))
    gamma = float(input("Volumetric expansion coefficient: "))
    dT = float(input("Variation of temperature: "))
    dV = V0*gamma*dT
    print(f"The variation in volume was {dV}")
else:
    print("Invalid selection.")


