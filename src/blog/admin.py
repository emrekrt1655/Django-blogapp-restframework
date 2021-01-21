from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Like, Comment, PostView


# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    exclude = ('slug',)
    list_display = ( 'id' , 'title', 'category', 'date_created' )
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(PostView)