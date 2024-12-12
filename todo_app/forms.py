from django import forms
from .models import Todo

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)

class AddTodoForm(forms.ModelForm):
    class Meta:
        model  = Todo
        fields = ['title', 'completed']