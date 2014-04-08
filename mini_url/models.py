from django.db import models
from django.core.urlresolvers import reverse
import string, random

# Create your models here.
class Mini(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date Redirected")
    author = models.CharField(max_length=42, null=True, blank=True)
    counter = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u"[{0}] {1}".format(self.short_url, self.short_url)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate(10)
            
        super(Mini, self).save(*args, **kwargs)
        
    def generate(self, N):
        characters = string.letters + string.digits
        random_list = [random.choice(characters) for _ in xrange(N)]
        self.short_url =  ''.join(random_list)
        
    def get_absolute_url(self):
        return reverse("Mini_home")