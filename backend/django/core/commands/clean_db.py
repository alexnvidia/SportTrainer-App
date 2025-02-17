from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Trainer, Client, Session, Rating, Message

class Command(BaseCommand):
    help = 'Limpia la base de datos, excepto el usuario admin.'

    def handle(self, *args, **kwargs):
        # Eliminar todos los registros excepto el usuario admin
        User.objects.exclude(username='admin').delete()
        Trainer.objects.all().delete()
        Client.objects.all().delete()
        Session.objects.all().delete()
        Rating.objects.all().delete()
        Message.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Limpieza de la base de datos completada.'))