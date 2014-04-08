from django.contrib import admin
from blog.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'category', 'preview')
    list_filter = ('author', 'category')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('title', 'content')
    
    def preview(self, article):
        text = article.content[0:40]
        if len(article.content) > 40:
            return '%s...' % text
        else:
            return text


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
