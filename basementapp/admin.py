from django.contrib import admin
from .models import mastermodel, home_page, about_page

# Register your models here.
admin.site.register(mastermodel)
admin.site.register(home_page)
admin.site.register(about_page)

