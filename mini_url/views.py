# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from mini_url.models import Mini
from mini_url.forms import MiniForm

def target(request, short_url):
    short_link = get_object_or_404(Mini, short_url = short_url)
    short_link.counter += 1
    short_link.save()
    return redirect(short_link.long_url)

class MiniList(ListView):
    model = Mini
    context_object_name = "links"
    template_name = "mini_url/home.html"
    
    def get_queryset(self):
        return Mini.objects.order_by('-counter')
    
class URLCreate(CreateView):
    model = Mini
    template_name = "mini_url/new_link.html"
    form_class = MiniForm
    
class URLUpdate(UpdateView):
    model = Mini
    template_name = "mini_url/new_link.html"
    form_class = MiniForm
    
    def get_object(self, queryset=None):
        short_url = self.kwargs.get('short_url', None)
        return get_object_or_404(Mini, short_url=short_url)
    
    