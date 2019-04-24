from django.contrib import admin
from .models import FileData,FolderData
from .forms import FileForm,FolderForm

class new_admin(admin.ModelAdmin):
    class Meta:
        list_display=['file','timestamp']
        form = FileForm

class new_admin2(admin.ModelAdmin):
    class Meta:
        form = FolderForm
        list_display=['foldername','timestamp']

admin.site.register(FileData,new_admin)
admin.site.register(FolderData,new_admin2)        
