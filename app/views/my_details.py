from django.shortcuts import render, redirect
from app.forms import *



from django.views import View

from app.models.User_Group_Bridge import UserGroupBridge
from app.models.Share import Share
from app.models.User import User
from app.models.Group import Group

class My_details(View):
    def get(self, request):
        user_id = request.session.get('user')
        user = User.get_User_by_id(user_id)
        form = Edit_my_details(instance=user)
        return render(request, 'my_details.html',{'user':user,'form':form})

    def post(self, request):
        postData = request.POST
        user_id = request.session.get('user')
        user = User.get_User_by_id(user_id)
        form = Edit_my_details(request.POST,request.FILES,instance=user)


        user = form.save()
        form = Edit_my_details(instance=user)
        return render(request, 'my_details.html', {'user': user, 'form': form})