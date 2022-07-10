from django.shortcuts import render, redirect
from app.forms import *
from django.contrib.auth.hashers import make_password


from django.views import View

from app.models.User_Group_Bridge import UserGroupBridge
from app.models.Share import Share
from app.models.User import User
from app.models.Group import Group

class Example(View):
    def get(self, request):
        members=UserGroupBridge.get_users(request.session['groupId'])
        form=Create_transaction()
        data={}
        data['members']=members
        data['form'] = form
        return render(request, 'create_transaction_example.html',data)

    def post(self,request):
        form = Create_transaction(request.POST, request.FILES)
        postdata = request.POST
        user=postdata.get('user')
        amount = postdata.get('amount')
        error_message = None
        value = {
            'user': user,
            'amount': amount,
        }
        error_message = self.validateUser(value)
        if error_message:
            members = UserGroupBridge.get_users(request.session['groupId'])
            data = {}
            data['error']=error_message
            data['values']=value
            data['members'] = members
            data['form'] = form
            return render(request, 'create_transaction_example.html', data)

        if form.is_valid():
            amount=int(str(postdata.get('amount')))
            print('amount:'+str(amount))
            share_option=postdata.get('share_option')
            members = UserGroupBridge.get_users(request.session['groupId'])
            instance = form.save()
            transaction_id = instance.id
            user = User.get_User_by_id(int(str(postdata.get('user'))))
            Group.update_total(request.session['groupId'],amount)
            group=Group.get_Group_by_id(request.session['groupId'])
            Transaction.update_Transaction(transaction_id,amount,user,group)
            for member in members:
                temp=None
                if share_option=='1':
                    print('percent')
                    temp='percent'+str(member.user.id)
                else:
                    print('equal')
                    temp = 'equal' + str(member.user.id)
                print("value qwertyuiopasdfghjkl:"+str(postdata.get('equal1')))
                share=Share()
                share.percent=int(str(postdata.get(temp)))
                share.User=User.get_User_by_id(member.user.id)
                share.Transaction=Transaction.get_Transaction_by_id(transaction_id)
                share.register()
            return redirect('group')


        else:
            members = UserGroupBridge.get_users(request.session['groupId'])
            data = {}
            data['members'] = members
            data['form'] = form
            return render(request, 'create_transaction_example.html', data)


    def validateUser(self, value):
        error_message = None

        if not value['user']:
            error_message = "please select paid by!!"
        elif not value['amount']:
            error_message = "Amount Requird !!"
        return error_message
