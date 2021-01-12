from core.equipos.views.equipo_pool.views import AssignPoolView, ListPoolView
from django.urls import path
from core.equipos.views.equipo.views import *
from core.equipos.views.basura_electronica.views import *
from core.equipos.views.stock.views import *


urlpatterns=[
    path('',DetailsEntregaView.as_view()),
    path('details/',MoreDetailsViews.as_view()),
    path('editar/<str:id>',EditEntregaView.as_view()),
    path('basura/',ListBasuraView.as_view()),
    path('basura/update/<slug:pk>',UpdateBasauraView.as_view()),
    path('basura/add/',AddBasuraView.as_view()),
    path('stock/',ListStockView.as_view()),
    path('stock/asignar/<str:id>',AssignStockView.as_view()),
    path('pool/',ListPoolView.as_view()),
    path('pool/assign',AssignPoolView.as_view()),
    path('generar/',generar_salida),
]