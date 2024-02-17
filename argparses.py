import argparse

# Створюємо парсер
parser = argparse.ArgumentParser(description='Опис програми')

# Додаємо аргументи
parser.add_argument('filename', help='Ім\'я файлу для обробки')
parser.add_argument('--verbose', '-v', action='store_true', help='Додатковий вивід')

# Отримуємо аргументи з командного рядка
args = parser.parse_args()

# Виводимо аргументи
print('Ім\'я файлу:', args.filename)
print('Додатковий вивід:', args.verbose)
