Этот репозиторий содержит скрипты для автоматизированного тестирования веб-страницы с использованием Selenium WebDriver Pytest и программу на Python.

### Требования
- Python 3.13.1 или выше
- Pytest 8.3.5 или выше
Selenium WebDriver 4.28.1 или выше
Google Chrome 136.0.7103.93 или выше
ChromeDriver 136.0.7103.92 или выше

### Установка
Установите Python с официального сайта: https://www.python.org/downloads/
Установите Pytest с помощью pip в командной строке: pip install pytest
Установите Selenium WebDriver с помощью pip: pip install selenium
Скачайте и установите Google Chrome с официального сайта: https://www.google.com/chrome/
Скачайте и установите ChromeDriver с официального сайта: https://chromedriver.chromium.org/downloads

Бибилотеки: 
Pytest: import pytest - библиотека для написания и запуска тестов.
Selenium WebDriver: from selenium import webdriver - библиотека для автоматизации веб-браузеров.
Selenium WebDriver: from selenium.webdriver.common.by import By - модуль для работы с локаторами элементов на странице.
Selenium WebDriver: from selenium.webdriver.support.ui import WebDriverWait - модуль для ожидания загрузки элементов на странице.
Selenium WebDriver: from selenium.webdriver.support import expected_conditions as EC - модуль для работы с ожидаемыми условиями (например, загрузка страницы).

Запуск text_example.py и programma.py:
1. Клонировать репозиторий: git clone https://github.com/KirillKarpuhin/Cloud.ru.internship.git
Настройка окружения
Добавьте путь к ChromeDriver в переменную среды PATH.(если это требуется)
Убедитесь, что Google Chrome и ChromeDriver установлены и работают корректно.

Запуск text_example.py: 
1. Откройте командную строку и создайте виртуальное окружение:python -m venv myenv (замените myenv на имя вашего виртуального окружения).
2. Запустите вир.окружение: *директория\Scripts\activate.bat
3. Перейдите в папку с файлом text_example.py и введите в командной строке: pytest text_example.py или pytest -s -v text_example.py (для подробных данных)
Альтернатива: 
1. Используйте редактор кода, например, Visual Studio Code (VS Code) с необходимыми разрешениями для Python
2. Запустите через терминал VSC:pytest text_example.py или pytest -s -v text_example.py (для подробных данных)

Запуск programma.py: 
1. Откройте командную строку и перейдите в папку с файлом
2. Введите python programma.py
Альтернатива:
1.Используйте редактор кода с необходимыми разрешениями для Python
