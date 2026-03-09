import os
import random
import sys


def check_current_year():
    filename = "current_year.txt"

    if not os.path.isfile(filename):
        print("Ошибка: файл current_year.txt не найден")
        return False

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if content != "2026":
        print("Ошибка: неверное значение в файле current_year.txt")
        return False

    return True


def check_counter():
    filename = "counter.txt"

    if not os.path.isfile(filename):
        print("Ошибка: файл counter.txt не найден")
        return False

    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    expected = [str(i) for i in range(1, 11)]

    if lines != expected:
        print("Ошибка: counter.txt должен содержать числа от 1 до 10 по одному в строке")
        return False

    return True


def check_error_files():
    files = os.listdir(".")

    error_files = [f for f in files if f.endswith(".error")]

    if error_files:
        print("Ошибка: найдены файлы с расширением .error:")
        for f in error_files:
            print(f"  {f}")
        return False

    return True


def main():
    ok = True

    if not check_current_year():
        ok = False
        exit()

    if not check_counter():
        ok = False
        exit()

    if not check_error_files():
        ok = False
        exit()

    if ok:
        print("Все проверки успешно пройдены")
        print("Ваш секретный код доступа", random.randint(0, 0xFFFFFFFFFFFF))
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()