import requests
from dadata import Dadata
from pystyle import Write, Colors
import json
import phonenumbers
from phonenumbers import geocoder, carrier

def main():
    Write.Print(f"by @zxcodeee", Colors.red_to_white, interval=0.05)
    print("")
    print("Введите Y что бы подтвердить действие.")
    choice = input("Введите номер действия (Y/n): ")
    if choice == 'Y':
        number = input("Введите номер телефона для пробива 79000000000: ")
        probiv_po_nomeru(number)
    elif choice == 'n':
        exit()
      
    else:
        print("Некорректный выбор. Пожалуйста, выберите Y или n.")
def probiv_po_nomeru(number):
    
    url = f"https://phonevalidation.abstractapi.com/v1/?api_key=5bab5899f8ff4275969921984cf9be31&phone={number}"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer c220514125d5e1792311bbed3df7bb9ceda72a4e'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        
        if "valid" in data:
            status = data["valid"]
        else:
            status = "Нет данных"

        if "country" in data and "name" in data["country"]:
            country = data["country"]["name"]
        else:
            country = "Нет данных"

        if "carrier" in data and "type" in data["carrier"]:
            carrier_type = data["carrier"]["type"]
        else:
            carrier_type = "Нет данных"

        if "messaging_apps" in data:
            messengers = data["messaging_apps"]
            print("Мессенджеры:")
            for messenger in messengers:
                print(("app", "Нет данных") + ": " + ("phone", "Нет данных"))

        if "carrier" in data and "name" in data["carrier"]:
            mobile_operator = data["carrier"]["name"]
        else:
            mobile_operator = "Нет данных"

       
        print("Статус:", status)
        print("Страна:", country)
        print("Тип номера:", carrier_type)
        print("Мобильный оператор:", mobile_operator)

       
        print("\nИнформация о социальных сетях:")
        print(f"Telegram: t.me/{number}")
        print(f"WhatsApp: https://api.whatsapp.com/send?phone={number}")
        print(f"Viber: https://viber://add?number={number}")
    else:
        print("Ошибка при получении данных. Пожалуйста, попробуйте позже.")


    token = "c220514125d5e1792311bbed3df7bb9ceda72a4e"
    secret = "ca901148716e394c474ed2f3f6a662dff250a889"
    dadata = Dadata(token, secret)
    result = dadata.clean("phone", number)
    print("\n Доп.Данные:")
    print(result)


    print("")
    print("Инфа.доп")
    print(f"http://num.voxlink.ru/get/?num={number}")
    print(f"https://apigw.intradesk.ru/settings/odata/Clients?$skip=0&$orderby= name%20desc&$top=30&$filter=(contains(phoneNumbersSearch, '{number}'))&$count=true")
    print("")
    print("Ниже пишем заного номер но уже без +")
    print(f"https://getscam.com/{number}")
    print(f"https://htmlweb.ru/json/mnp/phone/{number}")
    print(f"https://htmlweb.ru/json/mnp/phone/{number}")


if __name__ == "__main__":
    main()

print("")


with open("main.py", encoding='utf-8') as file:  
    exec(file.read(), globals())

