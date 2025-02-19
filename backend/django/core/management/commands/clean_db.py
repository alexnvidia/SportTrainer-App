from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Trainer, Client, Session, Rating, Message

class Command(BaseCommand):
    help = 'Limpia la base de datos, excepto los superusuarios.'

    def handle(self, *args, **kwargs):
        # Eliminar sesiones, calificaciones y mensajes primero para evitar errores de clave foránea
        Session.objects.all().delete()
        Rating.objects.all().delete()
        Message.objects.all().delete()

        # Eliminar clientes y entrenadores, excluyendo aquellos cuyo usuario sea un superusuario
        Trainer.objects.exclude(user__is_superuser=True).delete()
        Client.objects.exclude(user__is_superuser=True).delete()

        # Eliminar usuarios que no sean superusuarios
        User.objects.exclude(is_superuser=True).delete()

        self.stdout.write(self.style.SUCCESS('Limpieza de la base de datos completada.'))