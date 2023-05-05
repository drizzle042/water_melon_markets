from rest_framework.views import APIView
from admin_dashboard.controllers.sale_controller import SaleController


class SaleView(APIView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = SaleController()

    def get(self, request):
        return self.controller.get(request)
    
    def put(self, request):
        return self.controller.activate_or_deactivate(request)