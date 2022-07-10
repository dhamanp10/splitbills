from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    total=models.IntegerField(default=0)
    image = models.ImageField(upload_to='group_images/',default='group_images/no-image.jpg')

    def register(self):
        self.save()
        return self.id



    @staticmethod
    def get_Group_by_id(Group_id):
        try:
            return Group.objects.get(id=Group_id)
        except:
            return False

    @staticmethod
    def update_total(Group_id,amount):
        group=Group.objects.get(id=Group_id)
        group.total=group.total+amount
        group.save()