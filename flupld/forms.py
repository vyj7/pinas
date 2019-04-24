from django import forms
from .models import FileData,FolderData
class FileForm(forms.ModelForm):

    class Meta:
        model = FileData
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data['file']
        return file

class FolderForm(forms.ModelForm):

    class Meta:
        model = FolderData
        fields = ['foldername']
