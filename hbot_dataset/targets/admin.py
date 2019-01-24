from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from hbot_dataset.targets.models import Target


class TargetResource(resources.ModelResource):
    class Meta:
        model = Target
        fields = [
            'id',
            'name',
        ]


class TargetAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    __basic_fields = ['name', 'created_at', 'updated_at']
    resource_class = TargetResource
    list_display = __basic_fields
    list_display_links = __basic_fields
    search_fields = __basic_fields


admin.site.register(Target, TargetAdmin)
