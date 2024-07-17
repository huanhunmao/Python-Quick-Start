available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Add {requested_topping} successfully!')
    else:
        print(f"Sorry, we don't have {requested_topping}")

# Add mushrooms successfully!
# Sorry, we don't have french fries
# Add extra cheese successfully!