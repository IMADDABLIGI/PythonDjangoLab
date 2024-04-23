from .models import Drink
from .serializer import DrinkSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT'])
def drink_list(request):
    
    if request.method == 'GET':
        drinks = Drink.objects.all() #gets all the drinks from model
        serializer = DrinkSerializer(drinks, many=True) #Serialaize the drinks
        # print(serializer.data)
        return JsonResponse({'drink': serializer.data}) #return Json
