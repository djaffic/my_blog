from django.contrib import admin
from .models import Post


admin.site.site_title = "Мой блог"
admin.site.site_header = "Мой блог"

admin.site.register(Post)


