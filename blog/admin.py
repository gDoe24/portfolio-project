from django.contrib import admin

# Register your models here.
from .models import Blog, Comment

admin.site.register(Blog)



class CommentAdmin(admin.ModelAdmin):

	list_display = ('username', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)