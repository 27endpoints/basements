from django.db import models

# Create your models here.
class  mastermodel(models.Model):
    Resident_name = models.CharField(max_length=30)
    relative_location = models.CharField(max_length=30)
    Room_types = models.CharField(max_length=6, null=True)
    Lavatory = models.CharField(max_length=7, null=True)
    Estimated_walk = models.SmallIntegerField(null=True, blank=True)
    single_room_price = models.IntegerField(null=True, blank=True)
    double_room_price = models.IntegerField(null=True, blank=True)
    commune_room_price = models.IntegerField(null=True, blank=True)
    vacant_rooms = models.SmallIntegerField(default=0, blank=False)
    

    def __str__(self):
        return self.Resident_name


class home_page(models.Model):
    base_title = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.base_title
    

class about_page(models.Model):
    about_us = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.about_us



        


  