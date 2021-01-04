from django.contrib import admin
from .models import Artictles
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
     list_display=("")
     search_fields=("")
     list_filter=("")



admin.site.register(Articles,ArticlesAdmin)
