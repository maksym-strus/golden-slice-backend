from rest_framework import serializers
from .models import Graphic


class GraphicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graphic
        fields = ['id', 'user_id', 'formula', 'start_point', 'step', 'number_of_points', 'accuracy']
