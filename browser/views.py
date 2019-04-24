import os,random,platform
from django.conf import settings
from django.shortcuts import render,HttpResponseRedirect
from .forms import SecondForm,FirstForm
from .models import SignUp,LogIn,newuid

class identifyOs:
    def __init__(self,newosname,newsplitstr,newjoinstr):
        self.osname=newosname
        self.splitstr=newsplitstr
        self.joinstr=newjoinstr
    def redefine(self):
        if platform.system()=="Windows":
            self.splitstr='\\'
            self.joinstr='\\'
            self.osname='Windows'
        elif platform.system()=="Linux":
            self.splitstr='/'
            self.joinstr='/'
            self.osname='Linux'
findos=identifyOs('','','')

def log(request):
    findos.redefine()
    temp = SecondForm(request.POST or None)
    text = "Log In"
    message="RETRY(Invalid Email Id or password)"
    context = {"title":text,
               "form":temp,
               "Message":message}
    if temp.is_valid() and request.method=="POST":
        it = temp.save(commit=False)
        reqobj=SignUp.objects.get(email=it.email)
        reqobj.auth=True
        path='/flupld/' + str(reqobj.uid) + '/0'
        reqobj.save(update_fields=['auth'])
        temp.save()
        return HttpResponseRedirect(path)        
    return render(request,"log.html",context)

def register(request):
    temp = FirstForm(request.POST or None)
    text = "Sign Up"
    context = {"title":text,
               "form":temp,}
    if temp.is_valid() and request.method=="POST":
        it = temp.save(commit=False)
        newuid.uidchange()
        it.uid=newuid.t
        temp.save()
        reqobj=SignUp.objects.get(uid=newuid.t)
        path=os.path.join(settings.MEDIA_ROOT,str(reqobj.id))
        os.makedirs(path)
        reqobj.data={'0':[path,str(reqobj.id)]}
        reqobj.save()
        return HttpResponseRedirect('/log/')
            
    else:
        return render(request,"reg.html",context)


def logout(request,user_id):
    reqobj=SignUp.objects.get(uid=int(user_id))
    reqobj.auth=False
    x=2**30
    y=2**40
    reqobj.uid=random.randint(x,y)
    reqobj.save(update_fields=['auth','uid'])
    return HttpResponseRedirect('/log/')
