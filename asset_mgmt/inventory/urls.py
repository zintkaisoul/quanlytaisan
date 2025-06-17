from django.urls import path
from . import views

urlpatterns = [
    # NV
    path('nv/', views.nv_list, name='nv_list'),
    path('nv/add/', views.nv_create, name='nv_add'),
    path('nv/<pk>/edit/', views.nv_update, name='nv_edit'),
    path('nv/<pk>/delete/', views.nv_delete, name='nv_delete'),
    # tương tự cho TS và BG
    path('ts/', views.ts_list, name='ts_list'),
    path('ts/add/', views.ts_create, name='ts_add'),
    path('ts/<pk>/', views.ts_detail, name='ts_detail'),
    path('ts/<pk>/edit/', views.ts_update, name='ts_edit'),
    path('ts/<pk>/delete/', views.ts_delete, name='ts_delete'),
    path('ts/<pk>/qr/', views.ts_qr_code, name='ts_qr_code'),

    path('bg/', views.bg_list, name='bg_list'),
    path('bg/add/', views.bg_create, name='bg_add'),
    path('bg/<pk>/edit/', views.bg_update, name='bg_edit'),
    path('bg/<pk>/delete/', views.bg_delete, name='bg_delete'),
]