from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def about_us(request):
    return render(request, 'about_us_app/index.html')