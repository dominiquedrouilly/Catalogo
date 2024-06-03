from django.core.management.base import BaseCommand
from django.core import management
from django.core.management.base import BaseCommand
from django.conf import settings
from piezas.models import Model

import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class Command(BaseCommand):
    help = "This command executes every other command related to imports. Doesn't need any arguments."

    def handle(self, *args, **kwargs):

        #Get every shape txt file, to run importShape with that file
        shapes_txt_folder = os.listdir(settings.SHAPE_FOLDER_PATH)
        shapes_txt = [archivo for archivo in shapes_txt_folder if archivo.endswith('.txt')]

        management.call_command('importTags')
        
        for shape in shapes_txt:
            management.call_command('importShape', shape)

        management.call_command('importCulture')

        management.call_command('importModel3D')

        management.call_command('importThumbs')

        management.call_command('importDescriptions')

