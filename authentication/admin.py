from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'is_superuser']
    ordering = ['email']
    actions = ['make_active']

    @admin.action(description=_('Activate selected users'))
    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, _('%d users were successfully activated.' % updated))
