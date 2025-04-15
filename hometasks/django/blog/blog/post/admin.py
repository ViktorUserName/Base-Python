from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created', 'updated', 'likes']  # Параметры для отображения в списке
    list_filter = ['created', 'updated', 'user']  # Фильтры для админки
    search_fields = ['title', 'content']  # Поиск по этим полям
    ordering = ['-created']  # Сортировка по дате создания (по убыванию)

admin.site.register(Post, PostAdmin)