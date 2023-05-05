from base_app.base_repo import BaseRepo
from base_app.models import Sale


class SaleRepo(BaseRepo):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.model = Sale
        self.model_objects = self.model.objects
        self.filter_fields = [
            'store_name',
            'gift_card_number',
            'gift_card_balance',
            'price',
            'blockchain_network',
            'wallet_address',
            'contact_email'
        ]
        