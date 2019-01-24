from django.db import models

from hbot_dataset.commons.models import AbstractTimestamp
from hbot_dataset.targets.models import Target


class TextVector(AbstractTimestamp):
    text = models.CharField(max_length=300)
    target = models.ForeignKey(Target, related_name='vectors', related_query_name='vectors',
                               null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text[:10] + '...'
