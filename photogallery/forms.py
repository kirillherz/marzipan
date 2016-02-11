from django import forms
from django.forms import Textarea, TextInput
from .models import ReviewModel, CakeModel, FeedbackModel
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
import re

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(label = 'Оценка', choices = ((1,1),(2,2),(3,3),(4,4),(5,5)))
    cake_id = forms.IntegerField(widget = forms.HiddenInput)
    
    class Meta:
        model = ReviewModel
        fields = '__all__'
        exclude = ['cake']
        widgets = {
            'review': Textarea(attrs = {'cols':80, 'rows': 20})
        }

    def set_cake_id(self, cake_id):
        self.fields['cake_id'].initial = cake_id
        
    def save(self, commit = True):
        instance = super(ReviewForm, self).save(commit = False)
        cake = CakeModel.objects.get(pk = self.cleaned_data['cake_id'])
        instance.cake = cake
        if commit:
            instance.save()
        
class FeedbackForm(forms.ModelForm):
    def length_validator(value):
        if len(str(value)) != 10:
            raise ValidationError('invalid', code = 'invalid')
            
    phone_number = forms.IntegerField(widget = TextInput(attrs={'data-validator': 'int', 'data-validator-id' : 'phone_number'}),validators = [length_validator],error_messages = {'invalid' : 'Неправильный номер телефона'})
    class Meta:
        model = FeedbackModel
        fields = '__all__'
        widgets = {
        'name' : TextInput(attrs={'data-validator': 'required', 'data-validator-id' : 'name'}),
        'message' : Textarea(attrs={'data-validator': 'required', 'data-validator-id' : 'message','cols':80, 'rows': 20}),
        'e_mail' : TextInput(attrs={'data-validator': 'e_mail', 'data-validator-id' : 'e_mail'}),
        }