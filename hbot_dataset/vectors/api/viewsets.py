from django.http import HttpResponse
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from hbot_dataset.vectors.admin import TextVectorResource
from hbot_dataset.vectors.api.serializers import TextVectorSerializer
from hbot_dataset.vectors.models import TextVector


class TextVectorFilter(filters.FilterSet):
    text = filters.CharFilter(field_name='text', lookup_expr='icontains')
    target = filters.CharFilter(field_name='target__name', lookup_expr='icontains')

    class Meta:
        model = TextVector
        fields = (
            'text',
            'target',
        )


class TextVectorViewSet(viewsets.ModelViewSet):
    """
    Get rid of clumsy permission by EC2 firewall
    `/download` to download the records
    """
    permission_classes = ()
    queryset = TextVector.objects.all()
    serializer_class = TextVectorSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = TextVectorFilter

    @action(detail=False)
    def download(self, request):
        dataset = TextVectorResource().export()
        file = open("text_vectors.csv", "w")
        file.write(dataset.csv)
        file.close()

        text_file = open("text_vectors.csv", 'r')
        response = HttpResponse(text_file.read(), content_type='application/file')
        response['Content-Disposition'] = 'attachment; filename=dataset.csv'
        return response
