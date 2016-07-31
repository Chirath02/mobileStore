from audioop import reverse

from django.db import models

class Mobile(models.Model):
    # elements for handling text
    model_name = models.CharField(max_length=300)


    # integer field for battery capacity
    battery_capacity = models.IntegerField()
    quantity = models.IntegerField()

    # float field for Mobile Features

    back_cam = models.FloatField()
    ram = models.FloatField()

    price = models.FloatField()


    # images are uploaded into /media/mobile/
    img = models.ImageField()

    def get_absolute_url(self):
        return reverse('mobile_detail', keywargs={'pk': self.pk})

