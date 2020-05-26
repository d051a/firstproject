from django.test import TestCase

# Create your tests here.
from django.apps import apps
apps.get_models('tokensapp')