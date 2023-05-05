from django.test import TestCase
from base_app.models import Sale


class SaleControllerTestCase(TestCase):
    def setUp(self) -> None:
        data = {
            "store_name": "Amazon",
            "gift_card_number": "1123445",
            "gift_card_balance": 248,
            "price": 260,
            "blockchain_network": "Ethereum",
            "wallet_address": "0X2320F7A6571C9989164BCE6680B2E",
            "contact_email": "admin@watermelonmarkets.com"
        }
        sale_obj = Sale(**data)
        sale_obj.save()

    def test_get_sale(self) -> None:
        response = self.client.get(
            path='/admin/api/v0/administartors/sales/',
            data={
                'id': 1
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "Success")
        self.assertEqual(response.json()["data"]['store_name'], "Amazon")

    def test_update_sale_status(self) -> None:
        response = self.client.put(
            path='/admin/api/v0/administartors/sales/',
            data={
                'id': 1
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "Success")
        self.assertEqual(response.json()["message"], "status changed successfully")
