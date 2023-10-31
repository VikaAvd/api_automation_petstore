import pytest
import payloads

def test_post_new_user_to_the_store(api):
    # check adding a new user to the store
    response = api.create_user(payloads.user_data)
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['code'] == 200, 'Incorrect code in response'
    assert response.json()['type'] == 'unknown', 'Incorrect type in response'

def test_create_users(api):
    # check creating a list of users
    users_data = [payloads.user_data, payloads.user_data]  # list of users
    response = api.create_users(users_data)
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['code'] == 200, 'Incorrect code in response'
    assert response.json()['message'] == 'ok', 'Incorrect message in response'

def test_user_login(api):
    # check user login
    username = payloads.user_data['username']
    password = payloads.user_data['password']
    response = api.login_user(username, password)
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['code'] == 200, 'Incorrect code in response'
    assert response.json()['type'] == 'unknown', 'Incorrect type in response'

def test_user_logout(api):
    # check user logout
    response = api.logout_user()
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['code'] == 200, 'Incorrect code in response'
    assert response.json()['message'] == 'ok', 'Incorrect message in response'

def test_post_new_pet_to_the_store(api):
    # check POST a new pet to the store
    response = api.create_pet(payloads.pet_data)
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['name'] == payloads.pet_data['name'], 'Incorrect pet object added'

def test_update_pet(api):
    # check updating a pet's name and status
    response = api.update_pet(payloads.updated_pet_data)
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['name'] == payloads.updated_pet_data['name'], 'Incorrect name in response'
    assert response.json()['status'] == payloads.updated_pet_data['status'], 'Incorrect status in response'

def test_update_pet_image(api):
    # check updating a pet's image
    pet_id = payloads.pet_data['id']  # get the pet ID from the payload
    image_file = 'C:/Users/Viktoriya_Avdiyenko/Desktop/SQE/Python/Python_Automation/automation_project/api_automation_petstore/dog.jpg'  # replace with your image file path
    response = api.update_pet_image(pet_id, image_file)
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['code'] == 200, 'Incorrect code in response'

def test_delete_pet(api):
    # check deleting a pet
    pet_id = payloads.pet_data['id']  # get the pet ID from the payload
    response = api.delete_pet(pet_id)
    assert response.status_code == 200, 'Response status code is not 200'
    assert response.json()['code'] == 200, 'Incorrect code in response'