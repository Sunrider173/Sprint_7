import pytest
import allure
from data import Order
from api_client import OrderAPI

@allure.feature("Создание заказа и просмотр списка заказов")
class TestOrder:
    @allure.title("Создание заказа с черным цветом")
    def test_create_order_black_color(self):
        payload = Order.order_data.copy()
        payload["color"] = ["BLACK"]
        
        response = OrderAPI.create_order(payload)
        
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title("Создание заказа с серым цветом")
    def test_create_order_grey_color(self):
        payload = Order.order_data.copy()
        payload["color"] = ["GREY"]
        
        response = OrderAPI.create_order(payload)
        
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title("Создание заказа с двумя цветами")
    def test_create_order_two_colors(self):
        payload = Order.order_data.copy()
        payload["color"] = ["BLACK", "GREY"]
        
        response = OrderAPI.create_order(payload)
        
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title("Создание заказа без указания цвета")
    def test_create_order_no_color(self):
        payload = Order.order_data.copy()
        # Не добавляем поле color
        
        response = OrderAPI.create_order(payload)
        
        assert response.status_code == 201
        assert 'track' in response.json()
    
    @allure.title("Просмотр списка заказов")
    def test_get_orders_list(self):
        response = OrderAPI.get_order_list()
        
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)