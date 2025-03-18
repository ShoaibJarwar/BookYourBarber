# from django import forms

# class RegisterForm(forms.Form):
#     USER_TYPE_CHOICES = [
#         ('user', 'As a User'),
#         ('barber', 'As a Barber'),
#     ]

#     user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.Select(attrs={'id': 'userType'}))
#     username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'required': True}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email', 'required': True}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Password', 'required': True}))
