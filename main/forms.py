from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='Enter Search String', max_length=100)