#A Simple Invoice Generator
from datetime import date
print("Enter customer name: ")
customer_name = input()

print("Enter Item name:")
item_name = input()

print("Quantity of item: ")
quantity_item = int(input())

print("Enter price per item: ")
price_per_item = float(input())

total_cost = quantity_item * price_per_item

if 5 < quantity_item <=10:
    discount = 0.10 * total_cost
    total_cost = total_cost - discount
    print(f"You have a discount of {discount:.2f} for your purchase.\n")
elif quantity_item > 10 and quantity_item <= 20:
    discount = 0.20 * total_cost
    total_cost = total_cost - discount
    print(f"You have a discount of {discount:.2f} for your purchase.\n")


#date and time
today = date.today()
print(f"Date: {today.strftime('%d-%m-%Y')}")

#Invoice note with == decoration
print("\n" + "="*40)
print("\t\t\t\tINVOICE")
print("="*40)

#Display Result
print(f"{'Customer Name:':25} {customer_name}")
print(f"{'Item Bought:':25} {item_name}")
print(f"{'Quantity:':25}{quantity_item}")
print(f"{'Price per Item:':25}GHC {price_per_item:.2f}")
print(f"{'Total Cost:':25}GHC {total_cost:.2f}")

#A dash for decoration
print("-"*40)
print("\n" + "="*40)
#A short message
print("\tThank you for shopping with us!")
print("="*40)

'''
This is an example of a multi-line comment.
Wow
'''