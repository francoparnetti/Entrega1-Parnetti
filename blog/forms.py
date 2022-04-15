from django import forms


class CreateBlog(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=200)
    
class BlogSearch(forms.Form):
    title = forms.CharField(max_length=50)
