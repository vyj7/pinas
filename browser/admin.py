from django.contrib import admin

from .models import SignUp,LogIn
from .forms import FirstForm,SecondForm
class new(admin.ModelAdmin):
    list_display=["id","__str__","full_name","email","data","maxno","password","uid","auth"]
    form = FirstForm
class new2(admin.ModelAdmin):
    list_display=["email","password"]
    form = SecondForm

admin.site.register(SignUp,new)
admin.site.register(LogIn,new2)
