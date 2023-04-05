from django import forms

class InputText(forms.Form):
    Text = forms.CharField(widget=forms.Textarea(attrs={"rows":"10","cols":"100"}))    
