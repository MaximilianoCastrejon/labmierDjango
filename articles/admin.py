from django.contrib import admin

# Register your models here.

from .models import Article, Users

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Article, ProfileAdmin)
admin.site.register(Users)