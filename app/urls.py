"""splitbills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import login,home,signup,signup_mobile,login_with_mobile,group,create_transaction,create_group_example,settle_up,del_transaction,my_details
from .views.login import logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.Login.as_view(), name='login'),
    path('home', home.Index.as_view(), name='homepage'),
    path('logout',logout,name='logout'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('signup_mobile', signup_mobile.Signup_mobile.as_view(), name='signup_mobile'),
    path('signup_verify_otp', signup_mobile.signup_verify_otp, name='signup_verify_otp'),
    path('login_with_mobile', login_with_mobile.Login_with_mobile.as_view(), name='login_with_mobile'),
    path('verify_otp', login_with_mobile.verify_otp, name='verify_otp'),
    path('group',group.Groups.as_view(),name='group'),
    path('create_group', create_group_example.Example.as_view(), name='create_group'),
    path('create_transaction', create_transaction.Example.as_view(), name='create_transaction'),
    path('settle_up', settle_up.Settle_up.as_view(), name='settle_up'),
    path('group_delete', group.del_group, name='group_delete'),
    path('transaction_delete', del_transaction.del_transaction, name='transaction_delete'),
    path('my_details',my_details.My_details.as_view(), name='my_details'),
]
