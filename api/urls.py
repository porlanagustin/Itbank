from django.contrib import admin
from django.urls import path
from sucursales.views import SucursalLists,SucursalDetails
from prestamos.views import PrestamoPost,PrestamoDetails
from clientes.views import ClienteLists,ClienteDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clientes/<int:pk>',ClienteDetails.as_view()),
    path('api/clientes/',ClienteLists.as_view()),
    path('api/sucursales/<int:pk>/',SucursalDetails.as_view()),
    path('api/sucursales/',SucursalLists.as_view()),
    path('api/prestamodelete/<int:pk>',PrestamoDetails.as_view()),
    path('api/prestamopost/', PrestamoPost.as_view()) 
]
