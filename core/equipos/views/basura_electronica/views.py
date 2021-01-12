
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import query
from django.views import generic
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from core.equipos import forms, models, filters


class UpdateBasauraView(LoginRequiredMixin,generic.UpdateView):
    model=models.Basura_Electronica
    template_name='basura_electronica/basura_electronica.html'
    form_class=forms.BasuraElectronicaForm
    success_url='/basura/'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update']=True
        return context
    

class ListBasuraView(LoginRequiredMixin,generic.list.ListView):
    template_name='basura_electronica/listar_basura.html'
    model=models.Basura_Electronica
    queryset=model.objects.all()
    context_object_name='basura'

    def get(self,request,*args,**kwargs):

       
        context=self.get_context_data()
        queryset=context['filter'].qs
        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

       
        context['page_obj']=page_obj
        context['cantidad']=len(queryset)
        return render(request,self.template_name,context=context)

    def get_context_data(self, **kwargs):
        self.object_list = self.model.objects.all()
        context = super().get_context_data(**kwargs)
        responsables=User.objects.all().values('username').filter(is_superuser=False)
        filter=filters.BasuraElectronicaFilter(self.request.GET,self.queryset)
        context['filter']=filter
        return context

class AddBasuraView(LoginRequiredMixin,generic.CreateView):
    model=models.Basura_Electronica
    template_name='basura_electronica/basura_electronica.html'
    form_class=forms.BasuraElectronicaForm
    success_url='/basura/'