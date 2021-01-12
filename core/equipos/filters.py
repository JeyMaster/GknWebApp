from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
import django_filters
from . import models as md


class BasuraElectronicaFilter(django_filters.FilterSet):

    fecha_registro=django_filters.DateFilter(field_name='fecha_registro',
                                                widget=forms.DateInput(
                                                    attrs={
                                                        'type':'date',
                                                        'class':'form-control'
                                                    }
                                                )
                                            )
    fecha_recoleccion=django_filters.DateFilter(field_name='fecha_recoleccion',
                                                    widget=forms.DateInput(
                                                        attrs={
                                                        'type':'date',
                                                        'class':'form-control'
                                                        }
                                                    )
                                                )
    recolectado=django_filters.BooleanFilter(field_name='recolectado',
                                                widget=forms.CheckboxInput()
                                            )

    choices=[(user.get('id'),user.get('username')) for user in User.objects.all().values('id','username').filter(is_superuser=False)]
    
    responsable=django_filters.ChoiceFilter(choices=choices,widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model=md.Basura_Electronica
        fields=('recolectado','responsable','fecha_registro','fecha_recoleccion',)
       
    
class EquiposFilter(django_filters.FilterSet):
    
    class Meta:
        model=md.Equipo
        fields=('estado',)