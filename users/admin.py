from django.contrib import admin

from users.models import User

# # Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'avatar', 'phone', 'country', 'is_active', 'is_staff',
                    'is_superuser', 'date_joined', 'last_login')
    list_filter = ('id',)
