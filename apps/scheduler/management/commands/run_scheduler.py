from django.core.management.base import BaseCommand
from apps.scheduler.services.scheduler_service import SchedulerService


class Command(BaseCommand):
    help = "Ejecuta los jobs programados del sistema"

    def handle(self, *args, **options):
        SchedulerService().run()