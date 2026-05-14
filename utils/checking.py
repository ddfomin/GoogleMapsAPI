import json

class Checking:

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, "Ошибка, Статус-код не совпадает"
        print(f"Успешно! Статус код {result.status_code} равен ожидаемому")

    @staticmethod
    def check_json_for_keys_in_the_response(result, expected_value):
        """Метод для проверки наличия ключей в ответе запроса"""
        fields = json.loads(result.text)
        assert list(fields) == expected_value, "Ошибка, Список полей не совпадает"
        print(f"Все ключи ответа присутствуют: {list(fields)}")

    @staticmethod
    def check_json_for_values_in_the_response(result, field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, "Ошибка, Значение поля не совпадает"
        print(f"Значение ключа {field_name} равно ожидаемому: {check_info}")

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса при помощи поиска по определенному слову"""
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f"Обязательное слово {search_word} присутствует в ключе {field_name}")