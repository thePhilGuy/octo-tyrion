from django.conf.urls import patterns, url
from blog.views import ListArticles, ListCategoryArticles, ArticleCreate, ArticleReadComments, ArticleUpdate
from blog.models import Article


urlpatterns = patterns('blog.views',
    url(r'^$', ListArticles.as_view(), name="blog_home"),
    url(r'^category/(\w+)$', ListCategoryArticles.as_view(), name="blog_category"),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)/$', ArticleReadComments.as_view(), name="blog_read"),
    url(r'^write/$', ArticleCreate.as_view(), name="blog_write"),
    url(r'^edit/(?P<id>\d+)-(?P<slug>.+)/$', ArticleUpdate.as_view(), name="blog_edit"),
)
