from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    word = forms.CharField(max_length=2000,
                           widget=forms.Textarea(attrs={'rows': '30', 'cols': '150'}))

    class Meta:
        model = Post
        fields = ('word',)
