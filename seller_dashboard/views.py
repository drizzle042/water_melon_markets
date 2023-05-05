from rest_framework.views import APIView
from seller_dashboard.controllers.sale_controller import SaleController


class SaleView(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = SaleController()

    def post(self, request):
        return self.controller.create(request)