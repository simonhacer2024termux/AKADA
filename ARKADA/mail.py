from dadata import Dadata
from colorama import Fore, Style
from pystyle import Write, Colors

def main():
    Write.Print(f"by @zxcodeee", Colors.red_to_white, interval=0.05)
    print("")
    print("Введите Y что бы подтвердить действие.")
    choice = input("Введите номер действия (Y/n): ")
    if choice == 'Y':
        email = input("Введите Email: ")
        probiv_po_email(email)
    elif choice == 'n':
        exit()
    else:
        print("Некорректный выбор. Пожалуйста, выберите Y или n.")

def probiv_po_email(email):
    token = "c220514125d5e1792311bbed3df7bb9ceda72a4e"
    secret = "ca901148716e394c474ed2f3f6a662dff250a889"
    dadata = Dadata(token, secret)
    result = dadata.clean("email", email)

    # Вывод информации о пробиве по Email
    if isinstance(result, list):
        print("\nИнформация по Email:")
        for item in result:
            print(f"Источник: {item.get('source', 'Нет данных')}")
            print(f"Email: {item.get('email', 'Нет данных')}")
            print(f"Локальная часть: {item.get('local', 'Нет данных')}")
            print(f"Домен: {item.get('domain', 'Нет данных')}")
            print(f"Тип: {item.get('type', 'Нет данных')}")
            print(f"Качество: {item.get('qc', 'Нет данных')}")
    else:
        print("Информация по Email не найдена или некорректна.")

if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода")

print("")


with open("main.py", encoding='utf-8') as file:  # Указываем кодировку файла
    exec(file.read(), globals())

