from django.contrib import admin

from quota.models import Quota

@admin.register(Quota)
class QuotaAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    fields = ('title','image','created_at')
    readonly_fields = ('created_at',)

