from django.shortcuts import render
from .models import Portfolio, Client, Service
from .forms import MessageForm

# Create your views here.


def home(request):
    portfolios = Portfolio.objects.all()
    clients = Client.objects.all()
    services = Service.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            content = {
                'portfolios': portfolios,
                'clients': clients,
                'services': services,
                'success': True
            }
            return render(request, 'home/home.html', content,)
    form = MessageForm()        
    content = {
        'portfolios': portfolios,
        'clients': clients,
        'services': services,
        'form':form
    }
    return render(request, 'home/home.html', content)
