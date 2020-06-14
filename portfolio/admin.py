from django.contrib import admin
from .models import Portfolio, Client, Service, Message

# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Message)
