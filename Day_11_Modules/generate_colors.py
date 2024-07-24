from list_of_rgb_colors import list_of_rgb_colors
from list_of_hexa_colors import list_of_hexa_colors
def generate_colors(hexa_or_rgb, number_of_hexa_or_rgb):
    if hexa_or_rgb == 'hexa':
        list_of_hexa_colors(number_of_hexa_or_rgb)
    if hexa_or_rgb == 'rgb':
        list_of_rgb_colors(number_of_hexa_or_rgb)
generate_colors('hexa',2)
generate_colors('rgb',5)