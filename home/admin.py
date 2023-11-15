from django.contrib import admin

from home.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','created_at')
    fields = ('name','surname','image','description')
    readonly_fields = ('created_at','updated_at')


