from rest_framework import serializers
from notatetr import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'slug')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Note
        fields = ('content', 'user', 'slug')