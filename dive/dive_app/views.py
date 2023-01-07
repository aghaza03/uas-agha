from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

def Login(request):
    if request.user.is_authenticated:
        return redirect ("/dive/")
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            user=authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('/dive/')
            
        return render(request, "login.html")

def Regis(request):
    if request.user.is_authenticated:
        return redirect ("/dive/")
    else:
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('/login/')

        return render(request, "regis.html")

def Logout(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='login')
def dive(request):
      selam = Dive.objects.all()
      lokasi_json = serializers.serialize('json', selam)
      konteks = {
          "Judul"   : "Sebaran Dive & Snorkle",
          'selam'  : selam,
          'lokasi_json' : lokasi_json,
      }
      return render(request, "dive.html", konteks)

@login_required(login_url='login')
def tambah_1(request):
      if request.POST:
          form = FormDive(request.POST, request.FILES)
          if form.is_valid():
              form.save()
              form = FormDive()
              selam = Dive.objects.all()
              konteks = {
                  "Judul"   : "Tambah Data",
                 'Title' : "Input Data Baru",
                 'selam' : selam,
                 'form'    : form,
                 'pesan'   : "Data berhasil ditambahkan"
              }
              return render(request, "tambah_1.html", konteks)
      else:
          form  = FormDive()
          selam = Dive.objects.all()
          konteks = {
             "Judul"   : "Tambah Data",
             'Title'   : "Input Data Baru",
             'selam' : selam,
             'form'    : form,
          }
          return render(request, "tambah_1.html", konteks)

@login_required(login_url='login')
def ubah_1(request, id):
      selam = Dive.objects.get(pk=id)
      if request.POST:
          form = FormDive(request.POST, request.FILES ,instance=selam)
          if form.is_valid():
              form.save()
              konteks = {
                  "Judul"   : "Ubah Data",
                  'Title' : "Ubah Data",
                  'selam' : selam,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "ubah_1.html", konteks)
      else:
          form = FormDive(instance=selam)
          konteks = {
          "Judul"   : "Ubah Data",
          'Title' : "Ubah Data",
          'selam' : selam,
          'form'  : form,
           }
      return render(request, "ubah_1.html", konteks)

@login_required(login_url='login')
def hapus_1(request, id):
    selam = Dive.objects.get(pk=id)
    selam.delete()
    
    return redirect("/dive/")

@login_required(login_url='login')
def peralatan(request):
      macam = Peralatan.objects.all()
      konteks = {
          "Judul" : "Peralatan Dive & Snorkle",
          'macam' : macam,
      }
      return render(request, "peralatan.html", konteks)

@login_required(login_url='login')
def tambah_2(request):
      if request.POST:
          form = FormPeralatan(request.POST, request.FILES)
          if form.is_valid():
              form.save()
              form = FormPeralatan()
              macam = Peralatan.objects.all()
              konteks = {
                  "Judul" : "Tambah Data",
                 'Title' : "Input Data Baru",
                 'macam' : macam,
                 'form'  : form,
                 'pesan' : "Data berhasil diubah"
              }
              return render(request, "tambah_2.html", konteks)
      else:
          form  = FormPeralatan()
          macam = Peralatan.objects.all()
          konteks = {
             "Judul" : "Tambah Data",
             'Title' : "Input Data Baru",
             'macam' : macam,
             'form'  : form,
          }
          return render(request, "tambah_2.html", konteks)

@login_required(login_url='login')
def ubah_2(request, id):
      macam = Peralatan.objects.get(pk=id)
      if request.POST:
          form = FormPeralatan(request.POST, request.FILES, instance=macam)
          if form.is_valid():
              form.save()
              konteks = {
                  "Judul"   : "Ubah Data",
                  'Title' : "Ubah Data",
                  'macam' : macam,
                  'form'  : form,
                  'pesan' : "Data berhasil diubah"
              }
              return render(request, "ubah_2.html", konteks)
      else:
          form = FormPeralatan(instance=macam)
          konteks = {
          "Judul"   : "Ubah Data",
          'Title' : "Ubah Data",
          'macam' : macam,
          'form'  : form,
           }
      return render(request, "ubah_2.html", konteks)

@login_required(login_url='login')
def hapus_2(request, id):
    macam = Peralatan.objects.get(pk=id)
    macam.delete()
    
    return redirect("/peralatan/")