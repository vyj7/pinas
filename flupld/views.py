import os,mimetypes
import shutil
import zipfile
from io import StringIO,BytesIO
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.shortcuts import render, HttpResponseRedirect
from .forms import FileForm,FolderForm
from .models import FileData,FolderData,newpath
from browser.models import SignUp
from browser.views import findos
from django.conf import settings
def getFolderSize(folder_path):
    total_size = os.path.getsize(folder_path)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path,item)
        if os.path.isfile(item_path):
            total_size += os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            getFolderSize(item_path)
    return total_size
    
def Upload(request,user_id,dir_id):
    try:
        reqobj=SignUp.objects.get(uid=int(user_id))
    except SignUp.DoesNotExist:
        return HttpResponseRedirect('/log/')
    findos.redefine()
    if reqobj.auth==True:
        max_size=2**30
        size=(getFolderSize(reqobj.data['0'][0])/max_size)*100
        filenames=[]
        foldernames=[]
        tempdata={}
        main_path = reqobj.data[dir_id][0]
        tpath=main_path.split('\\')
        s='\\\\'
        xpath=s.join(tpath)
        for j in reqobj.data:
            tempdata[str(j)]=[str(reqobj.data[j][0]),str(reqobj.data[j][1])]
        for root,dirc,files in os.walk(main_path):
            filenames=files
            foldernames=dirc
            break
        context = {
                'size':size,
                'value':pop.value,
                'data':tempdata,    
                'user_id':user_id,
                'owndir_id':dir_id,
                'filenames':filenames,
                'foldernames':foldernames,
                'main_path':xpath,
                'osname':findos.osname
               }
        pop.changevalue(0)
        return render(request,"upload.html",context)
        

class prompt:
    def __init__(self,startvalue):
        self.value=startvalue
    def changevalue(self,newvalue):
        self.value=newvalue
pop=prompt(0)

def createfolder(request,user_id,updir_id,folder_name):
    try:
        reqobj=SignUp.objects.get(uid=int(user_id))
        folder_path = os.path.join(reqobj.data[updir_id][0],str(folder_name))
        os.makedirs(folder_path)
        reqobj.maxno+=1
        reqobj.data[reqobj.maxno]=[folder_path,str(folder_name)]
        reqobj.save()
    except FileExistsError:
        print("ERROR raised")
        pop.changevalue(1)
        
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

def renamefolder(request,user_id,updir_id,folder_name,new_name):
    reqobj=SignUp.objects.get(uid=int(user_id))
    folder_path = os.path.join(reqobj.data[updir_id][0],str(folder_name))
    new_path = os.path.join(reqobj.data[updir_id][0],str(new_name))
    try:
        os.rename(folder_path,new_path)
        for j in reqobj.data:
            if reqobj.data[j][0]==folder_path:
                break
        reqobj.data[j]=[new_path,str(new_name)]
        reqobj.save()
        position=len(reqobj.data[j][0].split(findos.splitstr))
        for j in reqobj.data:
            if folder_path in reqobj.data[j][0]:
                somepath=reqobj.data[j][0].split(findos.splitstr)
                somepath[position-1]=new_name
                reqobj.data[j][0]=findos.joinstr.join(somepath)
            reqobj.save()
    except FileExistsError as e:
        print("ERROR raised:",e)
        pop.changevalue(1)
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)
   
def filedelete(request,user_id,updir_id,file_name):
    reqobj=SignUp.objects.get(uid=int(user_id))
    file_path = os.path.join(reqobj.data[updir_id][0],file_name)
    os.remove(file_path)
    for obj in FileData.objects.all():
        file_t = str(obj)
        if file_t==file_name:
            obj.delete()
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

def folderdelete(request,user_id,updir_id,dir_id):
    deletelist=[]
    reqobj=SignUp.objects.get(uid=int(user_id))
    folder_path = reqobj.data[dir_id][0]
    shutil.rmtree(folder_path)
    for obj in FolderData.objects.all():
        folder_t = str(obj)
        if folder_t==reqobj.data[dir_id][1]:
            obj.delete()
    for j in reqobj.data:
        if folder_path in reqobj.data[j][0]:
            deletelist.append(j)
    for i in deletelist:
        del reqobj.data[i]
    reqobj.save()
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

def deletemul(request,user_id,updir_id,item_list):
    reqobj=SignUp.objects.get(uid=int(user_id))
    t=item_list.split('|')
    for i in t:
        try:
            item_path = os.path.join(reqobj.data[updir_id][0],i)
            if os.path.isdir(item_path):
                deletelist=[]
                shutil.rmtree(item_path)
                for obj in FolderData.objects.all():
                    folder_t = str(obj)
                    if folder_t==os.path.basename(item_path):
                        obj.delete()
                for j in reqobj.data:
                    if item_path in reqobj.data[j][0]:
                        deletelist.append(j)
                for i in deletelist:
                    del reqobj.data[i]
                reqobj.save()
            else:
                os.remove(item_path)
                for obj in FileData.objects.all():
                    file_t = str(obj)
                    if file_t==os.path.basename(item_path):
                        obj.delete()
        except FileNotFoundError:
            print('ERROR Raised')
            continue;
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

class rempath:
    path=[]
    x=0
    def pathchanged(self,new_path):
        self.path.append(new_path)
pathobj=rempath()
        
def copyfolder(request,user_id,updir_id,item_list):
    reqobj=SignUp.objects.get(uid=int(user_id))
    t=item_list.split('|')
    pathobj.x=1
    pathobj.path=[]
    for i in t:
        folder_path = os.path.join(reqobj.data[updir_id][0],i)
        pathobj.pathchanged(folder_path)
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

def cutfolder(request,user_id,updir_id,item_list):
    reqobj=SignUp.objects.get(uid=int(user_id))
    t=item_list.split('|')
    pathobj.x=2
    pathobj.path=[]
    for i in t:
        folder_path = os.path.join(reqobj.data[updir_id][0],i)
        pathobj.pathchanged(folder_path)
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

def pastefolder(request,user_id,updir_id):
    reqobj=SignUp.objects.get(uid=int(user_id))
    folder_path = reqobj.data[updir_id][0]
    if pathobj.x==1:
        for i in pathobj.path:
            try:
                updatelist=[]
                if os.path.isdir(i):
                    position=len(i.split(findos.splitstr))
                    for j in reqobj.data:
                        if i in reqobj.data[j][0]:
                            temp=reqobj.data[j][0].split(findos.splitstr)
                            name=temp[-1]
                            final= os.path.join(folder_path,findos.joinstr.join(temp[position-1:]))
                            updatelist.append([final,name])
                    final= os.path.join(folder_path,os.path.basename(i))
                    shutil.copytree(i,final)
                    for each in updatelist:
                        reqobj.maxno+=1
                        reqobj.data[reqobj.maxno]=each
                    reqobj.save()
                else:
                    final= os.path.join(folder_path,os.path.basename(i))
                    shutil.copy(i,final)
            except (FileExistsError,FileNotFoundError):
                print("Copy ERROR Raised")
                continue
    elif pathobj.x==2:
        for i in pathobj.path:
            try:
                deletelist=[]
                updatelist=[]
                if os.path.isdir(i):
                    position=len(i.split(findos.splitstr))
                    for j in reqobj.data:
                        if i in reqobj.data[j][0]:
                            deletelist.append(j)
                            temp=reqobj.data[j][0].split(findos.splitstr)
                            name=temp[-1]
                            final= os.path.join(folder_path,findos.joinstr.join(temp[position-1:]))
                            updatelist.append([final,name])
                    shutil.move(i,folder_path)
                    for each1 in deletelist:
                        del reqobj.data[each1]
                    for each2 in updatelist:
                        reqobj.maxno+=1
                        reqobj.data[reqobj.maxno]=each2
                    reqobj.save()
                else:
                    shutil.move(i,folder_path)
            except (shutil.Error,FileNotFoundError):
                print("Cut ERROR Raised")
                continue
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

def uploadfile(request,user_id,updir_id):
    reqobj=SignUp.objects.get(uid=int(user_id))
    main_path=reqobj.data[updir_id][0]
    listit=request.FILES.getlist('files')
    newpath.func(main_path)
    for afile in listit:
        temp=FileData()
        temp.file=afile
        temp.save()
    return HttpResponseRedirect('/flupld/'+user_id+'/'+updir_id)

def downloadfile(request,user_id,updir_id,file_name):
    reqobj=SignUp.objects.get(uid=int(user_id))
    main_path=reqobj.data[updir_id][0]
    filepath=os.path.join(main_path,file_name)
    file=open(filepath,'rb')
    response = HttpResponse(FileWrapper(file),content_type=mimetypes.guess_type(filepath)[0])
    response['Content-Disposition']='attachment; filename=%s'%os.path.basename(filepath)
    response['Content-Length']=os.path.getsize(filepath)
    file.close()
    return response

def createzipfolder(zipf,folderpath):
    print("Inisde Zip folder")
    x = os.listdir(folderpath)
    print(x)
    if len(x)!=0:
        print("Inside if")
        for item in os.listdir(folderpath):
            print(item)
            item_path = os.path.join(folderpath,item)
            if os.path.isfile(item_path):
                zipf.write(item_path,item,zipfile.ZIP_DEFLATED)
                print("did zipping")
            elif os.path.isdir(item_path):
                print("Inside sub dirs")
                createzipfolder(zipf,item_path)
    else:
        print("Else")
        return
def downloadfolder(request,user_id,updir_id,folder_name):
    reqobj=SignUp.objects.get(uid=int(user_id))
    main_path=reqobj.data[updir_id][0]
    folderpath=os.path.join(main_path,folder_name)
    zipfolder = BytesIO()
    print("strinio")
    zipf = zipfile.ZipFile(zipfolder,"w")
    print("zipf")
    createzipfolder(zipf,folderpath)
    print("zipfcomplter")
    zipf.close()
    response = HttpResponse(zipfolder.getvalue(),content_type="application/x-zip-compressed")
    response['Content-Disposition']='attachment; filename=%s'%os.path.basename(folderpath)+".zip"
    response['Content-Length']=os.path.getsize(folderpath)
    return response

def backpage(request,user_id,dir_id):
    reqobj=SignUp.objects.get(uid=int(user_id))
    main_path=reqobj.data[dir_id][0]
    dir_path=os.path.dirname(main_path)
    togo=''
    if dir_id=='0':
        togo='0'
    else:
        for j in reqobj.data:
            if reqobj.data[j][0]==dir_path:
                togo=j
                break;
    return HttpResponseRedirect('/flupld/'+user_id+'/'+togo)
