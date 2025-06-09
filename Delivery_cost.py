# A Python script that calculates delivery costs based on weight and distance.

def calculate_delivery_cost(weight_kg, distance_km) :
    if weight_kg < 5 :
        cost = distance_km *5
    elif (weight_kg >= 5) and (weight_kg < 20) :
        cost = distance_km * 8
    else:
        cost = distance_km * 10
    if distance_km > 500 :
        cost +=100
    return cost
# Take input from the user
weight = float(input("Enter the weight of the package (kg): "))
distance = float(input("Enter the distance for delivery (km): "))

cost = calculate_delivery_cost(weight, distance)
print(f"Delivery cost for {weight}kg over {distance}km is GHC {cost}.")

