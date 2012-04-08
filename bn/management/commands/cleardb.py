from django.core.management.base import BaseCommand, CommandError
from bn.models import MetroStation

class Command(BaseCommand):
    help = 'Clean up database for all bn objects'
    args = 'none'

    def handle(self, *args, **kwargs):
        MetroStation.objects.all().delete()
