from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models.Group import Group
from app.models.Transaction import Transaction
from app.models.User_Group_Bridge import UserGroupBridge
from app.models.User import User
from app.models.Share import Share
from django.views import View

from collections import defaultdict
import heapq

class from_to:
    def __init__(self,f,t,a):
        self.from_user = f
        self.to_user = t
        self.amount = a


class Settle_up(View):
    def get(self,request):
        group_id=request.session['groupId']
        parameter=[]

        transactions=Transaction.get_Transaction_by_group(group_id)
        for transaction in transactions:
            shares=Share.get_Share_by_transaction_id(transaction.id)
            for share in shares:
                if transaction.user.id != share.User.id:
                    temp=[]
                    temp.append(share.User.id)
                    temp.append(transaction.user.id)
                    amt=(transaction.amount * share.percent)/100
                    temp.append(amt)
                    parameter.append(temp)


        answers=self.simplify_debts(parameter)
        data=[]
        for f,t,a in answers:
            from_user=User.get_User_by_id(f)
            to_user=User.get_User_by_id(t)
            temp=from_to(from_user,to_user,a)
            data.append(temp)
        return render(request, 'settle_up.html',{'data':data})


    def simplify_debts(self,parameter):
        total = defaultdict(int)

        for transaction in parameter:
            giver, receiver, amount = transaction
            total[giver] -= amount
            total[receiver] += amount

        credit = []
        debit = []

        for name, amount in total.items():
            if amount > 0:
                credit.append((-amount, name))
            if amount < 0:
                debit.append((amount, name))

        heapq.heapify(credit)
        heapq.heapify(debit)

        answer = []

        while credit and debit:
            credit_value, credit_name = heapq.heappop(credit)
            debit_value, debit_name = heapq.heappop(debit)

            if credit_value < debit_value:
                amount_left = credit_value - debit_value
                answer.append((debit_name, credit_name, -1 * debit_value))
                heapq.heappush(credit, (amount_left, credit_name))

            elif debit_value < credit_value:
                amount_left = debit_value - credit_value
                answer.append((debit_name, credit_name, -1 * credit_value))
                heapq.heappush(debit, (amount_left, debit_name))

            else:
                answer.append((debit_name, credit_name, -1 * credit_value))

        return answer




















