from django.http import HttpResponse

# Create your views here.
def index(reques):
    return HttpResponse("Spark Horizon! :D")
