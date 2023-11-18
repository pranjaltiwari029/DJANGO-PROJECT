from django import forms
from .models import Category,FoodItem
from accounts.validators import allow_only_images_validator

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category_name','description']
    

class FoodItemForm(forms.ModelForm):
    # image=forms.ImageField(widget=forms.FileInput(attrs={'class':'btn btn-info '}),validators=[allow_only_images_validator])
    # don't forget to mention image in fields sedtion while uncommenting the image 
    class Meta:
        model=FoodItem
        fields=['category','food_title','description','price','is_available']