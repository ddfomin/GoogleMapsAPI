import utils.http_methods as http


class GoogleMapsAPI:
    """Класс содержащий методы для тестирования Google Maps API. Здесь Мы будем хранить все,
    что необходимо для отправки нашего запроса - url, path, body и т.д."""

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    def create_new_place(self):
        """Метод по созданию новой локации"""

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # ресурс метода POST
        post_url = self.base_url + post_resource + self.key
        print(f"URL для метода POST: {post_url}")

        result_post = http.post(post_url, json_for_create_new_place)
        print(f"Ответ в json-формате: {result_post.json()}")
        print(f"Статус код: {result_post.status_code}")

        return result_post


    def get_new_place(self, place_id):
        """Метод для проверки новой локации"""

        get_resource = "/maps/api/place/get/json"  # ресурс метода Get
        get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
        print(f"URL для метода GET: {get_url}")

        result_get = http.get(get_url)
        print(f"Ответ в json-формате: {result_get.json()}")
        print(f"Статус код: {result_get.status_code}")

        return result_get

    def put_new_place(self, place_id):
        """Метод для изменения новой локации"""

        put_resource = "/maps/api/place/update/json"  # ресурс метода Put
        put_url = self.base_url + put_resource + self.key
        print(f"URL для метода PUT: {put_url}")

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = http.put(put_url, json_for_update_new_location)
        print(f"Ответ в json-формате: {result_put.json()}")
        print(f"Статус код: {result_put.status_code}")

        return result_put

    def delete_new_place(self, place_id):
        """Метод для удаления новой локации"""

        delete_resource = "/maps/api/place/delete/json"  # ресурс метода Delete
        delete_url = self.base_url + delete_resource + self.key
        print(f"URL для метода DELETE: {delete_url}")

        json_for_delete_new_location = {
            "place_id": place_id
        }

        result_delete = http.delete(delete_url, json_for_delete_new_location)
        print(f"Ответ в json-формате: {result_delete.json()}")
        print(f"Статус код: {result_delete.status_code}")

        return result_delete