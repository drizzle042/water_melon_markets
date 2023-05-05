from django.urls import path
from seller_dashboard import views

app_name = "seller_dashboard"

urlpatterns = [
    path('api/v0/sellers/sale/', views.SaleView.as_view(), name='sales')
]