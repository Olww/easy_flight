from django.contrib import admin
from tickets.models import Tickets

class TicketsAdmin(admin.ModelAdmin):
    fields = ['tickets_from' , 'tickets_to' , 'tickets_date','tickets_datetime' , 'tickets_class' ,
    'tickets_places', 'tickets_user', 'tickets_price', 'tickets_paid']
    list_display = ('tickets_from','tickets_to', 'tickets_places', 'tickets_user', 'tickets_price', 'tickets_paid')
admin.site.register(Tickets, TicketsAdmin)




# Register your models here.
