from django import forms
from .models import SignUp,LogIn

class FirstForm(forms.ModelForm):

        class Meta:
            model = SignUp
            fields =  ["full_name","email","password"]

        def clean_email(self):
                email=self.cleaned_data.get('email')
                if not "com" in email:
                        raise forms.ValidationError("Enter correct email-id")
                return email

class SecondForm(forms.ModelForm):
        class Meta:
            model = LogIn
            fields =  ["email","password"]

        def clean_email(self):
                flag=0;
                email=self.cleaned_data.get('email')
                for obj in SignUp.objects.all():
                        if obj.email==email :
                                flag=1
                if flag==0:       
                        raise forms.ValidationError("Invalid Email-Id")
                return email

        def clean_password(self):
                flag=0;
                password=self.cleaned_data.get('password')
                for obj in SignUp.objects.all():
                        if obj.password==password :
                                flag=1;
                if flag==0:
                        raise forms.ValidationError("Invalid Password")
                return password



            

            
