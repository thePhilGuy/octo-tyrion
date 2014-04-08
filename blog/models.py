#-*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.
class Article(models.Model):
    '''This class defines Articles in the blog'''
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date published")
    category = models.ForeignKey('Category')
    comments = generic.GenericRelation('Comment')
    
    def __unicode__(self): 
        '''Article is defined by its id then its title'''
        return u"[{0}] {1}".format(self.id, self.title)
    
    def save(self, *args, **kwargs):
        '''Override of the save function to generate a slug'''
        if self.pk is None:
            self.generate()
        super(Article, self).save(*args, **kwargs)
    
    def generate(self):
        '''generate a slug from the title'''
        slug = '-'.join(self.title.lower().split())
        self.slug = slug

    def get_absolute_url(self):
        '''because reverse_lazy doesn't work, returns the article's page'''
        return reverse("blog_read", kwargs={'id': self.id, 'slug': self.slug})
    
    
class Category(models.Model):
    '''This class is a simple foreign key for the articles defining their category'''
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        '''Category is defined by its name'''
        return self.name
    
class Comment(models.Model):
    '''A generic comment class (copy/pastable anywhere)'''
    author = models.CharField(max_length=42, default='anonymous')
    content = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    def __unicode__(self):
        return u"Comment by {0} on {1}".format(self.author, self.content_object)
    
    def get_absolute_url(self):
        '''Again, because reverse_lazy doesn't work, returns the article's page'''
        return reverse("blog_read", kwargs={'id': self.object_id, 'slug': self.content_object.slug})
        