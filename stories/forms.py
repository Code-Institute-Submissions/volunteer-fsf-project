from django import forms
from .models import StoryPost

class StoryPostForm(forms.ModelForm):
    class Meta:
        model = StoryPost
        fields = ('title', 'content', 'image', 'published_date', 'camp_id')