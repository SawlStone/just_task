from django.urls import path

from api import views

urlpatterns = [
    path('create/', views.TableOrderCreateApiView.as_view(), name='table_order_create')
]
