from django.db import models

# Create your models here.
class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=50, blank=True, null=True)
    gift_card_number = models.CharField(max_length=50, blank=True, null=True)
    gift_card_balance = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    blockchain_network = models.CharField(max_length=50, blank=True, null=True)
    wallet_address = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Gift Card with balance {self.gift_card_balance} by {self.store_name}"
