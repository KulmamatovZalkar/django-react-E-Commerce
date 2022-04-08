from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({"info": "React & Django ecommerce", "name": "Zalkar"})
