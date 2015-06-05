from django.contrib import admin

from .models import MCU, MCU_TABLE, NOTIFICE, ADMINS, PROCESS, INSPECT, INSPECTORS

admin.site.register(MCU)
admin.site.register(MCU_TABLE)
admin.site.register(NOTIFICE)
admin.site.register(ADMINS)
admin.site.register(PROCESS)
admin.site.register(INSPECT)
admin.site.register(INSPECTORS)
