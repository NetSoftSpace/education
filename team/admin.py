from django.contrib import admin

from team.models import Position, Leader, Kafedra, Department

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    fields = ('title',)

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('id','position','created_at')
    fields = ('position','fullname','image','text','created_at')
    readonly_fields = ('created_at','updated_at')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','position','created_at')
    fields = ('position','fullname','image','text','created_at')
    readonly_fields = ('created_at','updated_at')

@admin.register(Kafedra)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('id','position','created_at')
    fields = ('position','fullname','image','text','created_at')
    readonly_fields = ('created_at','updated_at')
