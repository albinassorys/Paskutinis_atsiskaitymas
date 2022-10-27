from django.contrib import admin
from .models import Notes, Category


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')


admin.site.register(Category)
admin.site.register(Notes)