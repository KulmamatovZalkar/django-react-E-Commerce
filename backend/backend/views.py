from django.http import HttpResponse

# Create your views here.


def default(request):
    return HttpResponse("<h1>Api Home</h1>")
