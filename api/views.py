from . import serializers
from . import models
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def set_categories(request):

    if request.method == 'POST':

        serializer_data = serializers.CategorySerializer(data=request.POST)

        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse({'msg': "Data Successfully Added to Database !"})

        return JsonResponse({'msg': "Some Error Occured !"})


@csrf_exempt
def get_categories(request):

    if request.method == 'GET':

        data_list = []

        for i in range(1, 6):
            database_data = list(models.Categories.objects.filter(
                page=i).values("name", "page"))
            data_list.append(database_data)

        return JsonResponse({"data_list": data_list}, safe=False)
