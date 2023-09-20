# Алексей Смолин, 8а когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
def get_track_number_of_order(): #Функция для сохранения номера заказа
    track_number = sender_stand_request.post_new_order()
    return track_number.json()["track"]

# Тест 1. Запрос на получение заказа по треку заказа
def test_create_and_track_order():
    track_number = get_track_number_of_order()
    get_response = sender_stand_request.get_order_info(track_number)
    assert get_response.status_code == 200