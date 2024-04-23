from .models import Drink
from .serializer import DrinkSerializer
from django.http import JsonResponse


def drink_list(request):
    drinks = Drink.objects.all() #gets the drinks from model
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'drinks': serializer.data}, safe=False)