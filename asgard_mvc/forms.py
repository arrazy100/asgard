from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, ButtonHolder, MultiField, Row, Column
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import UserProfileModel

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), required=True)
    email = forms.CharField(widget=forms.EmailInput(), required=True)
    first_name = forms.CharField(widget=forms.TextInput(), required=True)
    last_name = forms.CharField(widget=forms.TextInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_repeat = forms.CharField(widget=forms.PasswordInput(), required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = (
            Div(
                Row(
                    Column(
                        Field(
                            'first_name',
                            css_class='form-control form-control-user',
                            css_id='exampleFirstName',
                            placeholder='First Name'
                        )
                    ),
                    Column(
                        Field(
                            'last_name',
                            css_class='form-control form-control-user',
                            css_id='exampleLastName',
                            placeholder='Last Name'
                        )
                    ),
                    Column(
                        Field(
                            'username',
                            css_class='form-control form-control-user',
                            css_id='exampleInputUsername',
                            placeholder='Username'
                        )
                    ),
                    Column(
                        Field(
                            'email',
                            css_class='form-control form-control-user',
                            css_id='exampleInputEmail',
                            placeholder='Email Address'
                        )
                    ),
                    Column(
                        Field(
                            'password',
                            css_class='form-control form-control-user',
                            css_id='exampleInputPassword',
                            placeholder='Password'
                        )
                    ),
                    Column(
                        Field(
                            'password_repeat',
                            css_class='form-control form-control-user',
                            css_id='exampleRepeatPassword',
                            placeholder='Repeat Password'
                        )
                    ),
                    css_class = 'form-group'
                ),
                Submit(
                    'submit',
                    'Register',
                    css_class='btn btn-primary btn-user btn-block'
                )
            )
        )

    def clean_username(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username sudah terdaftar")
        else:
            pass

    def clean_email(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email sudah terdaftar")
        else:
            pass

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if (password != password_repeat):
            print(password_repeat)
            raise ValidationError("Password tidak sama")
        else:
            pass

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'},
    ), required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'},
    ), required=True)

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = (
            Div(
                Field(
                    'username',
                    style='background-color: #232322;border: #232322;',
                    css_class='form-control form-control-user',
                    css_id='ExampleInputEmail',
                    placeholder="Enter Username"
                ),
                Field(
                    'password',
                    style='background-color: #232322;border: #232322;',
                    css_class='form-control form-control-user',
                    css_id='ExampleInputPassword',
                    placeholder="Enter Password"
                ),
                Submit(
                    'submit',
                    'Login',
                    style='background-color: #FF6166;border: #FF6166;',
                    css_class='btn btn-primary btn-user btn-block'
                )
            )
        )

class UserProfileForm(forms.ModelForm):
    image_profile = forms.ImageField(label='')
    class Meta:
        model = UserProfileModel
        fields = ('username', 'image_profile')
        