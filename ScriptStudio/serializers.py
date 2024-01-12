from rest_framework import serializers
from ScriptStudio.models import scripts

class scriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = scripts
        fields = '__all__'