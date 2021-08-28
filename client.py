import json
import requests

token_URL = "https://public-apis-api.herokuapp.com/api/v1/auth/token/"

category_URL = "https://public-apis-api.herokuapp.com/api/v1/apis/categories/?page="


class Postman:

    # GET Request to Postman API to get Token 
    def get_token(self):
        # Make request for token
        req = requests.get(token_URL)

        # Convert response to JSON object
        token_obj = req.json()

        # Get Token from response object
        token = token_obj["token"]

        return token

    # GET Request to Postman API to get Data List and Store in Local Database Via POST Request to Django Server
    def set_categories(self):
        token = self.get_token()
        headers = {
            "Authorization": "Bearer " + token
        }
        for i in range(1, 6):
            url = category_URL + str(i)
            req = requests.get(url, headers=headers)
            req = req.json()

            for category in req["categories"]:
                data_obj = {
                    "name": category,
                    "page": i
                }

                store_data = requests.post(
                    "http://127.0.0.1:8000/set-categories/", data_obj)

                response = json.loads(store_data.content)["msg"]

                print(response)

    # GET Request to django server to get data from Database which we have store using above method
    def get_categories(sefl):
        get_database_data = requests.get(
            "http://127.0.0.1:8000/get-categories/")

        response = json.loads(get_database_data.content)["data_list"]

        for data_list in response:
            for data in data_list:
                print(data, end="\n")
            print(end="\n")


obj = Postman()

# Get data from API and Store in Local Database
obj.set_categories()

# Get data from Local Database and Print
obj.get_categories()
