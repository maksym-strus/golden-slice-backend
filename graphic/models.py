from django.db import models


class Graphic(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    formula = models.CharField(max_length=100)
    start_point = models.FloatField()
    step = models.FloatField()
    number_of_points = models.IntegerField()
    accuracy = models.FloatField()