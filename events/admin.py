from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "venue", "date")
    prepopulated_fields = {"slug": ("title",)}
from django.contrib import admin

# Register your models here.
