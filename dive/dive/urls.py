"""dive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from dive_app.views import *
from dive_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.Login, name='login'),
    path("logout/", views.Logout, name='logout'),
    path("regis/", views.Regis, name='regis'),
    path("dive/", dive),
    path("tambah_1/", tambah_1),
    path("dive/ubah_1/<int:id>", ubah_1, name='update_1'),
    path("dive/hapus_1/<int:id>", hapus_1),
    path("peralatan/", peralatan),
    path("tambah_2/", tambah_2),
    path("peralatan/ubah_2/<int:id>", ubah_2, name='update_2'),
    path("peralatan/hapus_2/<int:id>", hapus_2),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)