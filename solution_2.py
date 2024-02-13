# Задача 2: Преобразование RGB в HEX

def convert_to_hex(rgb):
    r, g, b = rgb
    hex_value = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_value

rgb_tuple = (255, 0, 0)
hex_color = convert_to_hex(rgb_tuple)
print("HEX:", hex_color)

rgb_tuple = (0, 250, 0)
hex_color = convert_to_hex(rgb_tuple)
print("HEX:", hex_color)

rgb_tuple = (0, 0, 250)
hex_color = convert_to_hex(rgb_tuple)
print("HEX:", hex_color)