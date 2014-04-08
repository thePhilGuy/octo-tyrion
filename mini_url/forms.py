from django import forms
from models import Mini

class MiniForm(forms.ModelForm):
    class Meta:
        model = Mini
        exclude = ('short_url', 'counter')