#CONCESSION STAND

print("---------- MENU -----------")
menu = {"pizza":2.55,
        "burger":3.99,
        "pop corns":5.99,
        "ice cream":0.99,
        "chips":2.99,
        "water":0.55,
        "pepsi":1.55,
        "coca cola":1.55,
        "beer":1.99,
        "french fries":1.99,
        "hot dog":2.55}
for item,price in menu.items():
    print(f"{item:12} ..........${price}")
print()
print("----------------------------")

cart = {}
total = 0

while True:
    item = input("what is the item (press 0 to quit)? ".lower())
    if item == "0":
        break
    elif item not in menu.keys():
        print(f"{item} is not in the menu!!!")
        continue

    try:
        quantity = int(input("how many? "))
    except ValueError:
        print("Enter a valid number")
        continue

#adding things to the cart
    if item in cart :
        cart[item] += quantity

    else:
        cart[item] = quantity

#bill


for item_,quantity_ in cart.items():
    item_total = menu[item_]*quantity_
    total += item_total




#i for item and q for the number of items
for i,q in cart.items():
    print(f"{i:9}.............  ${menu[i]} * {q}")
    print()
print(f"the total is-------------  ${total:.2f}")

