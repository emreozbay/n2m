from django.contrib import admin
from .models import Post,Department

class PostAdmin(admin.ModelAdmin):
    list_display = ['name','recorded_date','department']
    list_display_links = ['recorded_date']
    list_filter = ['recorded_date']
    search_fields = ['name','surname']
    list_editable = ['name']


    class Meta:
        model = Post


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    class Meta:
        model = Department
    pass


admin.site.register(Post,PostAdmin)

admin.site.register(Department,DepartmentAdmin)
