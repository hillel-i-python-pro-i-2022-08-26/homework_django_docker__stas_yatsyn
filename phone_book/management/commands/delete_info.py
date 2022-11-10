import logging

from django.core.management import BaseCommand, CommandParser

from phone_book import models


class Command(BaseCommand):
    help = "Delete amount of users info"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--all",
            help="Delete ALL users",
            action="store_true",
        )

    def handle(self, *args, **options):
        amount_of_user_info = models.Contact.objects.all().count()
        self.logger.info(f"Now amount of users is: {amount_of_user_info}")

        if options["all"]:
            all_info = models.Contact.objects.all()
            answer = input("You try to delete ALL users, are you sure? Y/n \n")
            if answer == "Y":
                all_info.delete()

        db_query = models.Contact.objects.filter(is_auto_generated=True)
        delete_number, details = db_query.delete()

        self.logger.info(f"Delete {delete_number} of users info.")

        number_after_deleting = models.Contact.objects.all().count()
        self.logger.info(f"Current amount of users info is: {number_after_deleting}")
