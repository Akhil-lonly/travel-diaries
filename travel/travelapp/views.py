from django.shortcuts import render
from .models import Place, team


# Create your views here.
def home(request):
    obj1=Place.objects.all()
    obj2 = team.objects.all()
    return render(request, 'index.html', {'result':obj1, 'teams':obj2})

