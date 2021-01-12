from django import forms
from . import models

class AditionalInfo(forms.ModelForm):
    fecha_termino_garantia=forms.DateInput(
        attrs={
            'class':'form_control'
        }
    )
    class Meta:
        model=models.Equipo_Para_Entregar_Detalles
        fields=('site','departamento', 'area','ubicacion_exacta','apps_especiales')

        widgets={
            'site':forms.Select(attrs={'class':'form-control'},choices=(
                    ('CEL','Celaya'),('VLG','Villagran'),('CED','CEDIS'),('QRO','Queretaro'),('FOR','Forja'))),
        
            'departamento':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'area':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'ubicacion_exacta':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'apps_especiales':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':'3'
                },
            ),
        }
        labels={
            'apps_especiales':'Apps especiales, separadas por una coma'
        }
class PreparacionForm(forms.ModelForm):
    
    ESTADOS=(
        ('Pr','En preparacion'),
        ('Ua','Usuario asignado'),
        ('Et','Entregado'),
        ('Ep','Equipo pool'),
        ('Bs','Basura electronica')        
    )

    service_tag = forms.CharField(max_length=12,required=False,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    nombre_equipo=forms.CharField(max_length=12,required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    usuario_final = forms.CharField( max_length=20, required=False,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    estado = forms.ChoiceField(choices=ESTADOS,required=False,widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    fecha_termino_garantia=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'type':'date'
            }
        ),
        required=False
    )

    class Meta:

        model=models.Equipo_Para_Entregar_Detalles
        fields=('nombre_equipo','preparado_por','service_tag','usuario_final','configurado_por','solicitud','estado',
                'fecha_termino_garantia')
        widgets={
            'preparado_por':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'configurado_por':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }

class BasuraElectronicaForm(forms.ModelForm):
    class Meta:
        model=models.Basura_Electronica
        fields='__all__'
        widgets={
            'fecha_registro':forms.TextInput(
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'fecha_recoleccion':forms.TextInput(
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'type':'number',
                    'class':'form-control'
                }
            ),
            'modelo':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'marca':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'no_serie':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'planta':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'responsable':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'recolectado':forms.CheckboxInput(
           
            )
            
        }

class AsignarPool(forms.ModelForm):
    ESTADOS=(
        ('Ep','Equipo pool'),
        ('Pa','Pool asignado'),
        )

    estado = forms.ChoiceField(choices=ESTADOS,required=False,initial='Pa')
    
    class Meta:
        model=models.Equipo_Pool_Entrega
        exclude=('nombre_equipo',)
        

        widgets={
            'fecha_entrega':forms.TextInput(attrs={'type':'date'}),
            'fecha_salida':forms.TextInput(attrs={'type':'date'}),
        } 

