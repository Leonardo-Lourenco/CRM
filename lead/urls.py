from django.urls import path

from . import views

urlpatterns = [
    path('add-lead/', views.add_lead, name='add_lead'),  ## adicionando LEADS
    path('<int:pk>/', views.leads_detail, name='leads_detail'), ## detalhando os LEADS
    path('', views.leads_list, name='leads_list'),   ## listando LEADS


]
