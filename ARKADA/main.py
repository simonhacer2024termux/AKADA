import requests
from dadata import Dadata
import os
from colorama import Fore, Style
from pystyle import Write, Colors
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon
import hashlib
import os
import time

banner = '''


 █████  ██████  ██   ██  █████  ██████   █████  
██   ██ ██   ██ ██  ██  ██   ██ ██   ██ ██   ██ 
███████ ██████  █████   ███████ ██   ██ ███████ 
██   ██ ██   ██ ██  ██  ██   ██ ██   ██ ██   ██ 
██   ██ ██   ██ ██   ██ ██   ██ ██████  ██   ██ 

Слито в @r0xck
TG: @arkadasoft                                      
======================================================                                                 
| ∫+∫ 1. Пробив по номеру      ∫+∫ 2. Пробив IP(BETA)|
|                                                    |
| ∫+∫ 3. Пробив Mail(BETA)     ∫+∫ 4. Паспорт(BETA)  |
|                                                    |
| ∫+∫ 5. Проверка Сайта        ∫+∫ 6. Arkada Browser |
|                                                    |
|                ∫+∫ 7. Arkada AI(BETA)              |
======================================================                                         
'''

print(Fore.RED + banner)

choice = input("Введите номер действия (1/7): ")
if choice == '1':
    with open("aphone.py", encoding='utf-8') as file:  # Указываем кодировку файла
        exec(file.read(), globals())     
elif choice == '2':
    with open("ip.py", encoding='utf-8') as file:  # Указываем кодировку файла
        exec(file.read(), globals())     
elif choice == '3':
    with open("mail.py", encoding='utf-8') as file:  # Указываем кодировку файла
        exec(file.read(), globals()) 
elif choice == '4':
    with open("pasport.py", encoding='utf-8') as file:  # Указываем кодировку файла
        exec(file.read(), globals()) 
elif choice == '5':
    with open("urlcheck.py", encoding='utf-8') as file:  # Указываем кодировку файла
        exec(file.read(), globals()) 
elif choice == '6':
    with open("browser.py", encoding='utf-8') as file:  # Указываем кодировку файла
        exec(file.read(), globals())
elif choice == '7':
    with open("arkadai.py", encoding='utf-8') as file:  # Указываем кодировку файла
        exec(file.read(), globals())