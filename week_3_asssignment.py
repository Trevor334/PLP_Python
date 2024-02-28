def get_price():
    user_input = input(
        'Enter original price and the discount percentage: '
        ).split(' ')
    price = int(user_input[0])
    discount_percent = int(user_input[-1])
    def calculate_discount(price, discount_percent):
        if (discount_percent / 100) >= 0.2:
            price_disc = price * (1-(discount_percent / 100))
            return price_disc
        else:
            return price
    return calculate_discount(price, discount_percent)
get_price()
