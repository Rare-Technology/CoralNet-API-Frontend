from django import forms

class MainForm(forms.Form):
    global_id = forms.IntegerField()
    email = forms.EmailField()
