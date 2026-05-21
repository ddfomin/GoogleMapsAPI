import requests

# Пропуск ошибки: InsecureRequestWarning: Unverified HTTPS request is being made to host 'swapi.dev'. Adding certificate verification is strongly advised
import urllib3
urllib3.disable_warnings()

def get_films_characters_4() -> tuple[list, str]:
    """Функция возвращает список фильмов, в которых снимался Дарт Вейдер"""
    url = "https://swapi.dev/api/people/4/"
    response_get = requests.get(url, verify=False, timeout=10)
    json_response = response_get.json()
    films = json_response.get("films")
    name = json_response.get("name")
    return films, name

def get_name_characters_with_films_like_4_person() -> list:
    """Функция возвращает список имен персонажей, которые снимались в фильмах Дарт Вейдером"""
    url = "https://swapi.dev/api/people/" # базовый url
    page_number = 1 # номер страницы

    expected_films, name_4_person = get_films_characters_4()

    result_data = set()

    while True:
        # Get-запрос
        response_get = requests.get(f"{url}?page={page_number}", verify=False, timeout=10)

        status_code = response_get.status_code
        # Остановка цикла при ошибке
        assert status_code == 200, f"Ошибка, код ответа {status_code}"

        # Обработка ответа. Формируем список персонажей, которые снимались в фильмах с Дарт Вейдером
        json_response = response_get.json()
        for persona in json_response["results"]:
            name = persona["name"]
            films = persona["films"]

            # Проверяем: есть ли общие фильмы и не сам ли это Вейдер
            if any(film in films for film in expected_films) and name != name_4_person:
                result_data.add(name)

        # Счетчик для перехода по страницам
        if json_response.get("next"):
            page_number += 1
        else:
            break

    return sorted(result_data)

def write_to_file(filename: str = "characters_with_vader.txt"):
    """Сохраняет имена персонажей в файл"""
    characters = get_name_characters_with_films_like_4_person()

    with open(filename, "w", encoding="utf-8") as file:
        for name in characters:
            file.write(name + '\n')

    print(f"\nСохранено {len(characters)} персонажей в файл '{filename}'")


if __name__ == "__main__":
    print("Поиск персонажей, снимавшихся с Дартом Вейдером...\n")
    write_to_file()

    # Выводим содержимое файла
    with open("characters_with_vader.txt", "r", encoding="utf-8") as file:
        print(file.read())