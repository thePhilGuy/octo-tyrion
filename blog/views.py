# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Article, Category, Comment
from blog.forms import ArticleForm, CommentForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView

class ListArticles(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/home.html"
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(ListArticles, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        return Article.objects.order_by('-date')
    
class ListCategoryArticles(ListArticles):
    def get_queryset(self):
        return Article.objects.filter(category__id=self.args[0]).order_by('-date')
    
    
class ArticleCreate(CreateView):
    model = Article
    template_name = 'blog/write.html'
    form_class = ArticleForm
    
class ArticleRead(DetailView):
    context_object_name = 'article'
    model = Article
    template_name = 'blog/read.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleRead, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(object_id=context['article'].id)
        return context

class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'blog/write.html'
    form_class = ArticleForm
    
class ArticleReadComments(CreateView):
    model = Comment
    template_name = 'blog/read_comments.html'
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super(ArticleReadComments, self).get_context_data(**kwargs)
        article_id = self.kwargs.get('id', None)
        article_slug = self.kwargs.get('slug', None)
        article = get_object_or_404(Article, id = article_id, slug = article_slug)
        context['article'] = article
        context['comments'] = Comment.objects.filter(object_id=context['article'].id)
        return context
    
    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        article_id = self.kwargs.get('id', None)
        article_slug = self.kwargs.get('slug', None)
        self.object.content_object = get_object_or_404(Article, id = article_id, slug = article_slug)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    