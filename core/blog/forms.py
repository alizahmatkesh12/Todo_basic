from django import forms
from .models import Post


class PostCreateForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(label='Body', widget=forms.Textarea)
    date_posted = forms.DateTimeField(label='Created date', widget=forms.DateInput)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'date_posted']    #__all__
