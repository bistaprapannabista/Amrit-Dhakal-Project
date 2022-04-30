from . import views
from django.urls import path



app_name = 'product'


urlpatterns = [
    path('search', views.search, name="search"),
    path('delete/<int:product_id>/',views.delete_product,name="delete_product"),
    path('edit/<int:product_id>/',views.edit_product,name="edit_product"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name="product"),
    path('<slug:category_slug>/', views.category, name="category") 
]
