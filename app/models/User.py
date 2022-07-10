from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    image=models.ImageField(upload_to='user_images/')


    @staticmethod
    def get_all_users():
        return User.objects.all()

    def register(self):
        self.save()

    def isExist(self):
        if User.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_User_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_User_by_id(User_id):
        try:
            return User.objects.get(id=User_id)
        except:
            return False

    @staticmethod
    def get_User_by_phone(User_phone):
        try:
            return User.objects.get(phone=User_phone)
        except:
            return False
