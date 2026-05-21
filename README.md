# 🗺️ Google Maps API Testing Framework

Проект содержит автоматизированные тесты для проверки API геоданных (аналог Google Maps API). Тесты покрывают полный жизненный цикл локаций и CRUD операции

## 📋 О проекте

Этот проект представляет собой pet-project для изучения автоматизации тестирования API. Фреймворк тестирует следующие методы Google Maps API:
- POST `/maps/api/place/add/json` - создание новой локации
- GET `/maps/api/place/get/json` - получение информации о локации
- PUT `/maps/api/place/update/json` - обновление информации о локации
- DELETE `/maps/api/place/delete/json` - удаление локации

## 🛠️ Технологии

- **Python 3.8+** - язык программирования
- **Pytest** - фреймворк для тестирования
- **Allure** - генерация отчетов
- **Requests** - HTTP клиент
- **Allure-pytest** - интеграция Allure с Pytest

## 🧪 Тесты

### 1. `test_complete_places_management` - Цикл операций с пятью локациями

**Описание:** Тест проверяет работу с несколькими локациями одновременно

**Сценарий:**
1. Создание 5 локаций через метод POST
2. Сохранение ID локаций в файл `places.txt`
3. Проверка всех созданных локаций через метод GET
4. Удаление 2-й и 4-й локаций
5. Фильтрация существующих локаций и сохранение в `existing_places.txt`
6. Очистка временных файлов

**Ожидаемый результат:** 
- Создано 5 локаций
- Удалено 2 локации
- Осталось 3 существующие локации

После запуска тестов вы получите:
- ✅ Отчет Allure с графиками и статистикой
- 📝 Логи всех запросов/ответов в папке `logs/`
- 📁 Файлы с place_id: `created_places.txt`, `existing_places.txt`

### 2. `test_create_new_place` - Полный CRUD цикл

**Описание:** Тест проверяет полный жизненный цикл одной локации

**Сценарий:**
1. **POST** `/place/create` - создание новой локации
2. **GET** `/place/get` - проверка создания
3. **PUT** `/place/update` - обновление адреса
4. **GET** `/place/get` - проверка обновления
5. **DELETE** `/place/delete` - удаление локации
6. **GET** `/place/get` - проверка удаления (ожидается 404)

**Данные:**
- Оригинальный адрес: `"29, side layout, cohen 09"`
- Обновленный адрес: `"100 Lenina street, RU"`

**Проверки:**
- Статус коды ответов
- Наличие ключей в JSON ответе
- Значения полей
- Поиск подстроки в сообщении об ошибке

## 🧪 Запуск тестов

### Установка и подготовка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ВАШ_ЛОГИН/GoogleMapsAPI.git
   cd GoogleMapsAPI

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # для Linux/Mac
   .venv\Scripts\activate     # для Windows

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
4. Пример настройки alias для Allure (Указываем путь до allure):
   ```bash
   Set-Alias allure U:\ddfomin_project\allure-2.30.0\bin\allure.bat

5. Запуск всех тестов с очисткой прошлых прохождений:
   ```bash
   pytest -vs --alluredir=tests\allure-results .\tests --clean-alluredir
   
6. Открытие отчета:
   ```bash
   allure serve .\tests\allure-results