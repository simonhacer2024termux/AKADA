import requests

def check_url_for_viruses(url, api_key):
    params = {'apikey': api_key, 'resource': url}
    response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)

    if response.status_code == 200:
        json_response = response.json()

        if json_response['response_code'] == 1:
            print('Результаты сканирования для', url)
            for scan in json_response['scans']:
                print(f"{scan}: {json_response['scans'][scan]['result']}")
        else:
            print('Результат сканирования недоступен. Попробуйте позже или убедитесь, что ссылка была ранее отсканирована.')
    else:
        print(f'Ошибка при получении результатов сканирования. Код состояния: {response.status_code}')

# Введите ваш API-ключ от VirusTotal
api_key = 'e506a25ef3e8e085e8d5b2582e249affb7ae5cdd0280a781362598ac257ab69a'

# Введите ссылку для проверки
url = input('Введите ссылку для проверки на вирусы: ')

check_url_for_viruses(url, api_key)

print("")


with open("main.py", encoding='utf-8') as file:  # Указываем кодировку файла
    exec(file.read(), globals())
