from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Trainer, Client, Session, Rating, Message

# Extender el UserAdmin para incluir campos relacionados con Trainer y Client
class TrainerInline(admin.StackedInline):
    model = Trainer
    can_delete = False
    verbose_name_plural = 'Trainers'
    fk_name = 'user'

class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'Clients'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (TrainerInline, ClientInline)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

# Registrar el UserAdmin personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Configuración del administrador para Trainer
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'phone', 'bio')
    search_fields = ('user__username', 'specialization', 'phone')
    list_filter = ('specialization',)
    fieldsets = (
        (None, {
            'fields': ('user', 'specialization', 'phone', 'bio')
        }),
    )

# Configuración del administrador para Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'trainer')
    search_fields = ('user__username', 'trainer__user__username')
    list_filter = ('trainer',)
    fieldsets = (
        (None, {
            'fields': ('user', 'trainer')
        }),
    )

# Configuración del administrador para Session
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'client', 'date', 'attended', 'cancelled')
    search_fields = ('trainer__user__username', 'client__user__username', 'date')
    list_filter = ('date', 'attended', 'cancelled')
    fieldsets = (
        (None, {
            'fields': ('trainer', 'client', 'date', 'attended', 'cancelled', 'notes')
        }),
    )

# Configuración del administrador para Rating
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('session', 'rating')
    search_fields = ('session__client__user__username', 'rating')
    list_filter = ('rating',)
    fieldsets = (
        (None, {
            'fields': ('session', 'rating')
        }),
    )

# Configuración del administrador para Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('timestamp',)
    fieldsets = (
        (None, {
            'fields': ('sender', 'receiver', 'content')
        }),
    )