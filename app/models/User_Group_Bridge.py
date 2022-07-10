from django.db import models
from .Group import Group
from .User import User

class UserGroupBridge(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def register(self):
        self.save()




    @staticmethod
    def get_groups(User_Group_Bridge_user):
        try:
            return UserGroupBridge.objects.filter(user=User_Group_Bridge_user)
        except:
            return False

    @staticmethod
    def get_users(User_Group_Bridge_group):
        try:
            return UserGroupBridge.objects.filter(group=User_Group_Bridge_group)
        except:
            return False
