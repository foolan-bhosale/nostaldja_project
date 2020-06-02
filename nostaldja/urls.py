from django.urls import path
from .import views


urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('fads/', views.fad_list, name='fad_list'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('fads/new', views.fad_create, name='fad_create'),
    path('decades/<int:pk>/edit', views.decade_edit, name='decade_edit'),
    path('fads/<int:pk>/edit', views.fad_edit, name='fad_edit'),
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete'),

    #############             Class- based-views-path-urls            ##################
    path('class/decades/', views.DecadeListView.as_view(), name='decade_list'),
    path('class/decades/new/', views.DecadeCreateView.as_view(), name='decade_create'),
    path('class/decades/<int:pk>',
         views.DecadeDetailView.as_view(), name='decade_detail'),
    path('class/decades/<int:pk>/edit', views.DecadeEditView.as_view(),
         name='decade_edit'),
    path('class/decades/<int:pk>/delete',
         views.DecadeDeleteView.as_view(), name='decade_delete'),
]
