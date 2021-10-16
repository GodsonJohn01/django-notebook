from django.contrib import admin
from .models import Snippet, Tag

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('last_modified',)

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Tag)
