from django.test import TestCase


class SaleControllerTestCase(TestCase):
    def test_create_sale(self) -> None:
        response = self.client.post(
            path='/sellers/api/v0/sellers/sale/',
            data={
                "store_name": "Amazon",
                "gift_card_number": "1123445",
                "gift_card_balance": 248,
                "price": 260,
                "blockchain_network": "Ethereum",
                "wallet_address": "0X2320F7A6571C9989164BCE6680B2E",
                "contact_email": "admin@watermelonmarkets.com"
            },
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "Success")
        self.assertEqual(response.json()["message"], "Sale posted successfully.")
