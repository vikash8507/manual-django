from django.http import HttpResponse

def index(request):
    return HttpResponse("Hurray! Manually Created Django Application")