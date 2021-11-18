from django.contrib import admin
from . models import Home, Devotion, Branches


# Register your models here.
admin.site.register(Home)
admin.site.register(Devotion)
admin.site.register(Branches)



admin.site.site_url = "/home"