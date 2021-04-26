from rest_framework import serializers
from .models import Wallet
from .models import History
class WalletSerializer(serializers.ModelSerializer):
	class Meta:
		model = Wallet
		fields ='__all__'
class HistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = History
		fields ='__all__'
