from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'dashboard.html', context=context)