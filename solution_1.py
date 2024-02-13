# Задача 1: Подсчет скидки

prices_and_discounts = input("Введите цены и скидку: ")
input_data = [float(x) for x in prices_and_discounts.split(', ')]
def calculate_discount(input_data):
    price = input_data[:-1]
    sum_price = sum(price)
    discount = sum_price * (input_data[-1] / 100)
    return discount
print('Сумма скидки: ', calculate_discount(input_data))
