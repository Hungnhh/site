from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(),name='index'),
    path('item/', views.item, name='item'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/',views.CreateItem.as_view(), name='create_item'),
    path('edit/<int:pk>', views.update_item, name='update_item'),
    path('delete/<int:pk>', views.delete_item, name='delete_item')
]