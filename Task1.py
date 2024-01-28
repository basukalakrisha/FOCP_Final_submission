def get_positive_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            num = int(user_input)
            if num < 0:
                raise ValueError
            return num
        except ValueError:
            print("Please enter a positive integer!")

def get_yes_or_no(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input
        print('Please answer "Y" or "N".')

def calculate_price(is_tuesday, num_pizzas, is_delivery, is_ordered_via_app):
    pizza_price = 12
    delivery_cost = 2.5 if num_pizzas < 5 and is_delivery else 0
    total_pizza_price = num_pizzas * pizza_price

    if is_tuesday:
        total_pizza_price *= 0.5  # Apply 50% off on total_pizza_price if tuesday

    if is_ordered_via_app:
        total_pizza_price *= 0.75  # Apply 75% off on total_pizza_price  if ordered via app

    #Calculate total_price with total pizza price and delivery cost
    total_price = total_pizza_price + delivery_cost
    return total_price

def main():
    print()
    print("BPP Pizza Price Calculator")
    print("==============")
    

    num_pizzas = get_positive_int("How many pizzas ordered? ")
    is_delivery = get_yes_or_no("Is delivery required? (Y/N) ")
    is_tuesday = get_yes_or_no("Is it Tuesday? (Y/N) ")
    is_ordered_via_app = get_yes_or_no("Did the customer use the app? (Y/N) ")

    total_price = calculate_price(is_tuesday == 'y', num_pizzas, is_delivery == 'y', is_ordered_via_app == 'y')
    print(f"Total price: £{total_price:.2f}")

if __name__ == "__main__":
    main()
