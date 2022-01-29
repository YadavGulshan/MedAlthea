from django.contrib import admin

# Register your models here.
from .models import Medical, Medicine
admin.site.register(Medical)
admin.site.register(Medicine)