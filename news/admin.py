from django.contrib import admin

from news.models import Blog, Category, SubImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class SubImageInline(admin.StackedInline):
    model = SubImage
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (SubImageInline,)
    list_display = ('id','title','created_at')
    fields = ('title','slug','category','image','body','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)

@admin.register(SubImage)
class SubImageAdmin(admin.ModelAdmin):
    list_display = ('id','blog')
    fields = ('blog__title','image')


