import json
import requests

BASE_URL = 'https://petstore.swagger.io/v2'

class PetstoreAPI:
    def __init__(self, url) -> None:
        self.base_url = url
  
    def create_user(self, user_data):
        # method to add a new user 
        post_user_url = f"{self.base_url}/user"
        headers = {
              'accept': 'application/json',
              'Content-Type': 'application/json'
        }
        response = requests.post(
            post_user_url, data=json.dumps(user_data), headers=headers
        )
        return response

    def create_users(self, users_data):
        # method to create a list of users
        create_users_url = f"{self.base_url}/user/createWithArray"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.post(
            create_users_url, data=json.dumps(users_data), headers=headers
        )
        return response

    def login_user(self, username, password):
        # method to login a user
        login_url = f"{self.base_url}/user/login"
        params = {
            'username': username,
            'password': password
        }
        headers = {
            'accept': 'application/json',
        }
        response = requests.get(login_url, params=params, headers=headers)
        return response
    
    def logout_user(self):
        # method to logout a user
        logout_url = f"{self.base_url}/user/logout"
        headers = {
            'accept': 'application/json',
        }
        response = requests.get(logout_url, headers=headers)
        return response

    def create_pet(self, pet_data):
        # method to add a new pet to the store
        post_pet_url = f"{self.base_url}/pet"
        headers = {
              'accept': 'application/json',
              'Content-Type': 'application/json'
        }
        response = requests.post(
            post_pet_url, data=json.dumps(pet_data), headers=headers
        )
        return response

    def update_pet(self, updated_pet_data):
        # method to update a pet's name and status
        update_pet_url = f"{self.base_url}/pet"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        response = requests.put(
            update_pet_url, data=json.dumps(updated_pet_data), headers=headers
        )
        return response

    def update_pet_image(self, pet_id, image_file):
        # method to update a pet's image
        update_image_url = f"{self.base_url}/pet/{pet_id}/uploadImage"
        headers = {
            'accept': 'application/json'
        }
        with open(image_file, 'rb') as f:
            files = {'file': f}
            response = requests.post(update_image_url, headers=headers, files=files)
        return response

    def delete_pet(self, pet_id):
        # method to delete a pet
        delete_pet_url = f"{self.base_url}/pet/{pet_id}"
        headers = {
            'accept': 'application/json',
        }
        response = requests.delete(delete_pet_url, headers=headers)
        return response