from django.shortcuts import render, redirect,HttpResponseRedirect

from django.contrib.auth.hashers import check_password

from app.models.User import User
from django.views import View


class Login(View):
    return_url=None
    def get(self, request):
        request.session['mobile_login_return_url'] = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.get_User_by_email(email)

        error_message = None
        if user:
            if check_password(password, user.password):
                request.session['user']=user.id
                request.session['user_name'] = user.first_name + user.last_name
                return redirect('homepage')
            else:
                error_message = 'Password Invalid..!!'
        else:
            error_message = 'Email Invalid..!!'
        data= {}
        data['error']=error_message
        data['email']=email
        return render(request, 'login.html', data)

def logout(request):
    request.session.clear()
    return redirect('login')
