from django.shortcuts import render,redirect
from app.models.User import User
from app.models.Group import Group
from app.models.User_Group_Bridge import UserGroupBridge
from django.views import View



class Index(View):

    # def post(self,request):
    #     product=request.POST.get('product')
    #     remove= request.POST.get('remove')
    #     cart= request.session.get('cart')
    #     if cart:
    #         quantity=cart.get(product)
    #         if quantity:
    #             if remove:
    #                 if quantity<=1:
    #                     cart.pop(product)
    #                 else:
    #                     cart[product] = quantity - 1
    #
    #             else:
    #                 cart[product] = quantity + 1
    #         else:
    #             cart[product] = 1
    #     else:
    #         cart={}
    #         cart[product] = 1
    #     request.session['cart']=cart
    #     print(request.session['cart'])
    #     return redirect('homepage')


    def get(self,request):
        request.session['phone'] = None
        request.session['random_otp'] = None
        request.session['groupId']=None
        user=User.get_User_by_id(request.session['user'])

        bridges = UserGroupBridge.get_groups(user)
        groups=[]

        if bridges:
            for gName in bridges:

                groups.append(Group.get_Group_by_id(gName.group.id))

        data = {}
        data['groups'] = groups


        return render(request, 'index.html',data)


















