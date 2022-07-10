from django.shortcuts import render,redirect
from django.views import View
from app.forms import *
from app.models.User import User
from app.models.User_Group_Bridge import UserGroupBridge
class Example(View):
    def get(self, request):
        users = User.get_all_users()
        form = Create_group()
        data = {}
        data['users'] = users
        data['form'] = form

        return render(request, 'create_group_example.html',data)

    def post(self, request):
        form = Create_group(request.POST, request.FILES)


        postData = request.POST

        members = postData.getlist('members')
        print('members')
        print(members)
        if form.is_valid():
            instance=form.save()
            groupId = instance.id
            user_group_bridge = UserGroupBridge(group=Group(id=groupId), user=User(id=request.session['user']))
            user_group_bridge.register()
            for memberId in members:
                user_group_bridge = UserGroupBridge(group=Group(id=groupId), user=User(id=memberId))
                user_group_bridge.register()
            return redirect('homepage')
        else:
            users = User.get_all_users()

            data = {}
            data['users'] = users
            data['form'] = form

            return render(request, 'create_group.html', data)



    def validategroup(self, group):
        error_message = None

        if not group.name:
            error_message = "Group Name Requird !!"
        elif len(group.name) < 3:
            error_message = "Group Name must be 3 character long or more !!"

        return error_message
