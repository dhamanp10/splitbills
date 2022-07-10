from django.shortcuts import render,redirect

from app.models.Group import Group
from app.models.Transaction import Transaction
from app.models.User_Group_Bridge import UserGroupBridge
from app.models.User import User
from django.views import View

def del_group(request):
    group_id = request.GET.get('groupId')

    group=Group.get_Group_by_id(group_id)

    group.delete()
    return redirect('homepage')


def del_transaction(request):
    print(request.GET.get('transactionId'))
    transaction_id=int(str(request.GET.get('transactionId')))
    transaction=Transaction.get_Transaction_by_id(transaction_id)
    transaction.delete()
    return redirect('group')

class Groups(View):

    def get(self,request):
        group_id=None
        if request.GET.get('groupId'):
            group_id=request.GET.get('groupId')
            request.session['groupId'] = group_id
        else:
            group_id = request.session['groupId']

        transactions = Transaction.get_Transaction_by_group(group_id)
        group=Group.get_Group_by_id(group_id)


        bridges = UserGroupBridge.get_users(group_id)
        members = []

        if bridges:
            for member in bridges:
                members.append(User.get_User_by_id(member.user.id))
        data = {}
        data['members']= members
        data['transactions'] = transactions
        data['group'] = group
        # data['shares']=shares
        return render(request, 'group.html',data)


















