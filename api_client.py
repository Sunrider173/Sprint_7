import requests
from data import Urls


class CourierAPI:
    """Класс для работы с API курьера"""
    
    @staticmethod
    def create_courier(payload):
        """Создание курьера"""
        return requests.post(Urls.COURIER_ENDPOINT, json=payload)
    
    @staticmethod
    def login_courier(payload):
        """Авторизация курьера"""
        return requests.post(Urls.COURIER_LOGIN_ENDPOINT, json=payload)
    
    @staticmethod
    def delete_courier(courier_id):
        """Удаление курьера"""
        return requests.delete(f"{Urls.COURIER_ENDPOINT}/{courier_id}")


class OrderAPI:
    """Класс для работы с API заказа"""
    
    @staticmethod
    def create_order(payload):
        """Создание заказа"""
        return requests.post(Urls.ORDER_ENDPOINT, json=payload)
    
    @staticmethod
    def get_order_list():
        """Получение списка заказов"""
        return requests.get(Urls.ORDER_ENDPOINT)
