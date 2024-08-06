from dadata import Dadata
from colorama import Fore, Style
from pystyle import Write, Colors


def main():
    Write.Print(f"by @zxcodeee", Colors.red_to_white, interval=0.05)
    print("")
    print("Введите Y что бы подтвердить действие.")
    choice = input("Введите номер действия (Y/n): ")
    if choice == 'Y':
        ip_address = input("Введите IP: ")
        probity_po_ip(ip_address)
    elif choice == 'n':
        ip_address = input("Введите IP-адрес для пробива: ")
        probity_po_ipp(ip_address)
    else:
        print("Некорректный выбор. Пожалуйста, выберите Y или n.")


def probity_po_ip(ip_address):
    token = "c220514125d5e1792311bbed3df7bb9ceda72a4e"
    dadata = Dadata(token)
    result = dadata.iplocate(ip_address)

    # Вывод информации о местоположении по IP
    if "location" in result:
        location_data = result["location"]
        print("\nИнформация по IP-адресу:")
        print(f"Местоположение: {location_data.get('value', 'Нет данных')}")
        print(f"Страна: {location_data.get('data', {}).get('country', 'Нет данных')}")
        print(f"Регион: {location_data.get('data', {}).get('region', 'Нет данных')}")
        print(f"Город: {location_data.get('data', {}).get('city', 'Нет данных')}")
    else:
        print("Информация по IP-адресу не найдена.")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода")

# Вызов API сервиса для пробива по IP
token = "c220514125d5e1792311bbed3df7bb9ceda72a4e"
dadata = Dadata(token)
result = dadata.iplocate("46.226.227.20")

print("")

with open("main.py", encoding='utf-8') as file:  # Указываем кодировку файла
    exec(file.read(), globals())
