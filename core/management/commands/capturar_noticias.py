from django.core.management import BaseCommand

from core.scrapping import ScrappingManager


class Command(BaseCommand):
    help = 'Captura as notícias dos portais'

    def handle(self, *args, **options):
        manager = ScrappingManager()
        try:
            manager.process()
            self.stdout.write(self.style.SUCCESS('Notícias capturadas!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Algum erro ocorreu!'))
            raise e
