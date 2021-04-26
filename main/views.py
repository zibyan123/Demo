# from .mappingserielizer import TodoSerializer
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WalletSerializer
from .serializers import HistorySerializer
from .models import Wallet
from .models import History
from django.contrib.auth.models import User as UserModel
import json
import pdb
@api_view(['GET'])
def getWallet(request):

 user = UserModel.objects.get(id=request.data['id'])
 wallet = Wallet.objects.get(User=user)
 # pdb.set_trace()
 serializer = WalletSerializer(wallet, many=False)

 return Response(serializer.data)


@api_view(['POST'])
def createWallet(request):
    multicurrency=request.data['amount']
    wallet= Wallet.objects.get(id=request.data['id'])
    serializer = WalletSerializer(multicurrency,many=False)
    # k=eval(multicurrency)
    pdb.set_trace()
    serializer.data['WalletAmount']=multicurrency

    if serializer.is_valid():
      # pdb.set_trace()
      serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def depositAmount(request):
  # pdb.set_trace()

  serializer = WalletSerializer(Wallet,data=request.data)
  if serializer.is_valid():

   serializer.save()
  return Response(serializer.data)
@api_view(['GET'])
def withdrawAmount(request):
      data=request.data

      amount=request.data['amount']
      # pdb.set_trace()
      Intamount=int(amount)
      # d = json.loads(data)
      # pdb.set_trace()
      totalamount= Wallet.objects.get(id=data['id'])


      serializer = WalletSerializer(totalamount, many=False)
      Inttotalamount= int(serializer.data['WalletAmount'])
      # pdb.set_trace()
      if Intamount<=Inttotalamount:
         withdrawnamount=Inttotalamount-Intamount
         transactionrecord = History.objects.all()
         newrecord = History()
         newrecord.TransactionType=request.data['type']
         newrecord.Amount=withdrawnamount
         newrecord.save()
         # pdb.set_trace()
         return Response(withdrawnamount)

      else:
         return HttpResponse("Not Enough Balance")
@api_view(['GET'])
def trasactionHistory(request):
      history = request.GET.dict()
      # pdb.set_trace()
      transactionrecord= History.objects.get(id=history['id'])

      serializer = HistorySerializer(transactionrecord, many=False)
      # pdb.set_trace()
      return Response(serializer.data)
@api_view(['GET'])
def currentUser(request):
       user= request.data

       currentuser =UserModel.objects.filter(id=user['id'])

       serializecurrentuser = serializers.serialize("json", currentuser)
       return JsonResponse(serializecurrentuser, safe=False)
       # serializer = WalletSerializer(user, many=False)
       # return Response(serializer.data)
#
# 	return Response(serializer.data)
# def find_email_or_user(request):
#     if request.method == "GET":
#         username = request.GET.get('username')
#         email = request.GET.get('email')
#         user_object = ''
#         if username:
#             user_object = User.objects.filter(username=username)
#             user_object = UserData.objects.filter(User=user_object)
#         else:
#             user_object = UserData.objects.filter(Email=email)
#         if user_object:
#             user_data_serialized = serializers.serialize("json", user_object)
#             return HttpResponse(user_data_serialized, content_type="text/json-comment-filtered")
#         else:
#             return HttpResponse(0, content_type="text/json-comment-filtered")
