from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from core.equipos import models,forms

class ListPoolView(LoginRequiredMixin,generic.list.ListView):
    model=models.Equipo_Para_Entregar
    template_name='equipo_pool/equipos_pool.html'
    queryset=model.objects.select_related().filter(id_equipo__estado='Ep')
    context_object_name='equipos'
    paginate_by = 18
    
class AssignPoolView(LoginRequiredMixin,generic.FormView):
    template_name='equipo_pool/asignar_pool.html' 
    form_class=forms.AsignarPool  