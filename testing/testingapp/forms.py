from django import forms

class studentform(forms.Form):
    id = forms.IntegerField(label="ID")
    name=forms.CharField(label="NAME",max_length=100)
    
class getdetails(forms.Form):
    id = forms.IntegerField(label="ID")
    
class updatedetails(forms.Form):
    id=forms.IntegerField(label="ID")
    name = forms.CharField(label="Name to Update",max_length=100)
    
class deleteform(forms.Form):
    id = forms.IntegerField(label="ID")
    