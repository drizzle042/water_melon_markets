from django.urls import path
from admin_dashboard import views

app_name = "admin_dashboard"

urlpatterns = [
    path('api/v0/administartors/sales/', views.SaleView.as_view(), name='sales')
]