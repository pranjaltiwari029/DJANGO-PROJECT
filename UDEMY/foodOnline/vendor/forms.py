from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):
    # password=forms.CharField(widget=forms.PasswordInput())
    # confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Vendor
        fields=['vendor_name','vendor_license']
        
        
        
    # def clean(self):
    #     cleaned_data=super(UserForm,self).clean()
    #     password=cleaned_data.get('password')
    #     confirm_password=cleaned_data.get('confirm_password')
        
    #     if password !=confirm_password:
    #         raise form.ValidationError("password does not match !")