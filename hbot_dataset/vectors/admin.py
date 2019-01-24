from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from hbot_dataset.vectors.models import TextVector


class TextVectorResource(resources.ModelResource):
    class Meta:
        model = TextVector
        fields = [
            'id',
            'text',
            'target',
        ]


class TextVectorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    __basic_fields = ['text', 'target', 'created_at', 'updated_at']
    resource_class = TextVectorResource
    list_display = __basic_fields
    list_display_links = __basic_fields
    search_fields = __basic_fields


admin.site.register(TextVector, TextVectorAdmin)
