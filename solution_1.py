# Задача 1: Подсчет скидки

def calculate_discount(prices):
    discount_percentage = prices[-1]
    total_discount = 0

    for price in prices[:-1]:
        discount = price * discount_percentage / 100
        total_discount += discount

    return total_discount

prices = [100, 200, 300, 10]
discount = calculate_discount(prices)
print("Сумма скидки на все товары:", int(discount))

prices = [50, 150, 250, 20]
discount = calculate_discount(prices)
print("Сумма скидки на все товары:", int(discount))
