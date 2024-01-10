from django.shortcuts import render
from django.http import HttpResponse
# create your veiws here
def index(request):
    return HttpResponse("Hello, world!")
    

