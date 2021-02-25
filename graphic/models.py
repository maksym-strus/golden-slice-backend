from django.db import models


class Graphic(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    formula = models.CharField(max_length=100)
    start_point = models.FloatField()
    end_point = models.FloatField()
    accuracy = models.FloatField()
    number_of_points = models.IntegerField()