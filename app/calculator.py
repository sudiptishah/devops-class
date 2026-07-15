def apply_discount(amount, discount_percent):
    # Rule 1: the amount must be more than 0
    if amount <= 0:
        raise ValueError("amount must be > 0")
    # Rule 2: the discount must be between 0 and 80
    if discount_percent < 0 or discount_percent > 80:
        raise ValueError("discount must be between 0 and 80")

    # Work out the new price and round to 2 decimals
    discounted = amount * (1 - discount_percent / 100)
    return round(discounted, 2)
