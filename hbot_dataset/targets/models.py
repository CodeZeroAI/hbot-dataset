from django.db import models

from hbot_dataset.commons.models import AbstractTimestamp


class Target(AbstractTimestamp):
    """
    Intentionally put wording `Target` instead of `Class`
    Because it is a reserved word
    """
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name
