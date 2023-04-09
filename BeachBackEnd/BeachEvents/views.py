from django.shortcuts import HttpResponse


# Create your views here.
def get(request):
    print("this is the ")
    return HttpResponse("Fucking thing")

