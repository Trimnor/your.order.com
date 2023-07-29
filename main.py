foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == "q":
        break
    else:
        price = float(input('Enter the price of food: '))
        foods.append(food)
        prices.append(price)

print('-----YOUR CART----')
print()

for food in foods:
    print(food, end=' ')

for price in prices:
    total = total + price
print('')
print('Your total is', total)


