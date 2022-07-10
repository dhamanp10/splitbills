from django.contrib import admin
from .models.User import User
from .models.Group import Group
from .models.Share import Share
from .models.Transaction import Transaction
from .models.User_Group_Bridge import UserGroupBridge
# Register your models here.
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Share)
admin.site.register(Transaction)
admin.site.register(UserGroupBridge)