from django import forms
from .models import Blog,Events,About,Home,Wedding,Birthday,Haldi,Party


class homeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'
        
class aboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        
        
class weddingForm(forms.ModelForm):
    class Meta:
        model = Wedding
        fields = '__all__'
        
class birthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        
class haldiForm(forms.ModelForm):
    class Meta:
        model = Haldi
        fields = '__all__'
        
class partyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = '__all__'
        
        
class blogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
        
class eventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        