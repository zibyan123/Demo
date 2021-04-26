from django.db import models
from django.contrib.auth.models import User



class Wallet(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    WalletAmount = models.CharField(max_length=1000)


class History(models.Model):
    TransactionType = models.CharField(max_length=75,blank=True, null=True)
    Amount = models.IntegerField(blank=True, null=True)
