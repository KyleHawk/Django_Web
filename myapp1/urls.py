from django.urls import path
from . import views
app_name = 'myapp1'
urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('item/<int:type_no>', views.get_items),
 path('myapp1/<int:type_no>', views.detail, name='detail'),
 path('myapp1/items/', views.items),
 path('myapp1/items/<int:item_id>', views.itemdetail, name='itemdetail'),
 path('myapp1/placeorder/', views.placeorder, name='placeorder'),
]