from django.db import models
from .Transaction import Transaction
from .User import User


class Share(models.Model):
    percent=models.PositiveIntegerField(default=None)
    Transaction=models.ForeignKey(Transaction, on_delete=models.CASCADE)
    User=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def register(self):
        self.save()

    def isExist(self):
        if Share.objects.filter(email=self.email):
            return True
        return False


    @staticmethod
    def get_Share_by_transaction_id(transaction_id):
        try:
            return Share.objects.filter(Transaction=transaction_id)
        except:
            return False

    @staticmethod
    def get_Share_by_transaction_id_user(transaction_id,user):
        try:
            return Share.objects.get(Transaction=transaction_id,User=user)
        except:
            return False