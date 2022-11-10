import logging

from django.core.management import BaseCommand, CommandParser

from phone_book import models
from phone_book.services.generate_phone_book import organize_info


class Command(BaseCommand):
    help = "Generate some amount of phone book info"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "amount",
            type=int,
            metavar="NUMBER",
            default=10,
            help="generate amount of users info (by default it's 10 users)",
        )
        parser.add_argument(
            "-i",
            "--ignore",
            action="store_true",
            help="generate users with is_auto_generate=False",
        )

    def handle(self, *args, **options):  # sourcery skip: raise-specific-error
        amount: int = options["amount"]
        self.logger.info(f"Generate {amount} of users info")
        number_of_generations = models.PhoneBook.objects.all().count()
        self.logger.info(f"Now amount of users info is: {number_of_generations}")

        for count, info in enumerate(organize_info(amount=amount), start=1):
            self.logger.info(f"Generate: {count} of {amount}")
            if not options["ignore"]:
                info.is_auto_generated = True
            if options["amount"] > 100:
                raise Exception("It's going to be hard to delete")
            info.save()
            self.logger.info(f"Generate {count} of {amount} DONE")

        info_after_generation = models.PhoneBook.objects.all().count()
        self.logger.info(f"Amount of data:{info_after_generation}")