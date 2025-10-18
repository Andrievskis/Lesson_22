from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'image', 'is_published', 'views_count')
    list_filter = ('created_at',)
