from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from hbot_dataset.targets.api.serializers import TargetSerializer
from hbot_dataset.targets.models import Target


class TargetFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Target
        fields = [
            'name',
        ]


class TargetViewSet(viewsets.ModelViewSet):
    """
    Same reason as `TextVectorViewSet`
    """
    permission_classes = ()
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = TargetFilter
