from django.contrib import admin 
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # khi truy cập http://…/ thì tự động redirect sang /nv/
    path('', RedirectView.as_view(pattern_name='nv_list', permanent=False)),
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),  # tất cả nv/, ts/, bg/ đều map ở đây
]
