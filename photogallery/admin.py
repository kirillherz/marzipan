from django.contrib import admin
from django.core.files import File
from .models import CakeModel, ReviewModel, FeedbackModel
from django import forms
from django.forms import Textarea
from io import BytesIO
from PIL import Image

class CakeForm(forms.ModelForm):
       
    class Meta:
        model = CakeModel
        fields = '__all__'
        widgets = {'description' : Textarea(attrs = {'cols':80,'rows':20})}

class CakeAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        image_field = form.cleaned_data.get('image')
        image = Image.open(image_field)
        w, h = image.size
        image = image.resize((int(w/ 2) ,int(h / 2.0)), Image.ANTIALIAS)
        image_file = BytesIO()
        image.save(image_file,'JPEG',quality=90)
        image_field.file = image_file
        obj.image = image_field
        obj.save()
        
    form = CakeForm

admin.site.register(CakeModel, CakeAdmin)
admin.site.register(ReviewModel)
admin.site.register(FeedbackModel)

