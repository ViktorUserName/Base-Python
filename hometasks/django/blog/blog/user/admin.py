
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_active', 'is_staff']
    list_filter = ['role', 'is_active', 'is_staff']
    search_fields = ['username', 'email']
    ordering = ['username']

    # Добавить поля для создания и изменения пользователя
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_active', 'is_staff')
        }),
    )


# Регистрируем кастомного пользователя
admin.site.register(User, CustomUserAdmin)