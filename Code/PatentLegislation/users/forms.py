from django import forms
from django.core import validators
from django.http import  HttpRequest
from users.models import UserModel, UploadModel


def name_check(value):
    if value.isalpha()!=True:
        raise forms.ValidationError("only string are allowed")



class userForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(), required=True, max_length=100, validators=[name_check])
    lastname = forms.CharField(widget=forms.TextInput(), required=True, max_length=100, validators=[name_check])
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    qualification = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    city = forms.CharField(widget=forms.TextInput(), required=True, max_length=100, validators=[name_check])
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    def __str__(self):
        return self.email

    class Meta:
        model = UserModel
        fields=['firstname','lastname','passwd','email','mobileno','qualification','city','status']

# iterable
key_technology =(
    ("Computer Technology", "Computer Technology"),
    ("Management Control", "Management Control"),
    ("Digital Communication Measurement", "Digital Communication Measurement"),
    ("Telecommunications", "Telecommunications"),
    ("Medical Technology", "Medical Technology"),
    ("Games", "Games"),
    ("Handling Furniture", "Handling Furniture"),
    ("Electrical Machinery", "Electrical Machinery"),
    ("Transport", "Transport"),
    ("Audio-visual technology", "Audio-visual technology"),
    ("Other Special Machines", "Other Special Machines"),
    ("Civil Engineering", "Civil Engineering"),
    ("Other Consumer Goods", "Other Consumer Goods"),
    ("Thermal processes and apparatus", "Thermal processes and apparatus"),
    ("Machine Tools", "Machine Tools"),
    ("Analysis of Biological Materials", "Analysis of Biological Materials"),
    ("Chemical Engineering", "Chemical Engineering"),
    ("Engines", "Engines"),
    ("Pumps", "Pumps"),
    ("Turbines", "Turbines"),
    ("Optics", "Optics"),
    ("Environmental Technology", "Environmental Technology"),
    ("Mechanical Elements", "Mechanical Elements"),
    ("Materials", "Materials"),
    ("Metallurgy", "Metallurgy"),
    ("Biotechnology", "Biotechnology"),
    ("Basic Communication Processes", "Basic Communication Processes"),
    ("Food Chemistry", "Food Chemistry"),
    ("Semiconductors", "Semiconductors"),
    ("Textile and Paper Machines", "Textile and Paper Machines"),
    ("Macro-Molecular Chemistry", "Macro-Molecular Chemistry"),
    ("Polymers", "Polymers"),
    ("Basic Materials Chemistry", "Basic Materials Chemistry"),
    ("Pharmaceuticals", "Pharmaceuticals"),
    ("Surface Technology", "Surface Technology"),
    ("Coating","Coating"),
    ("Organic fine Chemistry","Organic fine Chemistry"),
    ("Micro-structure and nano-technology","Micro-structure and nano-technology"),
)

class UploadForm(forms.ModelForm):
    #email = forms.CharField(max_length=100, initial=request.session['email'])
    description = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    category = forms.ChoiceField(choices=key_technology)

    class Meta:
        model = UploadModel
        fields = ('email','category','title','description','file','status','adminstatus')