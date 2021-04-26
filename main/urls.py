from django.urls import path
from . import views

urlpatterns = [
	path('get-wallet/', views.getWallet, name="Get Wallet"),
	path('create-wallet/', views.createWallet, name="Create Wallet"),
	path('deposit-amount/', views.depositAmount, name="Deposit Amount"),
	path('withdrawn-amount/', views.withdrawAmount, name="Withdrawn Amount"),
	path('transaction-history/', views.trasactionHistory, name="Transaction History"),
	path('get-user/', views.currentUser, name="Get User")
]
