import os
from django.conf import settings
from django.db import models

class passpath:
        def func(self,main_path):
                self.mainpath = main_path
                
newpath=passpath()

def get_path(instance,filename):
        return os.path.join(settings.MEDIA_ROOT,newpath.mainpath,filename)

class FileData (models.Model):
        #title = models.CharField(max_length=50,blank=True)
        file = models.FileField(upload_to=get_path)
        timestamp = models.DateTimeField(auto_now_add=True ,auto_now=False )

        def __str__(self):
                return str(self.file).split("/")[-1]
        
class FolderData (models.Model):
        foldername = models.CharField(max_length=50,blank=True)
        timestamp = models.DateTimeField(auto_now_add=True ,auto_now=False )

        def __str__(self):
                return self.foldername
