from rest_framework import serializers

from hbot_dataset.targets.models import Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = [
            'name',
        ]
