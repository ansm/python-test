from django.contrib import admin
from .models import * 

# Register your models here.
class UniversitiesAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('Post data', {'fields': ('name', 'logo', 'website')}),
	    ('Date', {'fields': ('created_date','modified_at')}),
	    ('Permission', {'fields': ('is_active', )}),
	)

	exclude = ('published_date',)

	search_fields = ('name',)
	ordering = ('-created_date',)
	list_display = ('name', 'logo', 'website')
	list_display_links = ('name',)
	list_filter = ('name',)

	def enable(self, request, queryset):
		queryset.update(is_active=True)


admin.site.register(Universities, UniversitiesAdmin)
admin.site.register(School)
admin.site.register(Address)
admin.site.register(Student)