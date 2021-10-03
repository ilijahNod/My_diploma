from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "user_name"]
        labels = {
            "text": "Your Comment"
        }


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'image', 'title', 'excerpt', 'content', 'tags'
        ]

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'style': 'display: none;', 'class': 'form-control', 'required': False, })
        }
