from base_app.base_controller import BaseController
from seller_dashboard.repos.sale_repo import SaleRepo
from seller_dashboard.serializers.sale_serializer import SaleSerializer


class SaleController(BaseController):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.repo = SaleRepo()
        self.serializer = SaleSerializer
        self.identifier = 'id'
        self.query_dict = {
            'is_active': 'active'
        }
