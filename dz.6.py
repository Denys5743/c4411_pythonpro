import colorama
print(dir(colorama))

from colorama import Fore, Back, Style
print(Fore.RED + "Червоний текст")
print(Back.GREEN + "Зелений фон")
print(Style.RESET_ALL + "Скидання стилю")
