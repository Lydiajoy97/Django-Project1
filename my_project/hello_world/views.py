from django.shortcuts import render
from django.http import HttpResponse
# create your veiws here
def index(request):

    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)
    

