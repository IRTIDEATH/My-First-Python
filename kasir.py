menu = {
    "popcorn": 3.00,
    "hotdog": 2.20,
    "soda": 1.70,
    "chips": 1.00,
    "fries": 6.75,
    "lemonade": 4.30,
    "burger": 5.00,
    "salad": 2.35
}

cart = []
total = 0

print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")

while True:
    food = input("Select an Items (q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)

print("--------------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print(f"Total is: ${total:.2f}")

discount = 3

if total > 19:
    total -= discount

print(f"You got discount 5% for buying 3 french fries.\nDiscount:{total}")
