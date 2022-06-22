from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home(request):
    print(settings.STATIC_URL, settings.STATIC_ROOT)
    return render(request, 'coralnet/home.html', {})
