from rest_framework import serializers

from hbot_dataset.targets.models import Target
from hbot_dataset.vectors.models import TextVector


class TextVectorSerializer(serializers.ModelSerializer):
    target = serializers.PrimaryKeyRelatedField(queryset=Target.objects.all(), write_only=True)
    target_name = serializers.CharField(source='target.name', read_only=True)

    class Meta:
        model = TextVector
        fields = [
            'text',
            'target',
            'target_name',
        ]
