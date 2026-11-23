def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total, discount):
    return total - (total * discount / 100)


def main():
    price = 100
    quantity = 3
    total = calculate_total(price, quantity)
    final_price = calculate_discount(total, 10)

    print(final_price)


if __name__ == "__main__":
    main()
