from django.db import models


# Create your models here.

class USER(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='unknown')

    class Meta:
        db_table = 'USER'


class DATA(models.Model):
    email = models.CharField(max_length=100, default='unknown')
    order_date = models.DateField()
    company = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    weight = models.FloatField()
    request_for_shipment = models.CharField(max_length=100)
    tracking_id = models.CharField(max_length=100)
    shipment_size = models.CharField(max_length=100)
    box_count = models.IntegerField()
    specification = models.CharField(max_length=100)
    checklist_quantity = models.CharField(max_length=100)

    class Meta:
        db_table='DATA'
