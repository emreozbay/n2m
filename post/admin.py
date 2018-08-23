from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['name','recorded_date']
    list_display_links = ['recorded_date']
    list_filter = ['recorded_date']
    search_fields = ['name','surname']
    list_editable = ['name']


    class Meta:
        model = Post


admin.site.register(Post,PostAdmin)
