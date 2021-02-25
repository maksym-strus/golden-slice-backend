from rest_framework import serializers
from .models import Graphic


class GraphicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graphic
        fields = ['user_id', 'formula', 'start_point', 'end_point', 'accuracy', 'number_of_points']