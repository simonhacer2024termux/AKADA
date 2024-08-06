from dadata import Dadata
from colorama import Fore, Style
from pystyle import Write, Colors

def probiv_po_passport(service_number, passport_number):
    token = "c220514125d5e1792311bbed3df7bb9ceda72a4e"
    secret = "ca901148716e394c474ed2f3f6a662dff250a889"
    dadata = Dadata(token, secret)
    result = dadata.clean("passport", f"{service_number} {passport_number}")

    # Вывод информации о паспорте
    print("\nИнформация по паспорту:")
    for item in result:
        print(f"Источник: {item.get('source', 'Нет данных')}")
        print(f"Серия: {item.get('series', 'Нет данных')}")
        print(f"Номер: {item.get('number', 'Нет данных')}")
        print(f"Качество: {item.get('qc', 'Нет данных')}")

def probiv_po_fms_unit(query, region_code=None, type=None):
    token = "c220514125d5e1792311bbed3df7bb9ceda72a4e"
    dadata = Dadata(token)
    
    filters = []
    if region_code:
        filters.append({"region_code": region_code})
    if type:
        filters.append({"type": type})
    
    result = dadata.suggest("fms_unit", query, filters=filters)

    # Вывод информации о fms_unit
    print("\nИнформация о fms_unit:")
    for item in result:
        print(f"Результат: {item.get('result', 'Нет данных')}")
        # Добавьте необходимые поля для вывода

def main():
    Write.Print(f"by @zxcodeee", Colors.red_to_white, interval=0.05)
    print("")
    print("Введите Y что бы подтвердить действие.")
    choice = input("Введите номер действия (Y/n): ")
    if choice == 'Y':
        service_number = input("Введите серию и номер паспорта: ")
        passport_number = input("Введите номер паспорта: ")
        probiv_po_passport(service_number, passport_number)
        
        query = input("Введите запрос для fms_unit: ")
        region_code = input("Введите код региона (если есть): ")
        type = input("Введите тип (если есть): ")
        probiv_po_fms_unit(query, region_code, type)
    elif choice == 'n':
        exit()
    else:
        print("Некорректный выбор. Пожалуйста, выберите Y или n.")

if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода")

print("")


with open("main.py", encoding='utf-8') as file:  # Указываем кодировку файла
    exec(file.read(), globals())