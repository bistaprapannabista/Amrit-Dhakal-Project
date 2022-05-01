from django import forms
from django.forms import ImageField, ModelForm
from django import forms
from product.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=50)
    date_of_birth = forms.DateField(widget = DateInput)
    image = forms.ImageField(required=False)