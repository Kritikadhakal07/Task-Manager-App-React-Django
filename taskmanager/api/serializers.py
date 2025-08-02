from rest_framework import serializers
from .models import Task
#A serializer in Django REST Framework is used to convert 
# complex data types like Django models or querysets into 
# native Python data types (like dictionaries) — 
# which can then be easily rendered into JSON, XML, etc.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'