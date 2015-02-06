from django.contrib import admin
from polls.models import Query, Response

class ResponseInline(admin.StackedInline):
    model = Response
    extra = 2

class QueryAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]

admin.site.register(Query, QueryAdmin)
