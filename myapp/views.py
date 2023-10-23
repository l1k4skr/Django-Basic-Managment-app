from django.http import HttpResponse



# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

# Create an about page
def about(request):
    return HttpResponse("<h1>This is the about page.</h1>")