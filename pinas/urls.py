"""pinas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$','browser.views.log',name='log'),
    url(r'^register/','browser.views.register',name='register'),
    url(r'^log/','browser.views.log',name='log'),
    url(r'^logout/(?P<user_id>.+)','browser.views.logout',name='logout'),
    url(r'^flupld/(?P<user_id>.+)/(?P<dir_id>.+)','flupld.views.Upload',name='Upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^backpage/(?P<user_id>.+)/(?P<dir_id>.+)', 'flupld.views.backpage'),
    url(r'^fileupload/(?P<user_id>.+)/(?P<updir_id>.+)','flupld.views.uploadfile',name='uploadfile'),
    url(r'^filedownload/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<file_name>.+)','flupld.views.downloadfile'),
    url(r'^folderdownload/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<folder_name>.+)','flupld.views.downloadfolder'),
    url(r'^filedelete/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<file_name>.+)', 'flupld.views.filedelete'),
    url(r'^foldercreate/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<folder_name>.+)', 'flupld.views.createfolder'),
    url(r'^foldercopy/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<item_list>.+)', 'flupld.views.copyfolder'),
    url(r'^foldercut/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<item_list>.+)', 'flupld.views.cutfolder'),
    url(r'^muldelete/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<item_list>.+)', 'flupld.views.deletemul'),
    url(r'^folderpaste/(?P<user_id>.+)/(?P<updir_id>.+)', 'flupld.views.pastefolder'),
    url(r'^folderrename/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<folder_name>.+)/(?P<new_name>.+)', 'flupld.views.renamefolder'),
    url(r'^folderdelete/(?P<user_id>.+)/(?P<updir_id>.+)/(?P<dir_id>.+)', 'flupld.views.folderdelete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    
