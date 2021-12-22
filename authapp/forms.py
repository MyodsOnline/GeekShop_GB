from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ['username', 'password1', 'password2', 'email', 'age', 'avatar']

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        data = self.cleaned_data['age']
        if data == False:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class DateInput(forms.DateInput):
    input_type = 'date'


class ShopUserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-edit', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control-edit'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-edit'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control-edit'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-edit'}), required=False)
    birth_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control-edit'}), required=False)

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar', 'birth_date', 'promo_accept')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control-edit'
    #         field.help_text = ''
    #         if field_name == 'password':
    #             field.widget = forms.HiddenInput()
