import requests
from django.http.response import JsonResponse
from . import serializers

# Create your views here.

token_URL = "https://public-apis-api.herokuapp.com/api/v1/auth/token/"

category_URL = "https://public-apis-api.herokuapp.com/api/v1/apis/categories/?page="


class Postman:

    def get_token(self):
        # Make request for token
        req = requests.get(token_URL)

        # Convert response to JSON object
        token_obj = req.json()

        # Get Token from response object
        token = token_obj["token"]

        return token

    def set_categories(self):
        token = self.get_token()
        headers = {
            "Authorization": "Bearer " + token
        }
        for i in range(1, 6):
            url = category_URL + str(i)
            req = requests.get(url, headers=headers).json()

            for category in req["categories"]:
                data_obj = {
                    "name": category,
                    "page": i
                }
                # user_obj = Categories.objects.create(name=category, page=i)
                # user_obj.save()
                # res = {'msg': "Data Successfully Added to Database !"}
                # return JsonResponse(res)
                serializer = serializers.CategorySerializer(data=data_obj)
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': "Data Successfully Added to Database !"}
                    return JsonResponse(res)
                

                err = {'msg': "Some Error Occured !"}
                return JsonResponse(err)

obj = Postman()
obj.set_categories()
