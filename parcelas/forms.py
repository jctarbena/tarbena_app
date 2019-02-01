# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from dal import autocomplete
from django import forms
from django.contrib.auth.models import User

from .models import Parcela, Propietario

import urllib.request
import re
import ssl

def cleanhtml(raw_html):
    """
    Function to remove tags from a string

    """
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

class ParcelaForm(forms.ModelForm):
    propietario = forms.ModelChoiceField(
        queryset=Propietario.objects.all(),
        widget=autocomplete.ModelSelect2(url='parcelas:propietario-autocomplete')
    )

    class Meta:
        model = Parcela
        fields = '__all__'

    def save(self, commit=True):
        instance = super(ParcelaForm, self).save(commit=False)

        if not instance.kml:
            context = ssl._create_unverified_context()
            kml_url='https://ovc.catastro.meh.es/Cartografia/WMS/BuscarParcelaGoogle3D.aspx?refcat=03' + instance.poblacion.codigo + 'A'+ "{:03n}".format(int(instance.poligono)) + "{:05n}".format(int(instance.numero_parcela)) + '0000BP&del=3&mun=' + instance.poblacion.codigo + '&tipo=3d'
            fp = urllib.request.urlopen(kml_url,context=context)
            mybytes = fp.read()
            mykml = mybytes.decode('unicode_escape').encode('utf-8')
            instance.kml = mykml

            if commit:
                instance.save()
                
        if not instance.localizacion:
            my_url = "https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCConCiud.aspx?del=3&mun=" + instance.poblacion.codigo + "&UrbRus=&RefC=03" + instance.poblacion.codigo + "A" + "{:03n}".format(int(instance.poligono)) + "{:05n}".format(int(instance.numero_parcela)) + "0000BL&Apenom=&esBice=&RCBice1=&RCBice2=&DenoBice=&latitud=&longitud=&gradoslat=&minlat=&seglat=&gradoslon=&minlon=&seglon=&x=&y=&huso=&tipoCoordenadas="
            uClient = urllib.request.urlopen(my_url)
            page_html = uClient.read()
            uClient.close()
            instance.url = my_url

            page_soup = BeautifulSoup(page_html, "html.parser")
            labels_page = page_soup.find_all("label")
            for index, item in enumerate(labels_page, start=0):
                if index == 1:
                    remove_br = re.sub('<br/>', ' ', str(item))
                    instance.localizacion = cleanhtml(remove_br)
                    instance.save()
            if commit:
                instance.save()
        return instance