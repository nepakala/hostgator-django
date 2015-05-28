from django.contrib import admin

# Register your models here.
from mapmaker.models import City

class CityAdmin(admin.ModelAdmin):
    exclude  = ('client',)
    list_display = ('location', 'name',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.client = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(CityAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(client=request.user)

admin.site.register(City,CityAdmin)
