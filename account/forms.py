# from django.contrib.auth.models import User

# # 폼
# from django import forms

# class SignUpForm(forms.ModelForm):
#     # widget을 오버라이드하여 입력될때 *표시를 찍어준다
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['password', 'password2', 'email', 'date_of_birth', 'gender', 'address']

#         # TODO : 필드의 기본값 설정, Placeholder 설정법, css Class 설정법, Validator 설정법, help text 설정법
#         # TODO : 커스텀 필드 만드는 법

#     # clean_필드명
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

#         # 항상 해당 필드의 값을 리턴한다.
#         return cd['password2']