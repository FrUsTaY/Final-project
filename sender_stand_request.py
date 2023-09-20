import requests
import configuration
import data
def post_new_order(): #функция для создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
           json=data.order_body)

def get_order_info(track_number): #Функция для получения заказа по номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
           params={"t": track_number})