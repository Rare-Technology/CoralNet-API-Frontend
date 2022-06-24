from django import forms

class MainForm(forms.Form):
    number_of_images = forms.IntegerField()
    global_ID = forms.IntegerField()
    email = forms.EmailField()
