import requests
import json

print("ArkadaAI - BETA")
print("")

def search_wikipedia():
    search_query = input("Введите ваш запрос: ")

    url = f"https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=&explaintext=&titles={search_query}"
    response = requests.get(url)
    data = response.json()

    page = next(iter(data["query"]["pages"].values()))
    if "extract" in page:
        print(page["extract"])
    else:
        print("Ничего не найдено. Попробуйте изменить запрос.")

while True:
    search_wikipedia()
    
    choice = input("Хотите выполнить новый поиск? (да/нет): ")
    if choice.lower() == "нет":
        print("Программа завершена.")
        print("")
    with open("main.py", encoding='utf-8') as file: 
        exec(file.read(), globals())