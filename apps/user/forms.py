# from django import forms
# from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

# from user.models import User
# from django.forms import ModelForm


# class LoginForm(forms.Form):
#     username = forms.CharField(
#         label="Логин",
#         widget= forms.TextInput(
#             attrs = {"class":"form-control"}
#         )
#     )
#     password = forms.CharField(
#         label = "Пароль",
#         widget = forms.PasswordInput(
#             attrs = {"class":"form-control"}
#         )
#     )


# class UserRegisterForm(UserCreationForm):
#     password1 = forms.CharField(
#         label = "Пароль",
#         widget = forms.PasswordInput(
#             attrs = {"class":"form-control"}
#         )
#     )
#     password2 = forms.CharField(
#         label = "Повторите пароль:",
#         widget = forms.PasswordInput(
#             attrs = {"class":"form-control"}
#         )   
#     )


#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "phone",
#             "birthday"
#         ]
#         form_control = {"class":"form-control"}
#         widgets = {
#             "username":forms.TextInput(attrs=form_control),
#             "first_name":forms.TextInput(attrs=form_control),
#             "last_name":forms.TextInput(attrs=form_control),
#             "email": forms.EmailInput(attrs=form_control),
#             "phone": forms.TextInput(attrs=form_control),
#             "birthday": forms.DateInput(attrs=form_control),
#         }

# class UserUpdateForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = (
#             "avatar",
#             "email",
#             "first_name",
#             "last_name",
#             "phone",
#             "birthday"
#         )
#         widgets = {
#             "avatar": forms.FileInput(
#                 attrs={"class":"form-control"}
#             ),
#             "email": forms.EmailInput(
#                 attrs={"class":"form-control"}
#             ),
#             "first_name": forms.TextInput(
#                 attrs={"class":"form-control"}
#             ),
#             "last_name": forms.TextInput(
#                 attrs={"class":"form-control"}
#             ),
#             "phone": forms.TextInput(
#                 attrs={"class":"form-control"}
#             ),
#             "birthday": forms.DateInput(
#                 attrs={"class":"form-control"}
#             )
#         }


# class UserPasswordChangeForm(SetPasswordForm):
#     class Meta:
#         model = User
#         fields = ["new_password1", "new_password2"]