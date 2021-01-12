from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views import generic
from django.shortcuts import render,redirect
from django.db import transaction
from core.equipos import models, forms


class AssignStockView(LoginRequiredMixin,generic.FormView):
    template_name ='equipo/asignar.html'
    form_class= forms.PreparacionForm

    def get(self,request,id,*args,**kwargs):
        stock=models.Stock.objects.get(pk=id)
        ctx={'model':stock.modelo,'form':self.form_class}
        ctx['solicitud']=''
        return render(request,self.template_name,ctx)

    def post(self,request,id,*args,**kwargs):
        with transaction.atomic():
            form=self.form_class(request.POST)

            if form.is_valid():
                nombre_equipo=form.cleaned_data['nombre_equipo']
                preparado_por=form.cleaned_data['preparado_por']
                service_tag=form.cleaned_data['service_tag']
                usuario_final=form.cleaned_data['usuario_final']
                configurado_por=form.cleaned_data['configurado_por']
                solicitud=form.cleaned_data['solicitud']
                estado=form.cleaned_data['estado']
                fecha_preparacion=date.today()
                
                id_stock=models.Stock.objects.get(pk=id)
                id_stock.cantidad=id_stock.cantidad-1
                id_stock.save()

                equipo = models.Equipo.objects.create(id_stock=id_stock,service_tag=service_tag,estado=estado)

                id_equipo=models.Equipo.objects.get(pk=equipo.id_equipo)

                equipo_para_entregar=models.Equipo_Para_Entregar.objects.create(nombre_equipo=nombre_equipo,id_equipo=id_equipo
                                                                                ,usuario_final=usuario_final)

                
                equipo_para_entregar_id=models.Equipo_Para_Entregar.objects.get(pk=equipo_para_entregar.id_equipo_para_entregar)

                models.Equipo_Para_Entregar_Detalles.objects.create(id_equipo_para_entregar=equipo_para_entregar_id,
                                                                    preparado_por=preparado_por,configurado_por=configurado_por,
                                                                    fecha_preparacion=fecha_preparacion,solicitud=solicitud
                                                                    )
                return redirect('/stock/')
            else:
                return render(request,self.template_name,{'form':form})
  
class ListStockView(LoginRequiredMixin,generic.ListView):

    template_name = "stock/listar_stock.html"
    model = models.Stock

    def get(self,request,*args,**kwargs):
        context=self.get_context_data()
        queryset=context['queryset']
        queryset=self.filtros(request)
        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

       
        context['page_obj']=page_obj
        context['cantidad']=len(queryset)
        
        return render(request,template_name=self.template_name,context=context)

       
    def get_context_data(self, **kwargs):
        queryset= self.model.objects.all().order_by('modelo')
        self.object_list=queryset
        context = super().get_context_data(**kwargs)
        context['queryset']=queryset
        return context

    def filtros(self,request):
        context=self.get_context_data()
        queryset=context['queryset']
        categoria=request.GET.get('categoria')
        
        if categoria:
             queryset=queryset.filter(categoria=categoria)
       
        return queryset


    
 
