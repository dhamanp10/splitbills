from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password

from app.models.User import User
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = request.session['phone']
        email = postData.get('email')
        password = postData.get('password')
        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        user = User(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateUser(user)

        # saving
        if not error_message:
            user.password = make_password(user.password)
            user.register()
            request.session['phone']=None
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateUser(self, user):
        error_message = None

        if not user.first_name:
            error_message = "First Name Requird !!"
        elif len(user.first_name) < 3:
            error_message = "First Name must be 3 character long or more !!"
        elif not user.last_name:
            error_message = "Last Name Requird !!"
        elif len(user.last_name) < 4:
            error_message = "Last Name must be 4 character long or more !!"
        elif not user.phone:
            error_message = "Phone Number Required !!"
        elif len(user.phone) != 10:
            error_message = "Phone Number Must Be 10 Digit long"
        elif not user.email:
            error_message = "Email Required !!"
        elif len(user.email) < 5:
            error_message = "Email must Be 5 character long"
        elif not user.password:
            error_message = "Password Required !!"
        elif len(user.password) < 6:
            error_message = "Password must Be 6 character long"
        elif user.isExist():
            error_message = "Email Address Already Registered.."
        return error_message
