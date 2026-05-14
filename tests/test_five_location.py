from utils.checking import Checking
from utils.api import GoogleMapsAPI
import allure


@allure.epic("API Геоданных")
@allure.feature("Управление геоданными")
@allure.story("Полный жизненный цикл локаций")
@allure.title("Цикл операций с пятью локациями")
@allure.description("""Последовательность теста: 
    1. Создание 5 локаций через метод POST
    2. Сохранение их id в файл
    3. Проверка локаций через метод GET
    4. Удаление 2 и 4 локации
    5. Фильтрация и сохранение только существующих""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://wiki.company.com/places-api", name="Документация API")
def test_complete_places_management():
    api = GoogleMapsAPI()
    place_ids = []

    with allure.step("Создание 5 локаций"):
        print("\nСоздание 5 локаций")
        for i in range(5):
            with allure.step(f"Создание локации #{i + 1}"):
                print(f"Создание локации #{i + 1}")
                response = api.create_new_place()
                Checking.check_status_code(response, 200)
                place_ids.append(response.json()["place_id"])

        allure.attach(
            "\n".join(place_ids),
            "Созданные place_id",
            allure.attachment_type.TEXT
        )

    with allure.step("Сохранение ID в файл"):
        print("\nСохранение ID в файл")
        with open("places.txt", "w") as f:
            f.write("\n".join(place_ids))
        allure.attach("Данные сохранены в places.txt", "Информация", allure.attachment_type.TEXT)

    with allure.step(f"Проверка получения всех {len(place_ids)} локаций"):
        print(f"\nПроверка получения всех {len(place_ids)} локаций")
        with open("places.txt") as f:
            for idx, place_id in enumerate(f.read().splitlines(), 1):
                with allure.step(f"Проверка #{idx}: локация {place_id[:8]}..."):
                    print(f"Проверка #{idx}: локация {place_id[:8]}...")
                    response = api.get_new_place(place_id)
                    assert response.status_code == 200, f"Локация {place_id} не найдена"
                    allure.attach(
                        response.text,
                        f"Ответ для {place_id}",
                        allure.attachment_type.JSON
                    )

    with allure.step("Удаление 2-й и 4-й локаций"):
        print("\nУдаление 2-й и 4-й локаций")
        with open("places.txt") as f:
            ids = f.read().splitlines()

        with allure.step(f"Удаление 2-й локации: {ids[1]}"):
            print(f"\nУдаление 2-й локации: {ids[1]}")
            api.delete_new_place(ids[1])

        with allure.step(f"Удаление 4-й локации: {ids[3]}"):
            print(f"\nУдаление 4-й локации: {ids[3]}")
            api.delete_new_place(ids[3])

        allure.attach(
            f"Удалены:\n{ids[1]}\n{ids[3]}",
            "Удаленные ID",
            allure.attachment_type.TEXT
        )

    with allure.step("Фильтрация существующих локаций"):
        print("\nФильтрация существующих локаций")
        with open("places.txt") as f:
            all_ids = f.read().splitlines()

        existing = []
        for place_id in all_ids:
            response = api.get_new_place(place_id)
            if response.status_code == 200:
                existing.append(place_id)

        with open("existing_places.txt", "w") as f:
            f.write("\n".join(existing))

        allure.attach(
            f"Существуют: {len(existing)} из {len(all_ids)}\n" + "\n".join(existing),
            "Результат фильтрации",
            allure.attachment_type.TEXT
        )

        print(f"\nОжидалось 3 существующие локации, получено {len(existing)}")
        assert len(existing) == 3, f"Ожидалось 3 существующие локации, получено {len(existing)}"