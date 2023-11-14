from django.urls import path

from ecommerce_app import views
app_name='ecommerce_app'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('home/<slug:cslug>/',views.allProdCat,name='products_by_category'),
    path('<slug:cslug>/<slug:pro_slug>/',views.Prodetail,name='productdetail'),
]