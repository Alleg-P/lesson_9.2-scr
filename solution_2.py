# Задача 2: Преобразование RGB в HEX

def convert_to_hex(rgb):
    r, g, b = rgb
    hex_value = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_value

while True:
    rgb_input = input("Введите значения RGB: ")
    rgb_values = rgb_input.split(',')
    
    if len(rgb_values) != 3:
        print("Ошибка: Введите три значения цвета.")
        continue
    
    try:
        r, g, b = map(int, rgb_values)
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("Ошибка: Значения цвета должны быть в диапазоне от 0 до 255.")
            continue
    except ValueError:
        print("Ошибка: Введите числовые значения цвета.")
        continue
    
    break

rgb = (r, g, b)
hex_value = convert_to_hex(rgb)
print("HEX: ", hex_value)
