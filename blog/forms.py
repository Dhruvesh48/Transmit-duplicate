from django import forms
from .models import Community

class CreateCommunityForm(forms.ModelForm):
    class Meta:
        model = Community