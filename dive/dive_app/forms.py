from django.forms import ModelForm
from django import forms
from .models import *

class FormDive(ModelForm):
    class Meta:
        model = Dive
        fields = '__all__'

        widgets = {
            'nama'    : forms.TextInput({'class':'form-control', 'placeholder':'Nama Tempat', 'required':'required'}),
            'grs_lintang' : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Lintang', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
            'grs_bujur'  : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Bujur', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
            'gambar'   : forms.FileInput({'class':'form-control', 'required':'required'}),
        }


class FormPeralatan(ModelForm):
    class Meta:
        model = Peralatan
        fields = '__all__'

        widgets = {
            'nama_Alat'  : forms.TextInput({'class':'form-control', 'placeholder':'Nama Alat', 'required':'required'}),
            'harga'      : forms.TextInput({'class':'form-control', 'placeholder':'Harga Alat', 'required':'required'}),
            'gambar'     : forms.FileInput({'class':'form-control', 'required':'required'}),
            'deskripsi'  : forms.Textarea({'class':'form-control', 'placeholder':'Deskripsi', 'required':'required'}),
        }