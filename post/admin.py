from django.contrib import admin
from .models import Post,Department

class PostAdmin(admin.ModelAdmin):
    list_display = ['name','recorded_date']
    list_display_links = ['recorded_date']
    list_filter = ['recorded_date']
    search_fields = ['name','surname']
    list_editable = ['name']


    class Meta:
        model = Post
class PostDepartment(admin.ModelAdmin):
    list_editable = ['department']
    list_display = ['department']
    list_display_links = ['department']
    class Meta:
        model = Department

admin.site.register(Post,PostAdmin,Department)
