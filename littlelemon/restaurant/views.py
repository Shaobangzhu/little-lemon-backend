from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')