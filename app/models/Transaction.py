import datetime

from django.db import models
from .User import User
from .Group import Group

class Transaction(models.Model):
    title=models.CharField(max_length=50,default='')
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    amount=models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='Transaction_images/',default='group_images/no-image.jpg')
    Group=models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    date=models.DateField(default=datetime.datetime.now)

    def register(self):
        self.save()

    @staticmethod
    def update_Transaction(Transaction_id,amount,user,group):
        transaction=Transaction.objects.get(id=Transaction_id)
        transaction.amount=amount
        transaction.user=user
        transaction.Group=group
        transaction.save()

    @staticmethod
    def get_Transaction_by_id(Transaction_id):
        try:
            return Transaction.objects.get(id=Transaction_id)
        except:
            return False

    @staticmethod
    def get_Transaction_by_group(group_id):
        try:
            return Transaction.objects.filter(Group=group_id)
        except:
            return False
