import pytest
from generator import register_new_courier_and_return_login_password
from api_client import CourierAPI

@pytest.fixture
def create_courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    payload = {"login": login, "password": password, "firstName": first_name}

    response = CourierAPI.create_courier(payload)
    assert response.status_code == 201, "Курьер не был создан в фикстуре"
   
    yield login, password, first_name
    
    # Финализатор - всегда выполняется после теста
    login_payload = {"login": login, "password": password}
    login_response = CourierAPI.login_courier(login_payload)
    courier_id = login_response.json().get('id')
    CourierAPI.delete_courier(courier_id)
