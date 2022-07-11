from django.shortcuts import render, redirect
from app.models.Transaction import Transaction

def del_transaction(request):
    print(request.GET.get('transaction_id'))
    transaction_id=int(str(request.GET.get('transaction_id')))
    transaction=Transaction.get_Transaction_by_id(transaction_id)
    transaction.delete()
    return redirect('group')