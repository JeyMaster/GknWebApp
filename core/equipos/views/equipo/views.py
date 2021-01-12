from datetime import date
from django.db.models import query
from docxtpl import DocxTemplate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.db import transaction
from django.db.models import Q
from core.equipos import models, forms
from config.settings import BASE_DIR


class DetailsEntregaView(LoginRequiredMixin,generic.TemplateView):

    model=models.Equipo_Para_Entregar_Detalles
    template_name='equipo/detalles_entrega.html'
    
    def get(self,request,*args,**kwargs):
        
        context=self.get_context_data()
        queryset=context['queryset']
        queryset=self.filtros(context)

        if request.GET.get('search'):
            queryset=self.search(queryset,request.GET.get('search'))

        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

       
        context['page_obj']=page_obj
        context['cantidad']=len(queryset)
        
        return render(request,template_name=self.template_name,context=context)
    
    def filtros(self,context,**kwargs):
        estado=self.request.GET.get('estado')
        categoria=self.request.GET.get('categoria')
        queryset=context['queryset']
        
        context['estado']=''
        context['categoria']=''
        queryset=self.model.objects.select_related()
        if estado and estado!='all':
            queryset=queryset.filter(
                id_equipo_para_entregar__id_equipo__estado=estado
            )
            context['estado']=estado

        if categoria and categoria!='all':
            queryset=queryset.filter(
                id_equipo_para_entregar__id_equipo__id_stock__categoria=categoria
            )
            context['categoria']=categoria
        
        return queryset
            

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        queryset=self.model.objects.select_related().filter(
                Q(id_equipo_para_entregar__id_equipo__estado='Et')
                |Q(id_equipo_para_entregar__id_equipo__estado='Pr')
                |Q(id_equipo_para_entregar__id_equipo__estado='Ua')
                ).order_by('fecha_preparacion')
        context['queryset']=queryset
        context['search']=True
        return context


    def search(self,query,busqueda):
        query=query.filter(
            Q(id_equipo_para_entregar__usuario_final__icontains=busqueda)
            |Q(id_equipo_para_entregar__id_equipo__service_tag__icontains=busqueda)
            |Q(id_equipo_para_entregar__nombre_equipo__icontains=busqueda)
        )
        return query

class EditEntregaView(LoginRequiredMixin,generic.FormView):
    template_name ='equipo/asignar.html'
    form_class= forms.PreparacionForm
    
    def get(self,request,id,*args,**kwargs):
        
        return render(request,self.template_name,context=self.get_context_data(id,**kwargs))

    def post(self,request,id,*args,**kwargs):
        with transaction.atomic():
            form_type=request.POST.get('form')
            
            context=self.get_context_data(id,*kwargs)
          
            if form_type=='form_principal':
                form=forms.PreparacionForm(request.POST,request.FILES)
                context['form']=form
                if form.is_valid():
                    nombre_equipo=form.cleaned_data['nombre_equipo']
                    preparado_por=form.cleaned_data['preparado_por']
                    service_tag=form.cleaned_data['service_tag']
                    usuario_final=form.cleaned_data['usuario_final']
                    configurado_por=form.cleaned_data['configurado_por']
                    fecha_termino_garantia=form.cleaned_data['fecha_termino_garantia']
                    solicitud=form.cleaned_data['solicitud']
                    estado=form.cleaned_data['estado']
                    
                    detalles=models.Equipo_Para_Entregar_Detalles.objects.get(id_equipo_para_entregar=id)

                    if solicitud!=None:
                        solicitud.name='solicitud_%s_%s.docx'%(service_tag,usuario_final)
                        detalles.solicitud=solicitud
                    
                    
               
                    detalles.preparado_por=preparado_por
                    detalles.configurado_por=configurado_por
                    
                    detalles.save()

                    equipo_pe=models.Equipo_Para_Entregar.objects.get(pk=id)
                    equipo_pe.nombre_equipo=nombre_equipo
                    equipo_pe.usuario_final=usuario_final

                    equipo_pe.save()
                    e=models.Equipo.objects.get(pk=equipo_pe.id_equipo.id_equipo)
                    e.service_tag=service_tag
                    e.estado=estado
                    e.fecha_termino_garantia=fecha_termino_garantia
                    e.save()

                    context['saved']=True

                    if detalles.solicitud!=None:
                        context['solicitud']=detalles.solicitud
                    else:
                        context['solicitud']=''
                    
                    if(estado=='Bs'):
                        query=models.Equipo_Para_Entregar_Detalles.objects.select_related().values(
                            'id_equipo_para_entregar__id_equipo__id_stock__modelo',
                            'id_equipo_para_entregar__id_equipo__id_stock__marca',
                            'site',
                        )
                        models.Basura_Electronica.objects.create(
                            descripcion='Equipo',
                            cantidad=1,
                            modelo=query[0].get('id_equipo_para_entregar__id_equipo__id_stock__modelo'),
                            marca=query[0].get('id_equipo_para_entregar__id_equipo__id_stock__marca'),
                            planta=query[0].get('site'),
                            responsable=preparado_por,
                            fecha_registro=date.today(),
                            no_serie=service_tag,
                            recolectado=False
                        )
                    return render(request,self.template_name,context)

                else:
                    context['saved']=False
                    return render(request,self.template_name,context)
            else:
                form=forms.AditionalInfo(request.POST)
                context['form_extra']=form
                if form.is_valid():
             
                    documentos=request.POST.get('documentos')

                    detalles=models.Equipo_Para_Entregar_Detalles.objects.get(id_equipo_para_entregar=id)
                    site=form.cleaned_data['site']
                    departamento=form.cleaned_data['departamento']
                    area=form.cleaned_data['area']
                    ubicacion_exacta=form.cleaned_data['ubicacion_exacta']
                    apps_especiales=form.cleaned_data['apps_especiales']
                    detalles.apps_especiales=apps_especiales
                    detalles.departamento=departamento
                    detalles.ubicacion_exacta=ubicacion_exacta
                    detalles.site=site
                    detalles.area=area
                    detalles.save()

                    if documentos:
                        nombre_equipo=request.POST.get('nombre_equipo')
                        configurado_por=request.POST.get('configurado_por')
                        preparado_por=User.objects.get(pk=request.POST.get('preparado_por')).username
                        usuario_final=request.POST.get('usuario_final')
                        service_tag=request.POST.get('service_tag')
                        modelo=request.POST.get('modelo')
                        categoria=request.POST.get('categoria')
                        multi_user=request.POST.get('multi_user')
                        apps_especiales=request.POST.get('apps_especiales').split(',')
                        apps='Sin aplicaciones'
                        fecha_preparacion=detalles.fecha_preparacion

                        if len(apps_especiales[0])!=0:
                            apps=''
                            contador=1
                            for app in apps_especiales:
                                apps+='%s.-%s   '%(contador,app)
                                contador=contador+1
                       
                        ctx={
                            'nombre_equipo':nombre_equipo,
                            'configurado_por':configurado_por,
                            'preparado_por':preparado_por,
                            'tag':service_tag,
                            'usuario_final':usuario_final,
                            'fecha_preparacion':fecha_preparacion,
                            'site':site,
                            'departamento':departamento,
                            'area':area,
                            'ubicacion_exacta':ubicacion_exacta,
                            'apps':apps,
                            'modelo':modelo
                        }
                        if multi_user:
                            ctx['multi_user']=multi_user
                        self.generar_documentos(ctx,id,categoria)
                        detalles=models.Equipo_Para_Entregar_Detalles.objects.get(id_equipo_para_entregar=id)
                        context['checklist']=detalles.check_list
                        context['certificado']=detalles.certificado_de_calidad
                        print(detalles.check_list)
                    return render(request,self.template_name,context)     

    def get_context_data(self,id, **kwargs):
        context = super().get_context_data(**kwargs)
       
        query=models.Equipo_Para_Entregar_Detalles.objects.select_related().values(
            'id_equipo_para_entregar__id_equipo__service_tag','id_equipo_para_entregar__id_equipo__estado',
            'id_equipo_para_entregar__id_equipo__fecha_termino_garantia',
            'id_equipo_para_entregar__nombre_equipo','id_equipo_para_entregar__usuario_final','preparado_por','fecha_preparacion',
            'configurado_por','id_equipo_para_entregar__id_equipo__id_stock__categoria','site','departamento','area',
            'id_equipo_para_entregar__id_equipo__id_stock__modelo','apps_especiales',
            'ubicacion_exacta','solicitud','check_list','certificado_de_calidad').filter(id_equipo_para_entregar=id)


        form=self.form_class({  'nombre_equipo':query[0].get('id_equipo_para_entregar__nombre_equipo'),
                                'preparado_por':query[0].get('preparado_por'),
                                'service_tag':query[0].get('id_equipo_para_entregar__id_equipo__service_tag'),
                                'usuario_final':query[0].get('id_equipo_para_entregar__usuario_final'),
                                'configurado_por':query[0].get('configurado_por'),
                                'site':query[0].get('site'),
                                'departamento':query[0].get('departamento'),
                                'area':query[0].get('area'),
                                'ubicacion_exacta':query[0].get('ubicacion_exacta'),
                                'estado': query[0].get('id_equipo_para_entregar__id_equipo__estado'),
                                'fecha_termino_garantia':query[0].get('id_equipo_para_entregar__id_equipo__fecha_termino_garantia')})
        
        form_extra=forms.AditionalInfo(
            {
                'site':query[0].get('site'),
                'departamento':query[0].get('departamento'),
                'area':query[0].get('area'),
                'ubicacion_exacta':query[0].get('ubicacion_exacta'),
                'apps_especiales':query[0].get('apps_especiales')
            }
         )
        context['categoria']=query[0].get('id_equipo_para_entregar__id_equipo__id_stock__categoria')
        context['modelo']=query[0].get('id_equipo_para_entregar__id_equipo__id_stock__modelo')
        context['form']=form
        context['solicitud']=query[0].get('solicitud')
        context['checklist']=query[0].get('check_list')
        context['certificado']=query[0].get('certificado_de_calidad')
        context['editar']=True
        context['id']=id
        context['form_extra']=form_extra
        return context

    def generar_documentos(self,context,id,categoria):
        ruta_checklist=''
        if categoria=='LT':
            ruta_checklist='media/assets/CHECK_LIST_LT_BASE.docx'
        else:
            ruta_checklist='media/assets/CHECK_LIST_PC_BASE.docx'
        
        ruta_certificado_calidad='media/assets/CERTIFICADO_CALIDAD.docx'

        doc=DocxTemplate(BASE_DIR/ruta_checklist)
        doc.render(context)
        ruta_checklist='media/checklist/checklist_%s_%s.docx'%(context.get('tag'),context.get('nombre_equipo'))
        doc.save(BASE_DIR/ruta_checklist)


        doc=DocxTemplate(BASE_DIR/ruta_certificado_calidad)
        doc.render(context)
        ruta_certificado_calidad='media/certificado/certificado_%s_%s.docx'%(context.get('tag'),context.get('nombre_equipo'))
        doc.save(BASE_DIR/ruta_certificado_calidad)

        detalles=models.Equipo_Para_Entregar_Detalles.objects.get(id_equipo_para_entregar=id)
        detalles.check_list='checklist/checklist_%s_%s.docx'%(context.get('tag'),context.get('nombre_equipo'))
        detalles.certificado_de_calidad='certificado/certificado_%s_%s.docx'%(context.get('tag'),context.get('nombre_equipo'))
        detalles.save()
       
class MoreDetailsViews(LoginRequiredMixin,generic.ListView):
    model=models.Equipo_Para_Entregar_Detalles
    template_name='equipo/more_details.html'

    def post(self,request,*args,**kwargs):
        context=self.get_context_data()
        querydict=request.POST
        queryset=context['queryset']

        for equipo in querydict:
            if equipo!='csrfmiddlewaretoken':
                query_update=models.Equipo_Para_Entregar_Detalles.objects.get(id_equipo_para_entregar=equipo)
                query_update.registro_en_inventario=True
                query_update.save()
                print(equipo) 

            paginator = Paginator(queryset, 10)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context['page_obj']=page_obj
            context['cantidad']=queryset.count()

        return render(request,self.template_name,context)

    def get(self,request,*args,**kwargs):

        context=self.get_context_data()
        queryset=self.filtros(context)

        if request.GET.get('search'):
            queryset=self.search()
            print('enter')
        
        paginator = Paginator(queryset, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj']=page_obj
        context['cantidad']=queryset.count()

        return render(request,self.template_name,context)
    
    def get_context_data(self, **kwargs):
        self.object_list = self.model.objects.select_related()

        queryset=self.model.objects.select_related().filter(
            Q(id_equipo_para_entregar__id_equipo__estado='Et')&
            Q(registro_en_inventario=False)
            )

        context = super().get_context_data(**kwargs)
        context['queryset']=queryset
        context['search']=True

        return context
    
    def filtros(self,context,**kwargs):
        queryset=context['queryset']
        inventario=self.request.GET.get('inventario')
        
        context['inventario']=False
    
        if inventario:
            
            queryset=self.model.objects.select_related().filter(
                Q(id_equipo_para_entregar__id_equipo__estado='Et')&
                Q(registro_en_inventario=True)
            )
            context['inventario']=True
        
        return queryset

    def search(self):
        
        queryset=self.model.objects.select_related()
        search=self.request.GET.get('search')

        queryset=queryset.filter(
            Q(id_equipo_para_entregar__nombre_equipo__icontains=search)|
            Q(id_equipo_para_entregar__id_equipo__service_tag__icontains=search)|
            Q(id_equipo_para_entregar__usuario_final__icontains=search)
        )
        return queryset


def generar_salida(request):
    
    nombre_equipo=request.GET.get('nombre_equipo')
    q=models.Equipo_Para_Entregar.objects.select_related().filter(nombre_equipo=nombre_equipo)
    service_tag=q[0].id_equipo.service_tag
    usuario= q[0].usuario_final.upper().split('.')
    modelo=q[0].id_equipo.id_stock.modelo
    
    ruta='media/assets/CREDENCIAL_BASE.docx'
    
    print(BASE_DIR/ruta)
    #path=(Path(__file__).resolve().parent.parent)
    doc=DocxTemplate(BASE_DIR/ruta)
    context={
        'usuario_final':'%s %s' %(usuario[0],usuario[1]),
        'nom_equipo':nombre_equipo,
        'modelo':modelo,
        'service_tag':service_tag,
    }

    doc.render(context)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    
    response['Content-Disposition'] = 'attachment; filename=SALIDA_%s.docx' %(nombre_equipo)
   
    doc.save(response)
    

    return response
