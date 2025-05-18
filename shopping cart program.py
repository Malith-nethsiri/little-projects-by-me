# shopping cart program

foods = []
prices =[]
total = 0

while True :
    food = input("what is the food (press q to quit) -- ")
    if food.lower() == "q" :
        break
    else:
        price = float(input(f"what is the price of {food} -- $"))
        foods.append(food)
        prices.append(price)

print("----- the bill -----")

for food in foods:
    print(food)

for price in prices:
    total += price

print()
print(f"the total is ${total}")


