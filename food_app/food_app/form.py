
from django import forms
from .models import *
 
 
class receipe_Form(forms.ModelForm):
 
    class Meta:
        model = Reciepes
        fields = ['name', 'image','steps','description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "db-name",
                'placeholder': 'Use more generalised titles'
                }),
            'description': forms.TextInput(attrs={
                'class': "db-description",
                'placeholder': '  receipe description'
                }),
            'steps': forms.Textarea(attrs={
                'class': "db-steps", 
                'rows':50,
                'placeholder': ' keep it short and simple!! '
                }),
            'image':forms.ClearableFileInput(attrs={
                'class':'db-image'
            })
        }


class Main_receipe_Form(forms.ModelForm):
 
    class Meta:
        model = Reciepes
        fields = ['name', 'image','steps','user_id','description']

